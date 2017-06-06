import os
import glob
import subprocess


def get_file_list(my_dir):
    file = my_dir
    files = glob.glob(os.path.join(file, "*.jpg"))
    return files
def create_dir():
    if not os.path.exists("Result"):
        os.makedirs("Result")
def create_files(files):
    create_dir()
    for f in files:
        filename = os.path.basename(f)
        convert_launch = subprocess.run("convert {} -resize 200 {}".format(f, os.path.join("Result", filename)))

create_files(get_file_list("Source"))