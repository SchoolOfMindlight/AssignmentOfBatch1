# I am Rafat.
# This is my  regular assignment.
import pyttsx3
TTS = pyttsx3.init()
Mark = input("Enter your mark:")
Mark = int(Mark)
if Mark >= 80:
    TTS.say("Your result is a +",Mark)
elif Mark >= 70:
    TTS.say("Your result is a -",Mark)
elif Mark >= 60:
    TTS.say("Your result is  b",Mark)
elif Mark >= 50:
    TTS.say("Your result is  c",Mark)
else:
    TTS.say("Fail try again",Mark)
TTS.runAndWait()