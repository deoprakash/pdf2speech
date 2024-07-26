from PyPDF2 import PdfReader
import pyttsx3
import reader

path = open("C:/Users/Deo Prakash/OneDrive/DEO/Deo/imp doc/Deo Prakash Intern offer July 24, 2024.pdf", 'rb')

pdfreader = PdfReader(path)

from_page = pdfreader.pages[10]

text = from_page.extract_text()

speak = pyttsx3.init()
speak.say(text)
speak.runAndWait()
