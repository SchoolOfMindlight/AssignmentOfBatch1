import pyttsx3
zara = pyttsx3.init()
text = input("enter any text...")
zara.say(text)
zara.runAndWait()