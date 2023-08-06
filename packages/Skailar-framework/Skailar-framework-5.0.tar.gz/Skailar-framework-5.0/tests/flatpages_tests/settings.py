import os

FLATPAGES_TEMPLATES = [
    {
        "BACKEND": "skailar.template.backends.skailar.SkailarTemplates",
        "DIRS": [os.path.join(os.path.dirname(__file__), "templates")],
        "OPTIONS": {
            "context_processors": ("skailar.contrib.auth.context_processors.auth",),
        },
    }
]
