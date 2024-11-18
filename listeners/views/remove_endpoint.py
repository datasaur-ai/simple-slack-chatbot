from services.users import UserService
from listeners.events.app_home_opened import app_home_opened_callback


def handle_remove_endpoint_submission(ack, body, client):
    ack()
    user_id = body["user"]["id"]

    user_service = UserService()
    user_service.update_user(user_id, endpoint=None, api_key=None)

    app_home_opened_callback(
        client, {"user": user_id, "tab": "home"})
