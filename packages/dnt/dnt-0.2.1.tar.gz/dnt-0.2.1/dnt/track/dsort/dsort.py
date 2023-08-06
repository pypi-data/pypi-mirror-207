import os
import cv2
import torch
import numpy as np
import pandas as pd
from tqdm import tqdm

from deep_sort import build_tracker
from utils.parser import get_config

def track(video_file, det_file, out_file = None, gpu = True, deepsort_cfg = 'configs/deep_sort.yaml', 
          video_index = None, total_videos = None):

    cwd = os.path.dirname(__file__)
    deepsort_cfg = os.path.join(cwd, deepsort_cfg)

    cfg = get_config()
    cfg.merge_from_file(deepsort_cfg)

    device = torch.device('cuda') if (torch.cuda.is_available() and gpu) else torch.device('cpu')
    cap = cv2.VideoCapture(video_file)
    if not cap.isOpened():
        raise IOError("Couldn't open webcam or video")
        
    deepsort = build_tracker(cfg, use_cuda=gpu)

    detections = pd.read_csv(det_file, header=None).to_numpy()
    start_frame = int(min(detections[:,0]))
    end_frame = int(max(detections[:,0]))
    tot_frames = max((end_frame - start_frame + 1), 0)

    pbar = tqdm(total=tot_frames, desc='Tracking {}'.format(os.path.basename(video_file)), unit = 'frames')
    if video_index and total_videos:
        pbar.desc = 'Tracking {} of {}'.format(video_index, total_videos)

    results = []
    cap.set(cv2.CAP_PROP_POS_FRAMES, start_frame)
    while cap.isOpened():

        pos_frame = int(cap.get(cv2.CAP_PROP_POS_FRAMES))
        ret, frame = cap.read()

        if (not ret) or (pos_frame>end_frame):
            break
        
        im = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame_dets = detections[np.where(detections[:,0] == pos_frame)]
        nrows, ncols = frame_dets.shape

        if nrows > 0:
            bbox_xywh=[]
            for det in frame_dets:
                bbox_xywh.append([det[2]+det[4]/2, det[3]+det[5]/2, det[4], det[5]])
            bbox_xywh = np.array(bbox_xywh)
            conf_score = np.array(frame_dets[:,6])

            outputs = deepsort.update(bbox_xywh, conf_score, im)

            if len(outputs) > 0:
                for output in outputs:
                    results.append([pos_frame, output[4], output[0], output[1], output[2]-output[0], output[3]-output[1], -1, -1, -1, -1])

        pbar.update()

    cap.release()

    if out_file:
        df = pd.DataFrame(results)
        df.to_csv(out_file, index=False, header=None)

if __name__ == "__main__":

    video_file = "/mnt/f/videos/rt_channel/after/56th St & Fowler Ave 0000-2400 SW.mp4"
    mot_file = "/mnt/f/videos/output/clip_mot.txt"
    iou_file = "/mnt/f/videos/output/clip_iou.txt"
    out_file = "/mnt/f/videos/output/clip_track.txt" 

    track(video_file, iou_file, out_file)
    