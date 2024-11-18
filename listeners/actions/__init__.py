from .setup_endpoint import setup_endpoint
from .remove_endpoint import remove_endpoint


def register(app):
    app.action("setup_endpoint")(setup_endpoint)
    app.action("remove_endpoint")(remove_endpoint)
