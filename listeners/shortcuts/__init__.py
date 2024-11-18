from .summarize import summarize_shortcut


def register(app):
    app.shortcut("summarize")(summarize_shortcut)
