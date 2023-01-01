import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import wikipedia
import random
from tkinter import *


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        speak('listening')
        print('Listening')
        r.pause_threshold = 0.5
        audio = r.listen(source)
        try:
            print("Recognizing")
            list_speak = ['hmmm I am trying to recognise give me a sec', 'that was confusing, let me try to figure out','you have a great voice nice to hear you']
            speak(random.choice(list_speak))
            Query = r.recognize_google(audio, language='en-in')
            print("command is:", Query)
        except Exception as e:
                print(e)
                speak("Sorry couldn't recognise what you are saying")
                print("Sorry couldn't recognise what you are saying")
                return "None"
        return Query
def speak(audio):
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[0].id)
        engine.say(audio)
        engine.runAndWait()
def Day():
        day = datetime.datetime.today().weekday() + 1
        Day_dict = {1: 'Monday', 2: 'Tuesday',3: 'Wednesday', 4: 'Thursday',5: 'Friday', 6: 'Saturday',7: 'Sunday'}
        if day in Day_dict.keys():
                day_of_the_week = Day_dict[day]
                m_label.config(text=day_of_the_week)
                speak("The day is " + day_of_the_week)
def Time():
    time = str(datetime.datetime.now())
    m_label.config(text=(time[10:]))
    hour = time[11:13]
    min_ = time[14:16]
    speak( "The time is" + hour + "Hours and" + min_ + "Minutes")
def Hi():
     speak("hello I am plexi your desktop assistant Tell me how may I help you")
def wishme():
        hour=datetime.datetime.now().hour
        if hour >= 0 and hour < 12:
            speak("Hello,Good Morning")
            m_label.config(text="Hello,Good Morning")
        elif hour >= 12 and hour < 18:
            speak("Hello,Good Afternoon")
            m_label.config(text="Hello,Good Afternoon")
        else:
            speak("Hello,Good Evening")
            m_label.config(text="Hello,Good Evening")
def Take_query():
    work = True
    while work:
            query = takeCommand().lower()
            x_label.config(text='Command : '+query+'.',font=('helvetica',13))
            if "who are you" in query:
                  speak("I am Your desktop Assistant")
            elif 'what can you do' in query:
                  speak('I can open some websites,tell jokes,provide information and do some minor things for an effortless day.')
            elif "open my college website" in query:
                speak("Opening pesu")
                m_label.config(text='Opening PESU')
                webbrowser.open("www.pesuacademy.com")
            elif "open google" in query:
                speak("Opening Google ")
                m_label.config(text='opening google')
                webbrowser.open("www.google.com")
            elif 'news' in query:
                     news = webbrowser.open_new_tab("https://timesofindia.indiatimes.com/home/headlines")
                     speak('these are some headline from times of India')
            elif "today's date" in query:
                        today=str(datetime.datetime.now())
                        speak(today[0:11])
                        m_label.config(text=today[0:11])
            elif "today is" in query:
                      Day()
            elif "time" in query:
                      Time()
            elif 'tell me a joke' in query:
                    a=["Did you hear about the mathematician who's afraid of negative numbers?He'll stop at nothing to avoid them"," Did you hear about the claustrophobic astronaut?He just needed a little space"]
                    x=random.choice(a)
                    speak(x)
                    m_label.config(text=x)
            
            elif 'hello' in query:
                  wishme()
            elif "from wikipedia" in query:
                    speak("Checking the wikipedia ")
                    query = query.replace("wikipedia", "")
                    result = wikipedia.summary(query, sentences=1)
                    speak("According to wikipedia")
                    speak(result)
                    m_label.config(text='')
            elif 'bye' in query:
                    speak('bye Have a nice day')
                    exit()
            else:
                    m_label.config(text='')
                    work = False
if __name__ == '__main__':
        win = Tk()
        win.title('@PLEXI')
        win.configure(background='black')
        win.geometry('480x520')
        photo =PhotoImage(file=r"C:\Users\ADMIN\Pictures\Screenshots\Screenshot (281).png")
        photo1=photo.subsample(1,1)
        Label(win,text='VIRTUAL ASSISTANT',image=photo1,compound=BOTTOM,bg='black',fg='white',font=25).grid(row=1,column=0,sticky=E)
        askbutton=Button(win,text='ask',width=20,fg="#272324",bg="#A9A9A9",command=Take_query).grid(row=4,column=0)
        x_label=Label(win,text='',fg="#00D1FF",bg='black')
        m_label=Label(win,text='',fg='white',bg='black')
        x_label.grid(row=5,column=0)
        m_label.grid(row=6,column=0)
        Label(win,text='',bg='black').grid(row=7,column=0)
        Button(win,text='exit',command=win.destroy,bg='grey',fg='black').grid(row=8,column=0)
        Label(win,text='@PLEXI created by SPS.',fg='grey',bg='black').grid(row=12,column=0)
        Hi()
        win.mainloop()