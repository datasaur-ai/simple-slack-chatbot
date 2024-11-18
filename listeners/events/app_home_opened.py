from services.users import UserService


def app_home_opened_callback(client, event):
    user_service = UserService()

    if event["tab"] != "home":
        return

    user = user_service.get_or_create_user(event["user"])

    if 'endpoint' in user and user['endpoint']:
        endpoint_section = [
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": f"*Your Current Endpoint:*\n{user['endpoint']}"
                }
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": f"*Your Current API Key:*\n{user['api_key'][:4]}...{user['api_key'][-4:]}"
                }
            },
            {
                "type": "actions",
                "elements": [
                    {
                        "type": "button",
                        "text": {
                            "type": "plain_text",
                            "text": ":no_entry: Remove Endpoint",
                            "emoji": True
                        },
                        "value": "remove_endpoint",
                        "action_id": "remove_endpoint"
                    }
                ]
            }
        ]
    else:
        endpoint_section = [
            {
                "type": "section",
                "text": {
                        "type": "mrkdwn",
                        "text": "You can start by setting up an endpoint."
                }
            },
            {
                "type": "actions",
                "elements": [

                        {
                            "type": "button",
                            "text": {
                                "type": "plain_text",
                                "text": ":pencil2: Set Up Endpoint",
                                "emoji": True
                            },
                            "value": "setup_endpoint",
                            "action_id": "setup_endpoint"
                        }
                ]
            }
        ]

    client.views_publish(
        user_id=event["user"],
        view={
            "type": "home",
            "blocks": [
                {
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": "*Hi, <@" + event["user"] + ">!*",
                    },
                },
                *endpoint_section,
            ],
        },
    )
