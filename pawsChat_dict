from nltk.chat.util import Chat

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


class pawsChat():
    def __init__(self):
        self.name=self
    def pawsDict(self,content):
        reply = Chat(pairs, reflections).respond(content)
        return reply
