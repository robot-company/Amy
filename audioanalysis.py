import speech_recognition as sr
import socket
from  arduserial import arduino_port


def internet_on():
    try:
        # connect to the host -- tells us if the host is actually reachable
        socket.create_connection(("www.google.com", 80))
        return True
    except OSError:
        return False


def audio2text():
    r = sr.Recognizer()
    m = sr.Microphone()
    result = ""
    with m as source:
        '''try:
            call_serial(0, 'C')
        except AttributeError:
            print("No Arduino is Installed")'''
        print("Calibrating mic for noise reduction")
        r.adjust_for_ambient_noise(source, duration=2)
        '''try:
            call_serial(0, 'R')
        except AttributeError:
            print("No Arduino is Installed")'''
        print("Speak Now")
        audio = r.listen(source)
        '''try:
            call_serial(0, 'T')
        except AttributeError:
            print("No Arduino is Installed")'''
        try:
            if internet_on() is True:
                value = r.recognize_google(audio)
                # value = r.recognize_google_cloud(audio)
            else:
                value = r.recognize_sphinx(audio)

            if str is bytes:
                result = u"{}".format(value).encode("utf-8")

            else:
                result = "{}".format(value)

        except sr.UnknownValueError:
            print("")
        except sr.RequestError as e:
            print("{0}".format(e))
    # print(result)
    return result
