from skailar.apps import AppConfig


class ModelDefaultPKConfig(AppConfig):
    name = "model_options"


class ModelPKConfig(AppConfig):
    name = "model_options"
    default_auto_field = "skailar.db.models.SmallAutoField"


class ModelPKNonAutoConfig(AppConfig):
    name = "model_options"
    default_auto_field = "skailar.db.models.TextField"


class ModelPKNoneConfig(AppConfig):
    name = "model_options"
    default_auto_field = None


class ModelPKNonexistentConfig(AppConfig):
    name = "model_options"
    default_auto_field = "skailar.db.models.NonexistentAutoField"
