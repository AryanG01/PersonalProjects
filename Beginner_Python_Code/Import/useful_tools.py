import random

feet_in_mile = 5280
m_in_km = 1000

def get_file_exten(filename):
    return filename[filename.index(".") + 1:]

def roll_dice(num):
    return random.randint(1, num)