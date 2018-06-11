# -*- coding: utf-8 -*-
from skpy import Skype, SkypeEventLoop, SkypeNewMessageEvent
import requests
from pprint import pprint
import jsonpickle, json
import logging
from logging.handlers import RotatingFileHandler
from flask import Flask, request, redirect, url_for, jsonify
import re



jsonpickle.set_preferred_backend('json')
jsonpickle.set_encoder_options('json', ensure_ascii=False);



app = Flask(__name__)


clusterChat='YOUR_CHAT_GROUP_ID_HERE'
skypeLogin="LOGIN_HERE"
skypePass="PASS_HERE"
slackGetUserUrl='https://slack.com/api/users.info'
slackToken='SLACK_TOCKEN_HERE'

#это оформляем отдельным прилодением, которое вызывается по событию из слака. учесть что подключения надо кешировать


def remove_html_tags(text):
    """Remove html tags from a string"""
    clean = re.compile('<.*?>')
    return re.sub(clean, '', text)


#you can setup this route in Slack but we strongly  recommend to use Corezoid instead
@app.route('/listen/skype', methods=['GET', 'POST'])
def listen_skype():
     if request.method == 'POST'
        app.logger.info('/listen request:'+ "".join( request.data.splitlines()))
        _json =  request.get_json(force=True)

        if "challenge" in _json:
            return _json["challenge"]



        if _json["event"]["type"] == "message":
            if not 'sybtype' in  _json["event"]:
                r = requests.post(corezoidUrl,data=request.data)
                app.logger.info('/corezoid answer:' + "".join(r.content.splitlines()))
                return '{"OK":true}'

        return '{"OK":true}'

#API call to send Skype message, do login and sends message, uncomment print statesments to debug
@app.route('/listen/send_skype', methods=['GET', 'POST'])
def send_skype():
    if request.method == 'POST':
        app.logger.info('/send request:' + "".join(request.data.splitlines()))
        _json = request.get_json(force=True)

        if _json["event"]["type"] == "message":
            if not 'subtype' in _json["event"]:
                if _json["production"]:
                    clusterChat=clusterChat_prod

                sk = Skype(skypeLogin, skypePass, 'session.tmp')  # connect to Skype
                chats = sk.chats  # your conversations
                ch = chats.chat(clusterChat)

                r = requests.get(slackGetUserUrl, params={"token": slackToken, "user": _json["event"]["user"]})
                # print r.content
                _user = jsonpickle.decode(r.content)
                # ch.sendMsg( _user["user"]["real_name"] + ' via Slack: ' + _json["event"]["text"]) # plain-text message
                ch.sendRaw(messagetype="RichText", contenttype="text",
                           content='<b>' + _user["user"]["real_name"] + ' via Slack: </b>' + remove_html_tags(_json["event"][
                               "text"]))  # plain-text message
                app.logger.info(_user["user"]["real_name"] + ' via Slack: ' + remove_html_tags(_json["event"]["text"]))
                return '{"OK":true}'

        return '{"OK":true}'


handler = RotatingFileHandler('skype_outgoing.log', maxBytes=20000, backupCount=3)
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
app.logger.addHandler(handler)
app.logger.setLevel(logging.INFO)



