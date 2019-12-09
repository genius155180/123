from telegram.ext import Updater, CommandHandler, MessageHandler, Filters    
import logging
import stngs

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
level=logging.INFO,
filename='bot.log'
)

def qwe(bot, update):
    text = ("Вызван /start")
    print(text)
    update.message.reply_text(text)

def talk_to_me(bot, update):
    user_text = update.message.text
    logging.info("User: %s, Chat id: %s, Message: %s", update.message.chat.username, update.message.chat.id, update.message.text)
    update.message.reply_text(user_text)
 
 
def ewq():
    mybot=Updater(stngs.key)
    logging.info("BOT")
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", qwe))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    mybot.start_polling()
    mybot.idle()
ewq()
