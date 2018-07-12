# -*- coding: utf-8 -*-
from skpy import Skype, SkypeEventLoop, SkypeNewMessageEvent
import requests
from pprint import pprint
import jsonpickle, json
import logging
from logging.handlers import RotatingFileHandler
import re


def remove_html_tags(text):
    """Remove html tags from a string"""
    clean = re.compile('<.*?>')
    return re.sub(clean, '', text)


handler = RotatingFileHandler('skype_incoming.log', maxBytes=20000, backupCount=3)
handler.setLevel(logging.INFO)
logger = logging.getLogger("main")
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.setLevel(logging.INFO)

logger.addHandler(handler)




clusterChat='YOUR_CHAT_GROUP_ID_HERE'
skypeLogin="LOGIN_HERE"
skypePass="PASS_HERE"
slackUrl='WEBHOOK_URL_IN_SLAK_HERE'
telegramBotToken= 'YOUR_BOT_TOKEN'
telegramUrl = 'https://api.telegram.org/bot'+telegramBotToken+'/sendMessage'
telegramChatId='YOUR_CHAT_ID'
mode="Slack" #change to "Telegram" to make Skype to Telegram integration

#код ниже слушает события скайпа и если пришло сообщение в нужную группу, то отправляет в слак текст сообщения
class SkypePing(SkypeEventLoop):
    def __init__(self):
        super(SkypePing, self).__init__(skypeLogin,  skypePass)
    def onEvent(self, event):


        if isinstance(event, SkypeNewMessageEvent) and not event.msg.userId == self.userId:
            #print event.msg.chatId #uncomment to get chatId

            logger.info("Msg from chatId = " + event.msg.chatId)
            if event.msg.chatId==clusterChat:
         
            #print event.msg.raw["imdisplayname"]+' via Skype: '+event.msg.content
                msgstr = '*' +remove_html_tags(event.msg.raw["imdisplayname"].encode('utf-8'))+' via Skype* '+remove_html_tags(event.msg.content.encode('utf-8'))
                if mode=="Slack":
                    r = requests.post(slackUrl,data='{ "text": "'+ msgstr +  '" }')
                    logger.info(msgstr + '#slack resp: ' + r.content)
                if mode=="Telegram":
                    r = requests.post(telegramUrl,data='{"text":"'+msgstr+ '", "chat_id":"'+telegramChatId+'", "parse_mode":"Markdown"}')
                    logger.info(msgstr + '#slack resp: ' + r.content)


lp= SkypePing();
lp.loop();


