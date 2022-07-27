import speech_recognition as sr


class Listener():
    def __init__(self):
        self.listening = True
        self.r = sr.Recognizer()

    def listen(self):
        with sr.Microphone() as source:
            print("I am listening...")
            self.r.adjust_for_ambient_noise(source)
            audio = self.r.listen(source)
        data = ""
        try:
            data = self.r.recognize_google(audio)
            print("You said: " + data)
        except sr.UnknownValueError:
            print("Google Speech Recognition did not understand audio")
        except sr.RequestError as e:
            print("Request Failed; {0}".format(e))
        return data