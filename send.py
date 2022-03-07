from slack_sdk.errors import SlackApiError

def sendmsg(token, channel, msg):
    client = token
    channel_id = channel

    try:
        result = client.chat_postMessage(
            channel=channel_id,
            text=msg
            # You could also use a blocks[] array to send richer content
        )
        # Print result, which includes information about the message (like TS)
        print(result)

    except SlackApiError as e:
        print(f"Error: {e}")



