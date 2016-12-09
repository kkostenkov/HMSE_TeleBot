import os
import subprocess
import time

def take_picture():
  if (os.name == "nt"):
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
    # move
    #print("Moving...")
    #os.path.abspath(os.curdir)
    #os.chdir("..")
    #os.chdir("..")
    #new_path = os.path.abspath(os.curdir)
    #print(new_path)
    # /-y 
    #command = "move {} {}".format(new_file_name, new_path)
    #print (command)
    #process = subprocess.Popen(command,
    #                       shell=True, 
    #                       stdout=subprocess.PIPE
    #                       )
    #process.wait()
    file_path = os.path.abspath(os.curdir) + "\\" + new_file_name
    print(file_path)
    return file_path
 

 
if __name__ == "__main__":
  take_picture()