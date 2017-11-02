import threading
import time
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import subprocess

cnt = 0

def start(bot, update):
    update.message.reply_text('Hola, para usar el bot da el comando /test')


def test(bot, update):
    start = time.time()
    global cnt
    # ping a google
    address = "74.125.196.104"
    if cnt <= 4:
        res = subprocess.call(['ping', '-c', '1', address])
        if res == 0:
            end = time.time()
            update.message.reply_text("PING " + address + " time= {:0.3f}".format(end - start) + " ok")
        elif res == 2:
            end = time.time()
            update.message.reply_text("PING " + address + " time= {:0.3f}".format(end - start) + " bad")
        else:
            end = time.time()
            update.message.reply_text("PING " + address + " time= {:0.3f}".format(end - start) + " wrong")
        cnt += 1
        test(bot, update)
    else:
        cnt = 0


updater = Updater('token')
updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('test', test))

updater.start_polling()
updater.idle()
