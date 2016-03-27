#coding=utf-8

import os
import logging
import telegram
import urlparse
from flask import Flask, render_template, request

HOST = "<Host>"
app = Flask(__name__)
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

global bot
bot = telegram.Bot(token = "<Token>")

botName = "@MustangBot"

@app.route("/", methods=["POST", "GET"])
def setWebhook():
    if request.method == "GET":
        logging.info("Hello, Telegram!")
        return "OK, Telegram Bot!"

@app.route("/love", methods=["POST", "GET"])
def love():
    if request.method == "GET":
        return "Long time no see"

@app.route("/set_webhook", methods=['GET'])
def setWebHook():
    s = bot.setWebhook("{}/bot_talk".format(HOST))
    if s:
        return "{} WebHook Setup OK!".format(botName)
    else:
        return "{} WebHook Setup Failed!".format(botName)

@app.route("/bot_talk", methods=["POST"])
def bot_talk():
    if request.method == "POST":
        update = telegram.Update.de_json(request.get_json(force=True))
        if update is None:
            return "Show me your TOKEN please!"
        logging.info("Calling {}".format(update.message))
        handdle_message(update.message)
        return "ok"

def handdle_message(msg):
    text = msg.text
    if "/echo" in text:
      bot.sendMessage(chat_id=msg.chat.id, text="Hello, I am a nerd")
    if "/photo" in text:
        # bot.sendDocument(chat_id=msg.chat.id, document="")
        bot.sendPhoto(chat_id=msg.chat.id, photo="<photo>")
    elif "/help" in text:
        helpInfo(msg)
    else:
        helpInfo(msg)

def helpInfo(msg):
    text ="""
/echo  - echo
/photo - photo
/help  - Help Info

--------------------------
在 c9.io 上跑了个 telegram_bot
"""
    sendTxtMsg(msg, text)

def sendTxtMsg(msg, text):
    bot.sendMessage(chat_id=msg.chat.id, text=text)

def parseCommand(command):
    params = command.split(" ")
    if len(params) == 1:
        return None
    return params[1:]

if __name__ == "__main__":
  app.run(host=os.getenv('IP'),port=int(os.getenv('PORT'))) #

