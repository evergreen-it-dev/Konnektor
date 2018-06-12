# Konnektor
Konnektor Helps Connect Chatrooms And Groups When They’re Running On Different Services

Konnektor uses SkPy library and Corezoid engine (https://corezoid.com) to make integration between Skype, Slak and Telegram groups.
More integrations (WhatsApp, Facebook Messenger) is coming soon.

Official web page: http://evergreen.team/en/box-producs/konnektor.html

Skype to Slack integration
==============

Manual:

- register new Skype user
- setup Python, pip, SkPy, Flask, Requests, upload skype_listener_prod.py, skype_sender_prod.py to your server 
- Make new Slack app, set up incoming webhook and register post to channel https://api.slack.com/custom-integrations/outgoing-webhooks listener (http(s)://your_host/listen/skype) or Corezoid process (Corezoid is recommended, see below)
- If you choose Corezoid import SlackHostProcess into your Corezoid account and use Connect to Messnger -> Slack http://prntscr.com/jtpegi Event Subscription webhook http://prntscr.com/jtpepb as event listener
- if you will not use Telegram - live http://prntscr.com/ju8ahm with default values
- Change your Skype User login and password, change cluster chat ID  to your chat ID, set Slack webhook URL in .py files
- Run Flask with Gunicorn & Supervisor for skype_sender_prod.py and python with supervisor for skype_listener_prod.py 

Skype or Slack to Telegram integration
============

Manual (Corezoid https://corezoid.com account required!)

- register new Telegram bot via BotFather
- import Konnektor Telegram Host Process to your Corezoid account and connect it to your bot using Connect To Messenger http://prntscr.com/ju7eoa
- Set your integration type in the first SetParameter block - it should be "Skype" or "Slack" (without quotes)
- Set up your Slack webhook URL and Telegram bot token there http://prntscr.com/ju864f
- make Skype and/or Slack applications as described above. In this case you should use Corezoid and import SlackHostProcess and setup it http://prntscr.com/ju8ahm with your params
- if you want to set up Skype to Telegram integration instead of Skype to Slack integration, change mode="Slack" to mode="Telegram" in skype_listener.py 


**Contacts**

If you have any questions or help with Konnektor setup, contact support@evergreens.com.ua
Looking for more integrations? Check http://evergreen.team/en/box-producs/konnektor.html 








