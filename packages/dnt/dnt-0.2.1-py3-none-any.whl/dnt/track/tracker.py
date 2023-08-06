import os, sys
sys.path.append(os.path.dirname(__file__))

from dsort import track as track_dsort
from sort import track as track_sort

class Tracker:
    def __init__(self, method='sort', max_age=1, min_inits=3, iou_threshold=0.3, gpu = True, deepsort_cfg = 'configs/deep_sort.yaml'):
        self.method = method
        self.max_age = max_age
        self.min_inits = min_inits
        self.iou_threshold=iou_threshold 
        self.gpu = gpu 
        self.deepsort_cfg = deepsort_cfg
    
    def track(self, det_file, out_file, video_file = None, video_index = None, total_videos = None):
        if self.method == 'sort':
            track_sort(det_file, out_file, self.max_age, self.min_inits, self.iou_threshold, video_index, total_videos)
        elif self.method == 'dsort':
            if video_file:
                track_dsort(video_file, det_file, out_file, self.gpu, deepsort_cfg=self.deepsort_cfg, 
                            video_index=video_index, total_videos=total_videos)
            else:
                print('Invalid video file for deep sort tracking!')
        else:
            print('Invalid tracking method!')
    
    def track_batch(self, det_files, video_files, output_path=None, is_overwrite=False, is_report=True):
        results = []
        total_videos = len(det_files)
        count=0
        for det_file in det_files:
            count+=1

            base_filename = os.path.splitext(os.path.basename(det_file))[0].replace("_iou", "")
            if output_path:
                if not os.path.exists(output_path):
                    os.mkdir(output_path)
                track_file = os.path.join(output_path, base_filename+"_track.txt")

            if not is_overwrite:
                if os.path.exists(track_file):
                    if is_report:
                        results.append(track_file)    
                    continue 
            
            video_file = None
            if self.method=="dsort":
                video_file = video_files[count-1]

            self.track(det_file=det_file, out_file=track_file, video_file=video_file, video_index=count, total_videos=total_videos)

            results.append(track_file)

        return results
    
