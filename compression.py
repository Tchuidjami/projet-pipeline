import os
import subprocess
import ffmpeg


ffmpeg_cmd= f'ffmpeg -i {"test.mp4"} -vf scale=634:356 {"test_compress.mp4"}'
subprocess.run(ffmpeg_cmd, shell=True)
