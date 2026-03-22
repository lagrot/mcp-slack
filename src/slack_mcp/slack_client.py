import os
from slack_bolt import App

class SlackClient:
    def __init__(self):
        self.app = App(
            token=os.environ.get("SLACK_BOT_TOKEN"),
            signing_secret=os.environ.get("SLACK_SIGNING_SECRET")
        )

    def send_message(self, channel_id: str, message: str):
        return self.app.client.chat_postMessage(channel=channel_id, text=message)
