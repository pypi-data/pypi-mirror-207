import os

AUTH_MIDDLEWARE = [
    "skailar.contrib.sessions.middleware.SessionMiddleware",
    "skailar.contrib.auth.middleware.AuthenticationMiddleware",
]

AUTH_TEMPLATES = [
    {
        "BACKEND": "skailar.template.backends.skailar.SkailarTemplates",
        "DIRS": [os.path.join(os.path.dirname(__file__), "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "skailar.template.context_processors.request",
                "skailar.contrib.auth.context_processors.auth",
                "skailar.contrib.messages.context_processors.messages",
            ],
        },
    }
]
