# REQUIREMENT: install pyttsx3 module using the following command:
# pip install pyttsx3
import pyttsx3
engine = pyttsx3.init()
engine.say('A python program that change text to voice. Testing...')
engine.runAndWait()          
