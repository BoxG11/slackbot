from slack_sdk.errors import SlackApiError
from slack_sdk import WebClient
from tojson import save
import json

client = WebClient(token=(""))

key = "channels"
key2 = "name"
key3 = "id"

try:
    # Call the conversations.list method using the WebClient
    result = client.conversations_list(

    )
    result = str(result)

    while True:
        try:
            #crops the purpose from each channel to avoid illegal characters
            index = result.index("purpose") - 2
            index2 = result.index("}", index) + 2
            result = result[0: index:] + result[index2::]
        except:
            break
    #formats the result to valid json
    resultformat = save(result)

    jsoon = json.loads(str(resultformat))

    for ding in jsoon:
        if ding == key:
            value = jsoon.get(key)
            for ding1 in value:
                value1 = ding1.get(key2)
                value2 = ding1.get(key3)
                print(value1, value2)

except SlackApiError as e:
    print(f"Error: {e}")



