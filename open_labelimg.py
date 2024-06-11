import os
import subprocess

labelimg_path = "venv/lib/python3.10/site-packages/labelImg/labelImg.py"
image_path = "data/android_figurine/train"
command = f"python {labelimg_path} {image_path}"
subprocess.call(command, shell=True)