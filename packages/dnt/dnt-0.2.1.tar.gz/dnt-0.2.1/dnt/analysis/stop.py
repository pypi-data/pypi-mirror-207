from shapely.geometry import Point, Polygon, LineString, box
import geopandas as gpd, pandas as pd
from tqdm import tqdm

class StopAnalyzer():
    def __init__(self, h_coords, v_coords, event_dict, stop_iou=0.97, frame_buffer=5, verbose=True):
        self.hzones = StopAnalyzer.gen_zones(h_coords)
        self.vzones = StopAnalyzer.gen_zones(v_coords)
        self.event_dict = event_dict
        self.stop_iou = stop_iou
        self.frame_buffer = frame_buffer
        self.verbose = verbose
    
    def analysis(self, track_file, result_file=None, output_file=None, video_index=None, video_tot=None):
        
        tracks = pd.read_csv(track_file, header=None, sep=',')

        tracks = self.__stop_scan(tracks, video_index, video_tot)
        tracks = self.__event_identify(tracks, video_index, video_tot)
        results = self.__event_count(tracks, video_index, video_tot)

        if result_file:
            results.to_csv(result_file, index=False)

        if output_file:
            tracks.to_csv(output_file, header=None, index=False)
    
    def __stop_scan(self, tracks, video_index, video_tot):
        vehicles = tracks[1].unique()

        pbar = tqdm(total=len(vehicles), unit=' tracks')
        if video_index and video_tot:
            pbar.set_description_str("Scan stops {} of {}".format(video_index, video_tot))
        else:
            pbar.set_description_str("Scan stops ")

        for vehicle in vehicles:
            track = tracks[tracks[1] == vehicle].sort_values(by=0)

            for i in range(self.frame_buffer, len(track)):

                index = track.iloc[i].name

                bb0 = [track.iloc[i-self.frame_buffer, 2], track.iloc[i-self.frame_buffer, 3], 
                       track.iloc[i-self.frame_buffer, 4], track.iloc[i-self.frame_buffer, 5]]
                bb1 = [track.iloc[i, 2], track.iloc[i, 3], track.iloc[i, 4], track.iloc[i, 5]]
                tracks.at[index, 6] = StopAnalyzer.iou(bb0, bb1)

                center = Point(track.iloc[i,2]+track.iloc[i,4], track.iloc[i,3]+track.iloc[i,5])
                for j in range(len(self.vzones)):
                    if center.within(self.vzones[j]):
                        tracks.loc[tracks[1]==vehicle, 7]=j
                        break
                
                bb = box(track.iat[i, 2], track.iat[i, 3], track.iat[i, 2] + track.iat[i, 4], track.iat[i, 3] + track.iat[i, 5])
                for j in range(len(self.hzones)):
                    if bb.intersects(self.hzones[j]):
                        if j > tracks.at[index, 8]:
                            tracks.at[index, 8] = j
            if self.verbose:
                pbar.update()

        pbar.close()

        return tracks
    
    def __event_identify(self, tracks, video_index, video_tot):

        pbar = tqdm(total=len(tracks), unit=' frames')
        if video_index and video_tot:
            pbar.set_description_str("Identify events {} of {}".format(video_index, video_tot))
        else:
            pbar.set_description_str("Identify events ")

        for i in range(len(tracks)):

            if tracks.iat[i, 6] >= self.stop_iou:
        
                vzone = tracks.iat[i, 7]
                hzone = tracks.iat[i, 8]
                frame = tracks.iat[i, 0]
                veh = tracks.iat[i, 1]

                vehs_inlane = tracks.loc[(tracks[0]==frame) & (tracks[1]!=veh) & (tracks[7]==vzone) & (tracks[8]>hzone)]

                if len(vehs_inlane)==0:
                    
                    pre_key = -1
                    for key in self.event_dict:

                        if key >= pre_key:
                            pre_key = key
                            if tracks.iat[i, 8] in self.event_dict[key]:
                                tracks.iat[i, 9] = key

            if self.verbose:
                pbar.update()
        
        pbar.close()

        return tracks
    
    def __event_count(self, tracks, video_index, video_tot):


        pbar = tqdm(unit='events')
        results = []

        for key in self.event_dict:

            vehicles = tracks.loc[tracks[9]==key][1].unique()

            if video_index and video_tot:
                pbar.set_description_str("Count event {} for {} of {}".format(key, video_index, video_tot))
            else:
                pbar.set_description_str("Count event {}".format(key))

            pbar.total = len(vehicles)
            for vehicle in vehicles:

                track = tracks[(tracks[1] == vehicle) & (tracks[9] == key)]

                start_frame = int(track[0].min())
                end_frame = int(track[0].max())
                vzone = track[7].mode()[0]
                results.append([key, vehicle, vzone, start_frame, end_frame])
                
                pbar.update()

        results = pd.DataFrame(results, columns=['EVENT', 'TRACKID', 'LANE', 'START_FRAME', 'END_FRAME'])
        pbar.close()

        return results
    
    @staticmethod
    def export_label(track_file, analysis_file, label_file, vid_field=1, label_field=10, frame_field=0,
                     event_label=None, vid_disp=True, verbose=True):
        
        tracks = pd.read_csv(track_file, header=None)
        results = pd.read_csv(analysis_file)

        pbar = tqdm(total=len(tracks), desc='Generate labels ', unit=' frames')
        for index, track in tracks.iterrows():

            vid = int(track[vid_field])
            
            selected = results.loc[(results['START_FRAME']<=track[frame_field]) & 
                                   (results['END_FRAME']>=track[frame_field]) &
                                   (results['TRACKID']==track[vid_field])]
            if len(selected)>0:
                
                event = selected.iloc[0]['EVENT']

                if event_label:
                    tracks.at[index, label_field] = str(vid)+"-"+str(event_label[event])
                else:
                    tracks.at[index, label_field] = str(vid)+"-"+str(event)

            else:
                if vid_disp:
                    tracks.at[index, label_field] = str(vid)
                else:
                    tracks.at[index, label_field] = '-1'

            if verbose:
                pbar.update()

        pbar.close()

        tracks.to_csv(label_file, header=None, index=False)

        if verbose:
            print('Write to {}'.format(label_file))


    @staticmethod
    def iou(bb1, bb2):
        """
        Calculate the Intersection over Union (IoU) of two bounding boxes.
        Parameters
        ----------
        bb1 : [x1, y1, w, h]
            x1, y1 - top left corner
            w, h - width and height
        bb2 : [x1, y1, w, h]
            x1, y1 - top left corner
            w, h - width and height
        Returns
        -------
        iou: float [0, 1]
        """

        assert bb1[0] < bb1[0] + bb1[2]
        assert bb1[1] < bb1[1] + bb1[3]
        assert bb2[0] < bb2[0] + bb2[2]
        assert bb2[1] < bb2[1] + bb2[3]

        # determine the coordinates of the intersection rectangle
        x_left = max(bb1[0], bb2[0])
        y_top = max(bb1[1], bb2[1])
        x_right = min(bb1[0]+bb1[2], bb2[0]+bb2[2])
        y_bottom = min(bb1[1]+bb1[3], bb2[1]+bb2[3])

        if x_right < x_left or y_bottom < y_top:
            return 0.0

        # The intersection of two axis-aligned bounding boxes is always an
        # axis-aligned bounding box
        intersection_area = (x_right - x_left) * (y_bottom - y_top)

        # compute the area of both AABBs
        bb1_area = bb1[2] * bb1[3]
        bb2_area = bb2[2] * bb2[3]

        # compute the intersection over union by taking the intersection
        # area and dividing it by the sum of prediction + ground-truth
        # areas - the interesection area
        iou = intersection_area / float(bb1_area + bb2_area - intersection_area)
        assert iou >= 0.0
        assert iou <= 1.0
        return iou
    
    @staticmethod
    def gen_zones(line_coords):
        """
            Generate a list of shapely polygons
            Inputs:
                line_coords: a list of line coords ([[(x11, y11),(x12, y12)], [(x21, y21),(x22, y22)], ...])
            Returns:
                A list of PloyGons  
        """

        zones = []
        for i in range(1, len(line_coords)):
            shell = line_coords[i-1] + [line_coords[i][1], line_coords[i][0]]
            zones.append(Polygon(shell))        

        return zones

if __name__ == "__main__":
    pass