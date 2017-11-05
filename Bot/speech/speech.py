import os 
import subprocess
import time
from config import mp3_player, wav_player

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
        if file_path.endswith(".mp3"):
            packet = mp3_player
        else:
            packet = wav_player
        cmd = [packet, file_path] # adjust volume here
        p = subprocess.Popen(cmd, stdout=subprocess.PIPE)
        # Wait for file to be played
        p.wait()

def ding():
    say("ding")
    
def greet_with_daypart():
    now = time.time()
    gmtime = time.gmtime()
    h = gmtime.tm_hour
    if (6 <= h < 12):
        say("good_morning")
        return
    if (12 <= h < 18):
        say("good_day")
    if (18 <= h < 24) or (0 <= h < 2):
        say("good_evening")


if __name__ == "__main__":
    say("ding")
    say("good_morning")
    say("good_day")
    say("good_evening")
