import telepot
from telepot.loop import MessageLoop
import time

from firebase import firebase

from pawsChat_dict import *
import urllib.parse#
import requests#
import json#
from random import*#
from string import punctuation#

bot = telepot.Bot('insert-telegram-bot-token-here')

url = "insert-firebase-url-token-here" # URL to Firebase database
token = "insert-firebase-authentication-token-here" # unique token used for authentication

firebase = firebase.FirebaseApplication(url, token)

is_chatting = False

bean_chatbot = pawsChat()#

def returnHello(chat_id):#
	bot.sendMessage(chat_id, 'Hi! I\'m Audrey the plant! ')

def activateGreenThumb(chat_id):#
	gtMode = firebase.get('/greenthumbMode')
	if gtMode == True:
		bot.sendMessage(chat_id, 'I am already in Green Thumb Mode!')
	else:
		firebase.put('/','greenthumbMode', True)
		bot.sendMessage(chat_id, 'Green Thumb Mode Activated!')

def activateAutoMode(chat_id):#
	gtMode = firebase.get('/greenthumbMode')
	if gtMode == True:
		firebase.put('/','greenthumbMode', False)
		bot.sendMessage(chat_id, 'Activating Auto Mode!')
	else:
		bot.sendMessage(chat_id, 'I am already in Auto Mode!')

def temperature(chat_id):#
	temp = firebase.get(temperature)
	ans = 'It\'s ' + str(temp[1]) + ' degrees.'
	bot.sendMessage(chat_id, ans)

def returnHelp(chat_id):#
	ans = 'Hi! I\'m Audrey the plant!🌱\n\nHere are some of the things I can do!\n/greenthumb - Activate Green Thumb Mode\n/auto - Activate Auto Watering Mode\n/temperature - Get the temperature\n\nI am a project made for 10.009 1D Project by Abi, Benedict, Ivan, Wesson, Yu Lian.'
	bot.sendMessage(chat_id, ans)

def chatBot(chat_id,content):#
	global is_chatting
	if not is_chatting:
		is_chatting = True
		bot.sendMessage(chat_id, 'Hi I\'m Audrey. Who are You?')
	elif "Any news" in content:
		strip_punctuation=''.join(c for c in content if c not in punctuation)
		q=strip_punctuation[9:]
		main_api = 'https://newsapi.org/v2/top-headlines?'+urllib.parse.urlencode({'q': q})+'&apiKey=77e4bb173d4143e18b5736660a93de14'
		data = requests.get(main_api).json()
		ls=[]
		for i in data['articles']:
			ls.append(i['title']+'\n'+i['description']+'\n'+i['url'])
		if len(ls)==0:
			bot.sendMessage(chat_id, 'paiseh i cannot find it in my newspaper...')
		else:
			bot.sendMessage(chat_id, ls[randint(0,len(ls)-1)])
			bot.sendMessage(chat_id, bean_chatbot.pawsDict(content))
	else:
		bot.sendMessage(chat_id, bean_chatbot.pawsDict(content))
		print(content)
command = {
	"/greenthumb": activateGreenThumb,
	"/auto": activateAutoMode,
	"/start": returnHello,
	"/temperature": temperature,
	"/help": returnHelp,
	"/chat": chatBot#
}


def handle(msg):
	content_type, chat_type, chat_id = telepot.glance(msg)
	content = msg['text']

	if content_type == 'text':
                
		if content == "/chat":
			chatBot(chat_id, content=None)
			
		elif content in command.keys(): #
			command[content](chat_id)#

		elif is_chatting:
			chatBot(chat_id,content)
			
		elif content[0] != '/': #is this to test if the chat is working?
			bot.sendMessage(chat_id, '🌱')


MessageLoop(bot, handle).run_as_thread()
print('Audrey is listening...')

while 1:
	time.sleep(10)

