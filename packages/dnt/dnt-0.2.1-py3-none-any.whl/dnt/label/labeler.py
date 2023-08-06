import cv2
import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm
import pandas as pd
import os

class Labeler:
    def __init__(self, method='opencv', frame_field=0,
             label_fields=[1], color_field=1, zoom_factor=1, line_thickness=1,
             color_bgr = (0, 255, 0), compress_message=False, nodraw_empty=True):
        
        self.method = method
        self.frame_field = frame_field
        self.label_fields=label_fields
        self.color_field=color_field
        self.zoom_factor=zoom_factor 
        self.line_thickness=line_thickness
        self.color_bgr = color_bgr
        self.compress_message=compress_message
        self.nodraw_empty = nodraw_empty
    
    def draw(self, label_file, input_video, output_video, start_frame=None, end_frame=None, 
             video_index=None, video_tot=None):
        tracks = pd.read_csv(label_file, header=None)
        
        cmap = plt.get_cmap('tab20b')
        colors = [cmap(i)[:3] for i in np.linspace(0, 1, 20)]

        cap = cv2.VideoCapture(input_video)
        if not cap.isOpened():
            raise IOError("Couldn't open webcam or video")

        if start_frame is None:
            start_frame = 0
        if end_frame is None:
            end_frame = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))-1

        tot_frames = end_frame - start_frame + 1       
        fps = int(cap.get(cv2.CAP_PROP_FPS))
        width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        writer = cv2.VideoWriter(output_video, fourcc, fps, (width, height))

        pbar = tqdm(total=tot_frames, unit=" frames")
        if self.compress_message:
            pbar.set_description_str("Labeling")
        else:
            if video_index and video_tot:
                pbar.set_description_str("Labeling {} of {}".format(video_index, video_tot))
            else:
                pbar.set_description_str("Labeling {} ".format(input_video))

        cap.set(cv2.CAP_PROP_POS_FRAMES, start_frame)
        while cap.isOpened():
            pos_frame = int(cap.get(cv2.CAP_PROP_POS_FRAMES))
            ret, frame = cap.read()
            if (not ret) or (pos_frame>end_frame):
                break
            
            #boxes = tracks.query('@tracks[0]==2').values.tolist()
            boxes = tracks[tracks.iloc[:,self.frame_field]==pos_frame].values.tolist()
            #boxes = tracks.loc[tracks.columns[0]==pos_frame].values.tolist()
            
            for box in boxes:
                x1 = int(box[2])
                y1 = int(box[3])
                x2 = x1 + int(box[4])
                y2 = y1 + int(box[5])

                color = colors[int(box[self.color_field]) % len(colors)]
                color = [i * 255 for i in color]
                
                label_txt = ''
                for field in self.label_fields:
                    if (str(box[field]).strip() == '-1'):
                        if self.nodraw_empty:
                            label_txt += ''
                        else:
                            label_txt += str(box[field]) + ' '
                    else:
                        label_txt += str(box[field]) + ' '
                        
                label_txt = label_txt.strip()

                if label_txt:
                    cv2.rectangle(frame, (x1, y1), (x2, y2), color, self.line_thickness)
                    cv2.rectangle(frame, (x1, int(y1-30*self.zoom_factor)), (x1+len(label_txt)*int(17*self.zoom_factor), y1), 
                              color, -1)
                    cv2.putText(frame,str(label_txt),(int(x1), int(y1-int(10*self.zoom_factor))), 
                            0, 0.75*self.zoom_factor, (255,255,255), 1)

            writer.write(frame)
            key = cv2.waitKey(1) & 0xFF
            if key == ord("q"):
                break
            
            pbar.update()

        cv2.destroyAllWindows()
        cap.release()
        writer.release()

    
    def draw_lines(self, lines, input_video, output_video, start_frame=None, end_frame=None, video_index=None, video_tot=None):
        cap = cv2.VideoCapture(input_video)
        if not cap.isOpened():
            raise IOError("Couldn't open webcam or video")

        if start_frame is None:
            start_frame = 0
        if end_frame is None:
            end_frame = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))-1

        tot_frames = end_frame - start_frame + 1       
        fps = int(cap.get(cv2.CAP_PROP_FPS))
        width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        writer = cv2.VideoWriter(output_video, fourcc, fps, (width, height))

        pbar = tqdm(total=tot_frames, unit=" frames")
        if self.compress_message:
            pbar.set_description_str("Labeling")
        else:
            if video_index and video_tot:
                pbar.set_description_str("Labeling {} of {}".format(video_index, video_tot))
            else:     
                pbar.set_description_str("Labeling {} ".format(input_video))

        cap.set(cv2.CAP_PROP_POS_FRAMES, start_frame)
        while cap.isOpened():
            pos_frame = int(cap.get(cv2.CAP_PROP_POS_FRAMES))
            ret, frame = cap.read()
            if (not ret) or (pos_frame>end_frame):
                break

            for line in lines:
                cv2.line(frame, (int(line[0]), int(line[1])), (int(line[2]), int(line[3])), self.color_bgr, self.line_thickness)

            writer.write(frame)
            key = cv2.waitKey(1) & 0xFF
            if key == ord("q"):
                break
            
            pbar.update()

        cv2.destroyAllWindows()
        cap.release()
        writer.release()

    def clip(self, input_video, output_video, start_frame=None, end_frame=None):
        cap = cv2.VideoCapture(input_video)
        if not cap.isOpened():
            raise IOError("Couldn't open webcam or video")

        if start_frame is None:
            start_frame = 0
        if end_frame is None:
            end_frame = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))-1

        tot_frames = end_frame - start_frame + 1       
        fps = int(cap.get(cv2.CAP_PROP_FPS))
        width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        writer = cv2.VideoWriter(output_video, fourcc, fps, (width, height))

        pbar = tqdm(total=tot_frames, unit=" frames")
        if self.compress_message:
            pbar.set_description_str("Labeling")
        else:     
            pbar.set_description_str("Labeling {} ".format(input_video))

        cap.set(cv2.CAP_PROP_POS_FRAMES, start_frame)
        while cap.isOpened():
            pos_frame = int(cap.get(cv2.CAP_PROP_POS_FRAMES))
            ret, frame = cap.read()
            if (not ret) or (pos_frame>end_frame):
                break

            writer.write(frame)
            key = cv2.waitKey(1) & 0xFF
            if key == ord("q"):
                break
            
            pbar.update()

        cv2.destroyAllWindows()
        cap.release()
        writer.release()

    def draw_batch(self, label_files, input_videos, output_path, suffix='_track', is_overwrite=False):
        results = []
        total_videos = len(label_files)
        count=0
        for label_file in label_files:
            count+=1

            base_filename = os.path.splitext(os.path.basename(label_file))[0].replace("_track","")
            raw_video = input_videos[count-1] #os.path.join(input_path, base_filename+".mp4")           

            if output_path:
                if not os.path.exists(output_path):
                    os.mkdir(output_path)

                if suffix:
                    output_video = os.path.join(output_path, base_filename+suffix+".mp4") 
                else:
                    output_video = os.path.join(output_path, base_filename+".mp4")
                

            if not is_overwrite:
                if os.path.exists(output_video):
                    continue 

            self.draw(label_file=label_file, input_video=raw_video, output_video=output_video, video_index=count, video_tot=total_videos)

            results.append(output_video)

        return results
    
    def draw_lines_batch(self, label_files, input_videos, output_path, suffix, is_overwrite=False, is_report=True):
        results = []
        total_videos = len(label_files)
        count=0
        for label_file in label_files:
            count+=1

            base_filename = os.path.splitext(os.path.basename(label_file))[0]
            raw_video = input_videos[count-1]         

            if output_path:
                if not os.path.exists(output_path):
                    os.mkdir(output_path)

                if suffix:
                    output_video = os.path.join(output_path, base_filename+suffix+".mp4")
                else:
                    output_video = os.path.join(output_path, base_filename+".mp4")

            if not is_overwrite:
                if os.path.exists(output_video):
                    if is_report:
                        results.append(output_video)

                    continue 

            self.draw_lines(label_file=label_file, input_video=raw_video, output_video=output_video, video_index=count, video_tot=total_videos)

            results.append(output_video)

        return results
    
    def draw_shapes(self, input_video, output_video, points=None, lines=None, polygons=None, 
                    point_color=None, line_color=None, polygon_color=None, 
                    start_frame=None, end_frame=None, video_index=None, video_tot=None):
        cap = cv2.VideoCapture(input_video)
        if not cap.isOpened():
            raise IOError("Couldn't open webcam or video")

        if start_frame is None:
            start_frame = 0
        if end_frame is None:
            end_frame = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))-1

        tot_frames = end_frame - start_frame + 1       
        fps = int(cap.get(cv2.CAP_PROP_FPS))
        width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        writer = cv2.VideoWriter(output_video, fourcc, fps, (width, height))

        pbar = tqdm(total=tot_frames, unit=" frames")
        if self.compress_message:
            pbar.set_description_str("Labeling")
        else:
            if video_index and video_tot:
                pbar.set_description_str("Labeling {} of {}".format(video_index, video_tot))
            else:     
                pbar.set_description_str("Labeling {} ".format(input_video))

        cap.set(cv2.CAP_PROP_POS_FRAMES, start_frame)
        while cap.isOpened():
            pos_frame = int(cap.get(cv2.CAP_PROP_POS_FRAMES))
            ret, frame = cap.read()
            if (not ret) or (pos_frame>end_frame):
                break
            
            if points is not None:
                if point_color is None:
                    point_color = self.color_bgr
                for point in points:
                    cv2.circle(frame, (point[0], point[1]), radius=self.line_thickness, color=point_color, thickness=-1)

            if lines is not None:
                if line_color is None:
                    line_color = self.color_bgr
                for line in lines:
                    cv2.line(frame, (line[0], line[1]), (line[2], line[3]), line_color, self.line_thickness)
            
            if polygons is not None:
                if polygon_color is None:
                    polygon_color = self.color_bgr
                for polygon in polygons:
                    pts = np.array(polygon, np.int32)
                    pts = pts.reshape((-1, 1, 2))
                    cv2.polylines(frame, [pts], isClosed=True, color=polygon_color, thickness=self.line_thickness)

            writer.write(frame)
            key = cv2.waitKey(1) & 0xFF
            if key == ord("q"):
                break
            
            pbar.update()

        cv2.destroyAllWindows()
        cap.release()
        writer.release()
    
    @staticmethod
    def export_frames(input_video, frames, output_path):
    
        cap = cv2.VideoCapture(input_video)
        if not cap.isOpened():
            raise IOError("Couldn't open webcam or video")

        pbar = tqdm(total=len(frames), unit=" frames")
        pbar.set_description_str("Extracting frame")

        for frame in frames:
            cap.set(cv2.CAP_PROP_POS_FRAMES, frame)
            ret, frame_read = cap.read()

            frame_file = os.path.join(output_path, str(frame)+'.jpg')
            if ret:
                cv2.imwrite(frame_file, frame_read)            
            else:
                break
        
            pbar.update()
    
        pbar.close()
        cap.release()
    
        print("Writing frames to {}".format(output_path))

    @staticmethod
    def time2frame(input_video, time):
        cap = cv2.VideoCapture(input_video)
        if not cap.isOpened():
            raise IOError("Couldn't open webcam or video")

        video_fps = int(cap.get(cv2.CAP_PROP_FPS))                    #original fps
        frame = int(video_fps * time)
        return frame
    
if __name__=='__main__':
    video_file = "/mnt/d/videos/hfst/Standard_SCU7WH_2022-09-16_0630.02.001.mp4"    
    iou_file = "/mnt/d/videos/hfst/Standard_SCU7WH_2022-09-16_0630.02.001_iou.txt"
    track_file = "/mnt/d/videos/hfst/tracks/Standard_SCU7WH_2022-09-16_0630.02.001_track.txt"
    label_video = "/mnt/d/videos/hfst/labels/Standard_SCU7WH_2022-09-16_0630.02.001_track.mp4"
    label_file = "/mnt/d/videos/hfst/tracks/Standard_SCU7WH_2022-09-16_0630.02.001_label.txt"

    labeler = Labeler(video_file, zoom_factor=0.5, nodraw_empty=True, label_fields=[6])
    labeler.draw(label_file, video_file, label_video)

