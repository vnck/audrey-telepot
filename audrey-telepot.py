import telepot
from telepot.loop import MessageLoop
import time

from firebase import firebase

from nltk.chat.util import Chat
import urllib.parse
import requests
import json
from random import*
from string import punctuation

bot = telepot.Bot('TELEGRAM KEY HERE')

url = "FIREBASE URL HERE"
token = "FIREBASE TOKEN HERE"

firebase = firebase.FirebaseApplication(url, token)

is_chatting = False
reflections = {
    "am"     : "r",
    "was"    : "were",
    "i"      : "u",
    "i'd"    : "u'd",
    "i've"   : "u'v",
    "ive"    : "u'v",
    "i'll"   : "u'll",
    "my"     : "ur",
    "are"    : "am",
    "you're" : "im",
    "you've" : "ive",
    "you'll" : "i'll",
    "your"   : "my",
    "yours"  : "mine",
    "you"    : "me",
    "u"      : "me",
    "ur"     : "my",
    "urs"    : "mine",
    "me"     : "u"
}
# Note: %1/2/etc are used without spaces prior as the chat bot seems
# to add a superfluous space when matching.

pairs = (
    (r'(im|i\'m|I\'m) (.*)',
    ( "ur %2?? cool sial! You my father is it?",
      "Hi %2!! So...what you want talk?")),

    (r'(.*) don\'t you (.*)',
    ( "u think I steady can %2??! serious?? aiya i paiseh liao",
      "%2??! Crazy ah",
      "u think i tak boleh? wait i become a real plant then i show u")),

    (r'ye[as] [iI] (.*)',
    ( "u%1? teach me senpai!?",
      "how come u %1??",
      "u think u special ah, i also can")),

    (r'do (you|u) (.*)\??',
    ( "abuden...",
      "i dunno. u tell me lah")),

    (r'(.*)\?',
    ( "questions questions questions... im only a plant leh, i know u got brain but i don't. So pls no give questions anymore k?",
      "got ask Google yet?",
      "what that")),

    (r'(cos|because) (.*)',
    ( "excuses only sia u",
      "pls explain simpler so i can understand",
      "oo i see i see!")),

    (r'why can\'t [iI] (.*)',
    ( "got try off and on?",
      "u can do it as long as u think u can!",
      "i dunno! but when i cannot %1 i ask prof yan guang!",
      "ehh don't change topic...")),

    (r'I can\'t (.*)',
    ( "u can't %1",
      "bopian lor, just cri only",
      "lel u cannot",
      "then let's do something else")),

    (r'(.*) (like|love|watch) anime',
    ( "omg i love anime!! do u like sailor moon??! ^&^",
      "anime yay! anime rocks sooooo much!",
      "oooh anime! i love anime more than anything!",
      "anime is the bestest evar! evangelion is the best!",
      "hee anime is the best! do you have ur fav??")),

    (r'I (like|love|watch|play) (.*)',
    ( "cool! %2 rocks!",
      "power lah! i same same with you!",
      "me 2! what else u like?")),

    (r'anime sucks|(.*) (hate|detest) anime',
    ( "ur a liar! i'm not gonna talk to u nemore if u h8 anime *;*",
      "no way! anime is the best ever!",
      "nuh-uh, anime is the best!")),

    (r'(are|r) (you|u) (.*)',
    ( "am i %1??! how come u ask that!",
      "maybe!  y shud i tell u?? ")),
    
    (r'What is (.*)',
    ("Hope u like this dose of random news my friend!",
     "Was that what u searching for?",
     "Yo check out what i found man!",
     "You won't believe what happens next...")),

    (r'what (.*)',
    ( "hee u think im gonna tell u? .v.",
      "booooooooring! ask me somethin else!")),

    (r'how (.*)',#
    ( "got ask prof yanguang anot")),

    (r'(hi|hello|hey) (.*)',#
    ( "hello! u good?")),

    (r'quit',
    ( "ma tell me stop talking to you now need study bio now. bb!",
      "bye bye! tanks 4 keeping me company!",
      "bye! next time we go jalan jalan ok?")),

    (r'(.*)',
    ( "u joker sia lelelel.",
      "boooooring! talk something else! tell me wat u like!",
      "u like anime??",
      "let's change topic. y u join SUTD?",
      "i have no eyes...what does having eyes feels like?",
      "this should be a conversation for another day yo...",
      "how is it even possible that we chatting to each other...",
      "u know that u talking to plant rite?",
      "i no brain can talk simpler?",
      "u want to hear a joke?")),
    
    (r'(yes|yas|Yes|Yas|YAS)',#
    ( "Mr. Mushroom could never understand why he wasn't looked on as a real fun guy.",
      "If we canteloup lettuce marry!",
      "The tree that was creating energy was turned into a power-plant.",
      "What kind of tree grows on your hand? A palm tree.",
      "After a cold winter, will deciduous trees be releaved?",
      "In some conifer forests, you can't cedar wood for the trees."))
    )

