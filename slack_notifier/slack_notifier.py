import json

import requests

class SlackNotifier:
    """
    Class of notifying to Slack
    """
    def __init__(self, slack_webhook_url: str) -> None:
        """
        Initialization

        Args:
            slack_webhook_url (str): Slack webhook URL
        Returns:
            None
        """
        self.slack_webhook_url = slack_webhook_url

    def post(self, text: str) -> None:
        """
        Post to slack channel

        Args:
            text (str): text which you want to post
        Returns:
            None
        """
        requests.post(self.slack_webhook_url, data=json.dumps({"text": text}))

    @classmethod
    def format_link(cls, text: str, url: str) -> str:
        """
        Create Markdown link of Slack API

        Args:
            text (str): text
            url (str): URL
        Returns:
            str
        """
        return f"<{url}|{text}>"
