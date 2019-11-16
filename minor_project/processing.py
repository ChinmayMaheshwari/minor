import parselmouth
from parselmouth.praat import call, run_file

import os
import sys
import speech_recognition as sr


def speechtotext(audio='minor_project/dataset/audioFiles/base.wav'):
	r = sr.Recognizer()
	with sr.AudioFile(audio) as source:
		audio = r.record(source)
		#print ('Done!')
	try:
		text =r.recognize_google(audio)
		return text
	except Exception as e:
		return 0

def pause_count(m='base',p=r"minor_project"):
    sound=p+"/"+"dataset"+"/"+"audioFiles"+"/"+m+".wav"
    sourcerun=p+"/"+"dataset"+"/"+"essen"+"/"+"myspsolution.praat"
    path=p+"/"+"dataset"+"/"+"audioFiles"+"/"
    try:
        objects= run_file(sourcerun, -20, 2, 0.3, "yes",sound,path, 80, 400, 0.01, capture_output=True)
        print (objects[0]) # This will print the info from the sound object, and objects[0] is a parselmouth.Sound object
        z1=str( objects[1]) # This will print the info from the textgrid object, and objects[1] is a parselmouth.Data object with a TextGrid inside
        z2=z1.strip().split()
        z3=int(z2[1]) # will be the integer number 10
        z4=float(z2[3]) # will be the floating point number 8.3
        return z3
    except:
        z3=0
        return "Try again the sound of the audio was not clear"

def word_per_minutes(m='base',p=r"minor_project"):
    sound=p+"/"+"dataset"+"/"+"audioFiles"+"/"+m+".wav"
    sourcerun=p+"/"+"dataset"+"/"+"essen"+"/"+"myspsolution.praat"
    path=p+"/"+"dataset"+"/"+"audioFiles"+"/"
    try:
        objects= run_file(sourcerun, -20, 2, 0.3, "yes",sound,path, 80, 400, 0.01, capture_output=True)
        print (objects[0]) # This will print the info from the sound object, and objects[0] is a parselmouth.Sound object
        z1=str( objects[1]) # This will print the info from the textgrid object, and objects[1] is a parselmouth.Data object with a TextGrid inside
        z2=z1.strip().split()
        z3=int(z2[3]) # will be the integer number 10
        z4=float(z2[3]) # will be the floating point number 8.3
        return z3
    except:
        z3=0
        return "Try again the sound of the audio was not clear"

