import speech_recognition as sr
r = sr.Recognizer()
recording = sr.AudioFile('Recording.wav')
with recording as source:
    audio = r.record(source)
r.recognize_google(audio)
