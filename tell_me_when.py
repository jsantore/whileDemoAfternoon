import time
import gtts
from playsound import playsound

good_answers = ["yes", "yup", "yeah", "ok"]
said_the_right_thing = False
while not said_the_right_thing:
    answer = input("Can I have candy now?")
    answer = answer.lower()
    if answer in good_answers:
        said_the_right_thing = True

gloat = "Hooray, I can eat candy now!"
language = 'en'
sound_object = gtts.gTTS(text=gloat, lang=language, slow=True)
sound_object.save("gloat.mp3")
for i in range(10):
    playsound("gloat.mp3")
    time.sleep(1)