from doctest import OutputChecker
from urllib import response
import webbrowser
import speech_recognition as sr
import datetime
import wikipedia 
import time
import requests
import subprocess
from ecapture import ecapture as ec
import playsound 
from gtts import gTTS
import os
import wolframalpha
from selenium import webdriver


def talk():
    input=sr.Recognizer()
    with sr.Microphone()as source:
        audio=input.listen(source)
        data=""
        try:
            data=input.recognize_google(audio)
            print ("your question is "+data)
        except sr.UnknownValueError:
            print("sorry i did not here your question,please repeat again.")
        return data



def  respond(output):
     num=0
     print(output)
     num += 1
     response=gTTS(text=output,lang='en')
     file =str(num)+".mp3"
     response.save(file)

     
     os.remove(file)




if __name__=='__main__':
    respond("Hii,i am jarvis your personal voice assistant on this laptop")
    
    while(1):
        respond("how can i help you?")
        text=talk().lower()

        if text==0:
            continue
        if "stop" in str(text)or"exit" in str(text) or "bye"in str(text):
            respond("ok bye and take care master")
            break
        if 'Wikipedia' in text:
            respond('Searching Wikipedia')
            text=text.replace('Wikipedia',"")
            results = wikipedia.summary(text,sentences=3)
            respond("according to wikipedia ")
            print (results)
            respond(results)
        
        elif 'time' in text:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            respond(f"the time is {strTime}")
        elif 'search'in text:
             text = text.replace("search","")
             webbrowser.open_new_tab(text)
             time.sleep(5)
