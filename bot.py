import telepot
from telepot.loop import MessageLoop
from time import sleep

token="1700309048:AAGBTacX3S5PDx8ywHVYr9oeFPiL0-WI3YU"

bot=telepot.Bot(token)

def handler(msg):
    comm=msg['text']
    chat_id=msg['text','id']
    if(comm=='/start'):
        bot.sendMessage(chat_id,"hello")
    else:
        bot.sendMessage(chat_id,"bye")

MessageLoop(bot,handler).run_as_thread()
while 1:
    sleep(1)