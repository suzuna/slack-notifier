# slack-notifier

A simple Python package to post to a Slack channel via Slack webhook URL.

## Install

```bash
pip install git+https://github.com/suzuna/slack-notifier.git
```

## Usage

```python
from slack_notifier import SlackNotifier

slack_notifier = SlackNotifier(slack_webhook_url="YOUR_SLACK_WEBHOOK_URL")
slack_notifier.post("Hello, World!")
slack_notifier.post(
    f'Here is {SlackNotifier.format_link("Example Link", "https://example.com")}'
)
```
