import speech_recognition as sr
r = sr.Recognizer()
mic = sr.Microphone()
with mic as source:
    audio = r.listen(source)
r.recognize_google(audio, language='hi-IN')
