import pyttsx3
txt=input('chi begam ?: ')
sound=pyttsx3.init()
sound.setProperty('rate',110)
sound.say(txt)
sound.runAndWait()