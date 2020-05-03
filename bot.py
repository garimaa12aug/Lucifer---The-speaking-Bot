import os
import tkinter as tk
from tkinter import *
import parser
import tkinter.messagebox
import random
import requests
import json
from actions.define_subject import define_subject
from actions.tell_joke import tell_joke
from actions.news import business_news, agriculture_news, finance_news,  political_news, world_news

def speak(text):
        os.system('espeak "{}"'.format(text) )

def clicked():
        text = entry.get()
        speak(text)

def default(text):
	 messages = ['are you angry',
                'dont be sad talk to me',
                'what do you want',
		'I dont know what does that mean']
	 return (random.choice(messages))	


def who_are_you(text):
    messages = ['I am Lucifer ! your own personal assistant.',
                'Lucifer! didnt I tell you before?',
                'You asked that so many times! I am Lucifer']
    return (random.choice(messages))

def love_you(text):
    replies = [
               'I love you too.',
               'You are looking for love in the wrong place.'
              ]
    return (random.choice(replies))

def toss_coin(text):
    outcomes = ['heads', 'tails']
    return ('I just flipped a coin. It shows ' + random.choice(outcomes))

def how_am_i(text):
    replies = [
        'You are the coolest person ! I have ever seen !',
        'My knees ! go weak when I see you.',
        'You look like ! the kindest person I have met.',
	'are you angry',
	'dont be ! sad talk to me'
	
    ]
    return (random.choice(replies))

def born(text):
    return ('I was created by a person named ! Garima ! in India')

def marry_me(text):
    return ('I have been receiving a lot of marriage proposals recently.')


def are_you_up():
    return ('For you , always.')

def bot():
	message = entry.get()
	if message == "quit":
        	exit()
	elif message == "hello":
        	answer = "Hi"
	elif message == "hi":
        	answer = "Hello"
	elif message == "who are you":
		answer = who_are_you(message)
	elif message == "who created you" :
		answer = born(message)
	elif message == "do you love me" or "love you" :
		answer = love_you(message)
	elif message == "marry me":
		answer = marry_me(message)
	elif message == "finance news":
		answer = finance_news(message)
	elif message == "business news":
		answer = business_news(message)
	elif message == "political news":
		answer = political_news(message)
	elif message == "world news":
		answer = world_news(message)
	elif message == "tell a joke":
		answer = tell_joke(message)
	elif message == "how am i" or "what do you think about me":
		answer = how_am_i(message)
	else :
		answer = default(message)
	
	speak(answer)

root = tk.Tk()
root.title("Text to Speech")
root.resizable(width=False, height=False)
root.geometry("1200x700+0+0")
label1 = tk.Label(root, text='What do you want me to speak?',bg="blue", font=('Helvetica',20,'bold'))
label1.pack()
entry = tk.Entry(root)
entry.pack()
button = tk.Button(root, text='Speak this line!', command=clicked)
button.pack()
button = tk.Button(root,text ='talk to me',command = bot)
button.pack()
photo = PhotoImage(file = "robo.gif")
w = Label(root, image=photo)
w.pack(fill=BOTH, expand=YES)

root.mainloop()


