import PyPDF2
import pyttsx3
from tkinter import *
from tkinter import filedialog

hannah = pyttsx3.init()
hannah.say('Hey there!! I am Hannah. Your personal storyteller. Can we start?? If yes Enter Y....... if no enter N ')
hannah.runAndWait()
permission = input("If you wish to continue enter y....")

if permission.endswith('y'):
    hannah.say('Lets start')
    hannah.runAndWait()
elif permission.endswith('n'):
    hannah.say('I am sorry to see you go...! I will See you later!')    
    hannah.runAndWait()
    
root = Tk()    
pdffile = filedialog.askopenfilename() 
pdfReader = PyPDF2.PdfFileReader(pdffile)
pages = pdfReader.numPages
print(pages)

hannah = pyttsx3.init()
for num in range(1, pages):
    page = pdfReader.getPage(1)
    text = page.extractText()
    hannah.say(text)
    hannah.runAndWait()    
