from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import speech_recognition as sr 
import os
import pyttsx3
from datetime import datetime
   
def speak(str):
    engine=pyttsx3.init()
    engine.setProperty('voice',"HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0")
    engine.say(str)
    engine.runAndWait()
def wish():
    hour=datetime.now().hour
    if hour>=3 and hour<=12:
        speak("very good morning sir!!!")
    elif hour>=17 or hour<3:
        speak("very good evening sir!!!")
    elif hour>12 and hour<17:
        speak("very good afternoon sir!!!")

def audiorecoder():
    r2=sr.Recognizer()
    r3=sr.Recognizer()
    with sr.Microphone() as source :
        print("Listening...")
        audio = r3.listen(source)
    try: 
        text = r2.recognize_google(audio) 
        print ("you said: " + text )
    except sr.UnknownValueError: 
        print("Google Speech Recognition could not understand audio") 

    except sr.RequestError as e: 
        print("Could not request results from Google Speech Recognition service; {0}".format(e)) 

    return text
def helpbyus():
    dictans={}
    speak("let's start...")
    speak("please tell your first name")
    dictans["firstname"]=audiorecoder().upper()
    speak("please tell your last name")
    dictans["lastname"]=audiorecoder().upper()
    speak("ok.. I save ur name as" +dictans["firstname"]+dictans["lastname"])
    speak("please tell how old are you")
    dictans["age"]=int(audiorecoder())
    speak("can I know your sex")
    dictans["gender"]=audiorecoder()
    speak("ok.. let's say ur email id ")
    a=True
    while a:
        email=audiorecoder()
        if "@" in s:
            dictans["email"]=email.lower()
            a=False
        else:
            speak("please tell a valid email-id")
    speak("ok.. then tell your contact number")
    number=audiorecoder()
    number=int(number.replace(" ",""))
    b=True
    while b:
        number=audiorecoder()
        number=int(number.replace(" ",""))
        if len(number)==10:
            dictans["number"]=number
            b=False
        else:
            speak("please tell a valid number")
    speak("ok..choose your qualificattion")
    c=True
    while c:
        speak("for under matriculation say one. for matriculation say two. for under graduate say three. for graduate say four")
        ans=audiorecoder()
        if int(ans)==1:
            dictans["qualification"]="under-matriculation"
            c=False
        elif int(ans)==2:
            dictans["qualification"]="matriculation"
            c=False
        elif int(ans)==3:
            dictans["qualification"]="under-graduate"
            c=False
        elif int(ans)==4:
            dictans["qualification"]="graduate"
            c=False
        else:
            speak("please say a valid number")
    speak("ok.. survey is complete can i submit it")
    speak("please say submit for Submit it")
    ans=audiorecoder()
    if ans=="submit":
        dictans["submission"]="submit"
    else:
        speak("i think u don't want to submit")
        speak("for simplicity i save this information")

    speak("THANK u for you are giving time for  us") 
    
    return dictans
def submitform(dic):
    driver = webdriver.Chrome(executable_path="C:/Users/gyane/Downloads/chromedriver_win32 (1)/chromedriver.exe")
    driver.get("file:///C:/Users/gyane/OneDrive/Desktop/project2/file.html")
    driver.find_element_by_name('Firstname').send_keys(dic["firstname"])
    driver.find_element_by_name('lastname').send_keys(dic["lastname"])
    driver.find_element_by_name('Age').send_keys(dic["age"])
    driver.find_element_by_name('Gender').send_keys(dic["gender"])
    driver.find_element_by_name('email').send_keys(dic["email"])
    driver.find_element_by_name('phno').send_keys(dic["number"])
    if dic["Qualification"]==1:
        driver.find_element_by_id('um').click()
    elif dic["Qualification"]==2:
        driver.find_element_by_id('m').click()
    elif dic["Qualification"]==3:
        driver.find_element_by_id('g').click()
    else:
        driver.find_element_by_id('ug').click()
    driver.find_element_by_id('submit').click()
    
if __name__=="__main__":
    wish()
    speak("Sir we want to fill a form by You. If u fill it by manual speak manual  or speak help for help by us")
    ans=audiorecoder()
    if ans=="manual":
        driver = webdriver.Chrome(executable_path="C:/Users/gyane/Downloads/chromedriver_win32 (1)/chromedriver.exe")
        driver.get("file:///C:/Users/gyane/OneDrive/Desktop/project2/file.html")
    elif ans=="help":
        dic=helpbyus()
    submitform(dic)