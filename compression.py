import os
import subprocess
import ffmpeg


ffmpeg_cmd= f'ffmpeg -i {"smart.mp4"} -vf scale=634:356 {"smart_out.mp4"}'
subprocess.run(ffmpeg_cmd, shell=True)