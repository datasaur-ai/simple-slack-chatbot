def remove_endpoint(ack, body, client):
    ack()

    view = {
        "type": "modal",
        "callback_id": "remove_endpoint_confirmation",
        "title": {
            "type": "plain_text",
            "text": "Remove Endpoint"
        },
        "submit": {
            "type": "plain_text",
            "text": "Confirm"
        },
        "close": {
            "type": "plain_text",
            "text": "Cancel"
        },
        "blocks": [
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "Are you sure you want to remove your current endpoint and API key?"
                }
            }
        ]
    }

    client.views_open(
        trigger_id=body["trigger_id"],
        view=view
    )
