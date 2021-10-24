import smtplib
import speech_recognition as sr
import pyttsx3
from email.message import EmailMessage
listener = sr.Recognizer()
engine = pyttsx3.init()


def get_info():
    try:
        with sr.Microphone() as source:
            print("listening...")
            voice = listener.listen(source)
            info = listener.recognize_google(voice)
            print(info)
            return info.lower()
    except:
        pass


def say(text):
    engine.say(text)
    engine.runAndWait()



def send_email(receiver, subject, message):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    #add your email and password
    server.login('','')
    email = EmailMessage()
    email['from'] = ''
    email['to'] = receiver
    email['subject'] = subject
    email.set_content(message)
    server.send_message(email)

#add your contacts name: email of contact
contacts = {'': ''} 


def get_email_info():
    say("who do you want to send the email to")
    name = get_info()
    receiver = contacts[name]
    print(receiver)
    say('what is the subject of the email')
    subject = get_info()
    say('what is the content of the message')
    message = get_info()
    send_email(receiver, subject, message)


get_email_info()

