# https://api.telegram.org/bot<token>/getMe

from telegram import Updater
import logging

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

updater = Updater(token='161204461:AAGq03tRaH_fSKx1na3IQk2ZCN-5Mjmb9bE')

dispatcher = updater.dispatcher

def start(bot, update):
  bot.sendMessage(chat_id=update.message.chat_id, text="I'm a bot, please talk to me!")

dispatcher.addTelegramCommandHandler('start', start)

updater.start_polling()

def echo(bot, update):
  bot.sendMessage(chat_id=update.message.chat_id, text=update.message.text)

dispatcher.addTelegramMessageHandler(echo)


def unknown(bot, update):
  bot.sendMessage(chat_id=update.message.chat_id, text="Sorry, I didn't understand that command.")

dispatcher.addUnknownTelegramCommandHandler(unknown)


def caps(bot, update, args):
  text_caps = ' '.join(args).upper()
  bot.sendMessage(chat_id=update.message.chat_id, text=text_caps)

dispatcher.addTelegramCommandHandler('caps', caps)