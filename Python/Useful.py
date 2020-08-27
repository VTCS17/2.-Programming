import random

feet_in_mile = 52080
meters_in_kilometers = 10000
names = ["Samu","Bunny","Savi","Ele","Teddy"]

def get_file_ext(filename):
    return filename[filename.index(".")+1:]

def roll_dice(num):
    return random.randint(1,num)

