import pyttsx3                          # This module can be installed from "pip install pyttsx3"
import datetime                         # Importing date and time 
import speech_recognition as sr         # To detect our speech download this module using pip
import wikipedia                        # To search on wikipedia download this module and import here
import smtplib                          # To send Email import this module
import webbrowser as wb                 # To search in chrome function
import os                               # To control OS operations
import pyautogui                        # To take screen shot - pip install pyautogui
import psutil                           # To show cpu and battery - pip install psutil
import pyjokes                          # install this moudle using pip to make jokes

engine = pyttsx3.init()                 # Initialize the module
rate = engine.getProperty('rate')       # getting details of current speaking rate
print (rate)                            # printing current voice rate
engine.setProperty('rate', 150)         # setting up new voice rate
volume = engine.getProperty('volume')   # getting to know current volume level (min=0 and max=1)
print (volume)                          # printing current volume level
engine.setProperty('volume',1.0)        # setting up volume level  between 0 and 1


def speak(audio):               # speak function
    engine.say(audio)           # It can say the sentence
    engine.runAndWait()         # this will wait the speak to complete

def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak("The current time is")
    speak(Time)

def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak("The current date is")
    speak(date)
    speak(month)
    speak(year)

def wishme():
    speak("Welcome Back Sir!")
    time()
    date()
    hour  = datetime.datetime.now().hour
    if hour >=6 and hour<12:
        speak("Good Morning Sir!")
    elif hour >=12 and hour<16:
        speak("Good afternoon Sir!")
    elif hour>=16 and hour<24:
        speak("Good Evening Sir!")
    else:
        speak("Good Night Sir!")

    speak("Friday is at your service. please tell me how can I help you sir")


def takeCommand():
    r = sr.Recognizer()
    mic = sr.Microphone()
    with mic as source:
        print("listening..")
        r.pause_threshold = 1
        audio =  r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language='en-in') 
        print(query)

    except Exception as e:
        print(e)
        speak("Say that again Sir!")

        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login('YOUR_MAIL_ID','YOUR_PASSWORD')
    server.sendmail('YOUR_MAIL_ID',to,content)
    server.close()

def screenshot():
    img = pyautogui.screenshot()
    img.save("D:\\My Projects\\Voice Assitant\\Udemy\\ss.png") # create a png file and paste the location here

def cpu():
    usage = str(psutil.cpu_percent())
    speak("CPU is at"+usage)
    battery = psutil.sensors_battery()
    speak("Battery is ")
    speak(battery.percent)

def joke():
    speak(pyjokes.get_joke())

if __name__ == "__main__":
    wishme()
    while True:
        query = takeCommand().lower()

        if 'time' in query:
            time()

        elif 'date' in query:
            date()

        elif 'wikipedia' in query:
            speak("Searching...")
            query = query.replace("wikipedia","")
            result = wikipedia.summary(query, sentences = 2)
            print(result)
            speak(result)

        elif 'send email' in query:
            try:
                speak("What shoud I say?")
                content = takeCommand()
                to = 'TO_MAIL_ID'       #paste your to mail id here.
                sendEmail(to,content)
                speak("Email has been sent sir!")
            except Exception as e:
                print(e)
                speak("Unable to sent the email sir!")

        elif 'search in chrome' in query:
            speak("What should I search Sir ?")
            chromepath = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            search = takeCommand().lower()
            wb.get(chromepath).open_new_tab(search+'.com')

        elif 'logout' in query:
            os.system("shutdown -l")

        elif 'shutdown' in query:
            os.system("shutdown /s /t 1")

        elif 'restart' in query:
            os.system("shutdown /r /t 1")
        
        elif 'play songs' in query:
            songs_dir = 'D:\\Media\\music\\a\\music'   #paste your music directory here.
            songs = os.listdir(songs_dir)
            os.startfile(os.path.join(songs_dir, songs[1]))  #In the list play a particular song

        elif 'remember that' in query:
            speak("What should I remember?")
            data = takeCommand()
            speak("you said to remember that" + data)
            remember = open('data.txt','w')
            remember.write(data)
            remember.close()

        elif 'do you know anything' in query:
            remember = open('data.txt','r')
            speak("you said me to rember that" + remember.read())

        elif 'screenshot' in query:
            screenshot()
            speak("Screenshot has taken successfully")

        elif 'cpu' in query:
            cpu()

        elif 'joke' in query:
            joke()

        elif 'offline' in query:
            quit()
        