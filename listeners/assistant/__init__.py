from .assistant import assistant


def register(app):
    app.use(assistant)
