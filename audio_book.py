# -*- coding: utf-8 -*-
"""
Created on Sun Oct 18 21:42:46 2020

@author: datha
"""
import pyttsx3
import PyPDF2
book = open('D:\Deep Learning\Deep-Learning-with-PyTorch.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages

speaker = pyttsx3.init()
for num in range(31, pages):
    page = pdfReader.getPage(num)
    text = page.extractText()
    speaker.say(text)
    speaker.runAndWait()