bean_chatbot = Chat(pairs, reflections)

def returnHello(chat_id,content):
	bot.sendMessage(chat_id, 'Hi! I\'m Audrey the plant! 🌱')

def activateGreenThumb(chat_id,content):
	gtMode = firebase.get('/greenthumbMode')
	if gtMode == True:
		bot.sendMessage(chat_id, 'I am already in Green Thumb Mode!')
	else:
		firebase.put('/','greenthumbMode', True)
		bot.sendMessage(chat_id, 'Green Thumb Mode Activated!')

def activateAutoMode(chat_id,content):
	gtMode = firebase.get('/greenthumbMode')
	if gtMode == True:
		firebase.put('/','greenthumbMode', False)
		bot.sendMessage(chat_id, 'Activating Auto Mode!')
	else:
		bot.sendMessage(chat_id, 'I am already in Auto Mode!')

def temperature(chat_id,content):
	temp = firebase.get(temperature)
	ans = 'It\'s ' + str(temp[1]) + ' degrees.'
	bot.sendMessage(chat_id, ans)

def returnHelp(chat_id,content):
	ans = 'Hi! I\'m Audrey the plant! 🌱\n\nHere are some of the things I can do!\n/greenthumb - Activate Green Thumb Mode\n/auto - Activate Auto Watering Mode\n/temperature - Get the temperature\n/hello - Chat with me!\n\nI am a project made for 10.009 1D Project by Abi, Benedict, Ivan, Wesson, Yu Lian.'
	bot.sendMessage(chat_id, ans)

def chatBot(chat_id,content):#
        global is_chatting
        if not is_chatting:
                is_chatting = True
                bot.sendMessage(chat_id, 'Hi I\'m Audrey. Who are You?')
        elif "What is" in content:
                strip_punctuation=''.join(c for c in content if c not in punctuation)
                q=strip_punctuation[8:]
                main_api = 'https://newsapi.org/v2/top-headlines?'+urllib.parse.urlencode({'q': q})+'&apiKey=77e4bb173d4143e18b5736660a93de14'
                data = requests.get(main_api).json()
                ls=[]
                for i in data['articles']:
                        ls.append(i['title']+'\n'+i['description']+'\n'+i['url'])
                if len(ls)==0:
                        bot.sendMessage(chat_id, 'paiseh i cannot find it in my newspaper...')
                else:
                        bot.sendMessage(chat_id, ls[randint(0,len(ls)-1)])
                        bot.sendMessage(chat_id, bean_chatbot.respond(content))
        else:
                bot.sendMessage(chat_id, bean_chatbot.respond(content))	
	
command = {
	"/greenthumb": activateGreenThumb,
	"/auto": activateAutoMode,
	"/start": returnHello,
	"/temperature": temperature,
	"/help": returnHelp,
	"help": returnHelp,
	"/hello": chatBot
}


def handle(msg):
	content_type, chat_type, chat_id = telepot.glance(msg)
	content = msg['text']

	if content_type == 'text':

		if content in command.keys():
			command[content](chat_id,content)
			
		elif is_chatting:
			chatBot(chat_id, content)

		if content[0] != '/': #is this to test if the chat is working?
			bot.sendMessage(chat_id, '🌱')


MessageLoop(bot, handle).run_as_thread()
print('Audrey is listening...')

while 1:
	time.sleep(10)
