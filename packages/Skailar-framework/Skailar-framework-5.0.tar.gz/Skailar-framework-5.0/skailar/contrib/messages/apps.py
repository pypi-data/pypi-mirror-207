from skailar.apps import AppConfig
from skailar.contrib.messages.storage import base
from skailar.contrib.messages.utils import get_level_tags
from skailar.core.signals import setting_changed
from skailar.utils.translation import gettext_lazy as _


def update_level_tags(setting, **kwargs):
    if setting == "MESSAGE_TAGS":
        base.LEVEL_TAGS = get_level_tags()


class MessagesConfig(AppConfig):
    name = "skailar.contrib.messages"
    verbose_name = _("Messages")

    def ready(self):
        setting_changed.connect(update_level_tags)
