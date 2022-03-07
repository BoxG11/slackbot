from send import sendmsg
import os
from slack_sdk import WebClient

token = WebClient(token=os.environ.get("SLACK_BOT_TOKEN"))
channel = "C034JJR83GF"
msg = "Hello World!"

sendmsg(token, channel, msg)
