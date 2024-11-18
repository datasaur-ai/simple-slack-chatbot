def setup_endpoint(ack, body, client):
    ack()

    view = {
        "type": "modal",
        "callback_id": "setup_endpoint_submission",
        "title": {
            "type": "plain_text",
            "text": "Set Up Endpoint"
        },
        "submit": {
            "type": "plain_text",
            "text": "Save"
        },
        "close": {
            "type": "plain_text",
            "text": "Cancel"
        },
        "blocks": [
            {
                "type": "input",
                "block_id": "endpoint_input",
                "label": {
                    "type": "plain_text",
                    "text": "Deployed Endpoint URL"
                },
                "element": {
                    "type": "url_text_input",
                    "action_id": "endpoint",
                    "placeholder": {
                        "type": "plain_text",
                        "text": "Ex: https://llm.datasaur.ai/api/sandbox/1/1/sandbox-1"
                    }
                }
            },
            {
                "type": "input",
                "block_id": "api_key_input",
                "label": {
                    "type": "plain_text",
                    "text": "API Key"
                },
                "element": {
                    "type": "plain_text_input",
                    "action_id": "api_key",
                    "placeholder": {
                        "type": "plain_text",
                        "text": "Enter your API key"
                    }
                }
            }
        ]
    }

    client.views_open(
        trigger_id=body["trigger_id"],
        view=view
    )
