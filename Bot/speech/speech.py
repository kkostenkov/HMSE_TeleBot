import os 
import subprocess

base_path = os.path.split(os.path.split(os.path.realpath(__file__))[0])[0] # Two levels up
resources_path = os.path.join(base_path, "Resources")
print ("Resources are: " + resources_path)

filenames = {
           "welcome" : "welcome_home.mp3",
           }

def say(phrase):
    if (phrase not in filenames):
        print("Unrecognized phrase")
    filename = filenames[phrase]
    file_path = os.path.join(resources_path, filename)
    if os.name == "nt":
        print(file_path)
        return
    else:
        cmd = ["mpg321", file_path] # adjust volume here
        p = subprocess.Popen(cmd, stdout=subprocess.PIPE)
        # Wait for file to be played
        p.wait()
