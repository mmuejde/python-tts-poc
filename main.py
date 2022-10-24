import json

from gtts import gTTS

voices = []

with open("text.json", "r") as file:
    data = json.load(file)
    for i in data:
        tts_en = gTTS(i['en'], lang='en')
        tts_de = gTTS(i['de'], lang='de')

FILE_NAME = 'text.mp3'


with open(FILE_NAME, 'wb') as f:
    tts_en.write_to_fp(f)
    tts_de.write_to_fp(f)
