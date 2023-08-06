import time


def calculate_fps(start_time, fps_avg_frame_count):
    fps = (fps_avg_frame_count * 2) / (time.time() - start_time)
    return fps
