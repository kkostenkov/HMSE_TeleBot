import os 
import subprocess

base_path = os.path.split(os.path.split(os.path.realpath(__file__))[0])[0] # Two levels up
resources_path = os.path.join(base_path, "Resources")
print ("Resources are: " + resources_path)

filenames = {
           "cold" : "cold.wav",
           "ding" : "ding.mp3",
           "frost" : "frost.wav",
           "good_day" : "good_day.wav",
           "good_evening" : "good_evening.wav",
           "good_morning" : "good_morning.wav",
           "have_a_good_day" : "have_a_good_day.wav",
           "kirill" : "kirill.wav",
           "outdoors" : "outdoors.wav",
           "vika" : "vika.wav",
           "welcome" : "welcome.wav",
           "welcome_home" : "welcome_home.mp3",
           #"" : ".wav",
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

def ding():
    say("ding")