import time


def calculate_fps(start_time, fps_avg_frame_count):
    fps = (fps_avg_frame_count * 5.5) / (time.time() - start_time)
    return fps
