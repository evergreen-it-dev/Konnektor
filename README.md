# Konnektor
Konnektor Helps Connect Chatrooms And Groups When They’re Running On Different Services

Konnektor uses SkPy library and Corezoid engine (https://corezoid.com) to make integration between Skype, Slak and Telegram groups.
More integrations (WhatsApp, Facebook Messenger) is coming soon.

Official web page: http://evergreen.team/en/box-producs/konnektor.html

Manual:

- register new Skype user
- setup Python, pip, SkPy, Flask, Requests, upload skype_listener_prod.py, skype_sender_prod.py to your server 
- Make new Slack app, set up incoming webhook and register post to channel https://api.slack.com/custom-integrations/outgoing-webhooks listener (http(s)://your_host/listen/skype) or Corezoid process (Corezoid is recommended, see below)
- If you choose Corezoid import conv_.....json into your Corezoid account and use Connect to Messnger -> Slack http://prntscr.com/jtpegi Event Subscription webhook http://prntscr.com/jtpepb as event listener
- Change your Skype User login and password, change cluster chat ID  to your chat ID, set Slack webhook URL in .py files
- Run Flask with Gunicorn & Supervisor for skype_sender_prod.py and python with supervisor for skype_listener_prod.py 


**Contacts**

If you have any questions, contact support@evergreens.com.ua








