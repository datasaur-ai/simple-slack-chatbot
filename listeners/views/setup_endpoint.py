import validators
from services.summarizer import SummarizerService
from services.users import UserService
from listeners.events.app_home_opened import app_home_opened_callback


def handle_setup_endpoint_submission(ack, body, client, view):
    user_id = body["user"]["id"]

    endpoint = view["state"]["values"]["endpoint_input"]["endpoint"]["value"]
    api_key = view["state"]["values"]["api_key_input"]["api_key"]["value"]

    errors = {}
    if not validators.url(endpoint):
        errors["endpoint_input"] = "Please enter a valid URL"

    if not api_key:
        errors["api_key_input"] = "API key cannot be empty"

    if errors:
        ack(response_action="errors", errors=errors)
        return
    ack()

    if not SummarizerService.test_connection(endpoint, api_key):
        client.views_open(
            trigger_id=body["trigger_id"],
            view={
                "type": "modal",
                "title": {
                    "type": "plain_text",
                    "text": "Connection Error"
                },
                "close": {
                    "type": "plain_text",
                    "text": "Close"
                },
                "blocks": [
                    {
                        "type": "section",
                        "text": {
                            "type": "mrkdwn",
                            "text": "Unable to connect using the provided endpoint and API key. Please check and try again."
                        }
                    }
                ]
            }
        )
        return

    user_service = UserService()
    user_service.update_user(user_id, endpoint=endpoint, api_key=api_key)

    app_home_opened_callback(
        client, {"user": user_id, "tab": "home"})
