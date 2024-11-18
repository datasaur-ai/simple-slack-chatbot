
from slack_bolt import Ack
from slack_sdk import WebClient

from services.summarizer import SummarizerService


def summarize_shortcut(ack, body, client, context, shortcut):
    ack()
    modalView = client.views_open(
        trigger_id=body["trigger_id"],
        view={
            "type": "modal",
            "callback_id": "summarize_view_id",
            "title": {"type": "plain_text", "text": "Thread Summary"},
            "blocks": [
                {
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": "Summarizing thread...",
                    },

                },

            ],
            "close": {"type": "plain_text", "text": "Close"},
        },
    )
    if 'view' not in modalView:
        raise Exception("Failed to open modal")

    try:

        channel = shortcut['channel']['id']

        shortcut_message = client.conversations_replies(
            channel=channel,
            ts=shortcut['message']['ts'],
        )

        if not shortcut_message:
            raise Exception("Failed to get thread")

        thread_ts = shortcut_message['messages'][0]['thread_ts']

        summarizer = SummarizerService(context['user_id'])
        summary = summarizer.summarize_thread(
            client=client, channel=channel, thread_ts=thread_ts, mention_message=None)
        client.views_update(view_id=modalView['view']['id'], view={
            "type": "modal",
            "title": {"type": "plain_text", "text": "Thread Summary"},
            "blocks": [
                {"type": "section", "text": {"type": "mrkdwn", "text": summary}},
            ],
        })
    except ValueError:
        client.views_update(view_id=modalView['view']['id'], view={
            "type": "modal",
            "title": {"type": "plain_text", "text": "Error"},
            "blocks": [
                {"type": "section", "text": {"type": "mrkdwn",
                                             "text": "Please set up your endpoint first."}},
            ],
        })
    except Exception as e:
        client.views_update(view_id=modalView['view']['id'], view={
            "type": "modal",
            "title": {"type": "plain_text", "text": "Error"},
            "blocks": [
                {"type": "section", "text": {"type": "mrkdwn",
                                             "text": f"Sorry, something went wrong. Please try again later. ({e})"}},
            ],
        })
