from services.summarizer import SummarizerService


def app_mention(client, context, event, say):
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
            reply_ts = say(mrkdwn=True, text='Generating...',
                           thread_ts=message_ts)['ts']
            summary = summarizer.summarize_thread(
                client, channel, thread_ts, mention_message)
            client.chat_update(channel=channel, text=summary, ts=reply_ts)

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
