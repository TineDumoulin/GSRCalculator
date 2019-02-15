# pip install SpeechRecognition

import operator
import speech_recognition as sr

ops = { "+": operator.add, "-": operator.sub, "x": operator.mul, 'divided': operator.truediv, '/': operator.truediv, 'by': operator.truediv}

# obtain audio
r = sr.Recognizer()
with sr.Microphone() as source:
    print("What should I calculate?")
    audio = r.listen(source)
    
# recognize speech + cast into usable list
audio = (r.recognize_google(audio, language = "en_US")).lower().split(' ')
print(audio)

#assign numbers + execute operation
try:
    audio_a, audio_b = float(audio[0]), float(audio[2])
    result = ops[audio[1]](audio_a,audio_b)
    print(result)

except:
    print('This is probably my fault...')