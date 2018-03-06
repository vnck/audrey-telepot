import telepot
from telepot.loop import MessageLoop
import time

from firebase import firebase

bot = telepot.Bot('TELEGRAM KEY HERE')

url = "FIREBASE URL HERE"
token = "FIREBASE TOKEN HERE"

firebase = firebase.FirebaseApplication(url, token)

def returnHello(chat_id):
	bot.sendMessage(chat_id, 'Hi! I\'m Audrey the plant! 🌱')

def activateGreenThumb(chat_id):
	gtMode = firebase.get('/greenthumbMode')
	if gtMode == True:
		bot.sendMessage(chat_id, 'I am already in Green Thumb Mode!')
	else:
		firebase.put('/','greenthumbMode', True)
		bot.sendMessage(chat_id, 'Green Thumb Mode Activated!')

def activateAutoMode(chat_id):
	gtMode = firebase.get('/greenthumbMode')
	if gtMode == True:
		firebase.put('/','greenthumbMode', False)
		bot.sendMessage(chat_id, 'Activating Auto Mode!')
	else:
		bot.sendMessage(chat_id, 'I am already in Auto Mode!')

def temperature(chat_id):
	temp = firebase.get(temperature)
	ans = 'It\'s ' + str(temp[1]) + ' degrees.'
	bot.sendMessage(chat_id, ans)

def returnHelp(chat_id):
	ans = 'Hi! I\'m Audrey the plant! 🌱\n\nHere are some of the things I can do!\n/greenthumb - Activate Green Thumb Mode\n/auto - Activate Auto Watering Mode\n/temperature - Get the temperature\n\nI am a project made for 10.009 1D Project by Abi, Benedict, Ivan, Wesson, Yu Lian.'
	bot.sendMessage(chat_id, ans)

command = {
	"/greenthumb": activateGreenThumb,
	"/auto": activateAutoMode,
	"/start": returnHello,
	"/temperature": temperature,
	"/help": returnHelp,
	"help": returnHelp,
}


def handle(msg):
	content_type, chat_type, chat_id = telepot.glance(msg)
	content = msg['text']

	if content_type == 'text':

		if content in command.keys():
			command[content](chat_id)

		if content[0] != '/':
			bot.sendMessage(chat_id, '🌱')


MessageLoop(bot, handle).run_as_thread()
print('Audrey is listening...')

while 1:
	time.sleep(10)
