import openai
from services.users import UserService


class SummarizerService:
    @staticmethod
    def test_connection(endpoint, api_key):
        try:
            client = openai.OpenAI(
                api_key=api_key, base_url=endpoint)
            client.chat.completions.create(
                model=None,
                messages=[{"role": "user", "content": "Hi"}])
            return True
        except Exception as e:
            return False

    def __init__(self, slack_user_id):
        user_service = UserService()
        user = user_service.get_or_create_user(slack_user_id)
        if not user['endpoint'] or not user['api_key']:
            raise ValueError("Endpoint and API key are required")
        self.client = openai.OpenAI(
            api_key=user['api_key'], base_url=user['endpoint'])

    def get_thread_messages(self, client, channel, ts):
        if not ts:
            return []

        message_replies = client.conversations_replies(
            channel=channel,
            ts=ts,
        )

        if not message_replies['messages']:
            return []

        latest_message = message_replies['messages'][0]
        parent_ts = latest_message['thread_ts'] if 'thread_ts' in latest_message else latest_message['ts']

        if not parent_ts:
            return message_replies['messages']

        thread_replies = client.conversations_replies(
            channel=channel,
            ts=parent_ts,
        )

        return thread_replies['messages'] if 'messages' in thread_replies else []

    def summarize_thread(
        self,
        client,
        channel,
        thread_ts,
        mention_message,
    ) -> str:
        thread_messages = self.get_thread_messages(
            client, channel, thread_ts)

        conversation_messages = []

        user_map = {}
        for message in thread_messages:
            text = message['text']
            user = message['user']
            user_info = None
            if user and user not in user_map:
                try:
                    user_info = client.users_info(user=user)['user']
                    user_map[user] = user_info
                except Exception:
                    user_info = None
            else:
                user_info = user_map[user]

            if not user_info or not text:
                continue

            conversation_messages.append(
                {"role": 'assistant' if user_info['is_bot'] else 'user', "content": f"{user_info['real_name']}: {text}"})

        if not mention_message:
            conversation_messages.append(
                {"role": "user", "content": "Summarize the conversation above"})

        response = self.client.chat.completions.create(
            model=None,
            messages=conversation_messages,
        ).choices[0].message.content

        return response if response else ''
