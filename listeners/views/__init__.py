from .remove_endpoint import handle_remove_endpoint_submission
from .setup_endpoint import handle_setup_endpoint_submission


def register(app):
    app.view("remove_endpoint_confirmation")(handle_remove_endpoint_submission)
    app.view("setup_endpoint_submission")(handle_setup_endpoint_submission)
