import os
import subprocess
import time

def take_picture_nix():
    pic_path = "/home/kkostenkov/Pictures/webcam.jpeg"
    command = "fswebcam"
    resolution = "-r 640*480"
    delay = "-D0.1"
    skip_frames = "-S1"
    title = "Koss home"
    # exec command
    process = subprocess.call([command, 
                               delay, 
                               skip_frames, 
                               resolution,
                               title,
                               pic_path
                               ])
    #process.wait()
    return pic_path

def take_picture_win():
    # take pic
    print("Taking pic")
    command = "snapz.exe"
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
    process.wait()
    # rename
    time_mark = str(int(time.time()))
    new_file_name = time_mark + ".png"
    print(new_file_name)
    
    command = "ren snapz.dib {}".format(new_file_name)
    print (command)
    process = subprocess.Popen(command ,
                           shell=True, 
                           stdout=subprocess.PIPE
                           )
    process.wait()
    file_path = os.path.abspath(os.curdir) + "\\" + new_file_name
    print(file_path)
    return file_path
 

def take_picture():
    if (os.name == "nt"):
        return take_picture_win()
    else:
        return take_picture_nix()
    
 
if __name__ == "__main__":
  take_picture()
