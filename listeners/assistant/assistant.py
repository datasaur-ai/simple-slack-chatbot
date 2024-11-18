from slack_bolt import Assistant
from services.summarizer import SummarizerService


assistant = Assistant()


@assistant.thread_started
def thread_started(client, event):
    client.assistant_threads_setSuggestedPrompts(
        channel_id=event['assistant_thread']['channel_id'],
        thread_ts=event['assistant_thread']['thread_ts'],
        prompts=[
            {
                "title": 'What is LLM?',
                "message": 'What is LLM?',
            },
            {
                "title": 'Give me 5 random AI facts',
                "message": 'Give me 5 random AI facts',
            },
            {
                "title": 'Can you tell me a joke?',
                "message": 'Can you tell me a joke?',
            },
        ],
    )


@assistant.user_message
def user_message(client, context, set_status, event, say):
    message_ts = event['ts']
    channel = event['channel']
    user = event['user']
    reply_ts = None
    try:
        message_replies = client.conversations_replies(
            channel=channel,
            ts=message_ts
        )

        if not message_replies['messages']:
            return

        latest_message = message_replies['messages'][0]
        mention_message = latest_message['text']
        thread_ts = latest_message['thread_ts'] if 'thread_ts' in latest_message else latest_message['ts']

        if mention_message:
            summarizer = SummarizerService(context['user_id'])
            set_status("is typing...")
            summary = summarizer.summarize_thread(
                client=client, channel=channel, thread_ts=thread_ts, mention_message=mention_message)
            say(channel=channel, text=summary)

    except ValueError:
        client.chat_postEphemeral(
            channel=channel,
            user=user,
            text="Please set up your endpoint first.")
    except Exception as e:
        if reply_ts:
            client.chat_delete(channel=channel, ts=reply_ts)
        client.chat_postEphemeral(
            channel=channel,
            user=user,
            text=f"Sorry, something went wrong. Please try again later. ({e})")
