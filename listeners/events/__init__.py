from .app_home_opened import app_home_opened_callback
from .app_mention import app_mention


def register(app):
    app.event("app_home_opened")(app_home_opened_callback)
    app.event("app_mention")(app_mention)
