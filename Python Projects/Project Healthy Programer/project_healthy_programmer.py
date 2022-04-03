#Healthy Programmer
# 9am - 5pm
# Water - water.mp3 (3.5 litres) - Drank - log - Every 40 min
# Eyes - eyes.mp3 - every 30 min - EyDone - log - Every 30 min
# Physical activity - physical.mp3 every - 45 min - ExDone - log
# Rules
# Pygame module to play audio

from pygame import mixer # Mixer is particular function that comes from pygame module.
from datetime import datetime,timedelta
from time impor

def gana(file,stopper):
    mixer.init() # Initiate the song
    mixer.music.load(file) # Choose the song
    mixer.music.set_volume(0.7)  # volume control
    mixer.music.play() # this apply for the play music.
    while True:
        input_of_user = input()
        if input_of_user == stopper:
            mixer.music.stop()
            break
def log_file(msg):
    with open("my_log.txt", "a") as tp:
        tp.write(f"{msg} at {datetime.now()}\n")


nw = datetime.now() # it takes system time.
hrs = nw.hour;mins = nw.minute;secs = nw.second; # It is a convert time in seconds.
zero = timedelta(seconds = secs+mins*60+hrs*3600)
st = nw - zero # this take me to 0 hours.
time1 = st + timedelta(seconds=9*3600) # this gives 9 AM
time2 = st + timedelta(seconds=17*3600)  # this gives 5 PM

if __name__ == '__main__':
    if(nw>= time1 and nw < time2):
            init_water = time()
            init_eyes = time()
            init_exercise = time()
            watersecs =40*60
            exsecs =30*60
            eyessecs =45*60
            print("Your programme is working mode")
            while True:

                if time() - init_water > watersecs:
                    print("Water Drinking time. Enter 'drank' to stop the alarm.")
                    gana('water.mp3', 'drank')
                    init_water = time()
                    log_file("Drank Water at")

                if time() - init_eyes > eyessecs:
                    print("Eye exercise time. Enter 'doneeyes' to stop the alarm.")
                    gana('eyes.mp3', 'doneeyes')
                    init_eyes = time()
                    log_file("Eyes Relaxed at")

                if time() - init_exercise > exsecs:
                    print("Physical Activity Time. Enter 'donephy' to stop the alarm.")
                    gana('physical.mp3', 'donephy')
                    init_exercise = time()
                    log_file("Physical Activity done at")


    else:
        print("Now your system is overed for today.")




