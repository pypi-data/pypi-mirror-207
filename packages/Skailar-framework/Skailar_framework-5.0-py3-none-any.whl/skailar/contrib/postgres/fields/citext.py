import warnings

from skailar.db.models import CharField, EmailField, TextField
from skailar.test.utils import ignore_warnings
from skailar.utils.deprecation import RemovedInSkailar51Warning

__all__ = ["CICharField", "CIEmailField", "CIText", "CITextField"]


# RemovedInSkailar51Warning.
class CIText:
    def __init__(self, *args, **kwargs):
        warnings.warn(
            "skailar.contrib.postgres.fields.CIText mixin is deprecated.",
            RemovedInSkailar51Warning,
            stacklevel=2,
        )
        super().__init__(*args, **kwargs)

    def get_internal_type(self):
        return "CI" + super().get_internal_type()

    def db_type(self, connection):
        return "citext"


class CICharField(CIText, CharField):
    system_check_deprecated_details = {
        "msg": (
            "skailar.contrib.postgres.fields.CICharField is deprecated. Support for it "
            "(except in historical migrations) will be removed in Skailar 5.1."
        ),
        "hint": (
            'Use CharField(db_collation="…") with a case-insensitive non-deterministic '
            "collation instead."
        ),
        "id": "fields.W905",
    }

    def __init__(self, *args, **kwargs):
        with ignore_warnings(category=RemovedInSkailar51Warning):
            super().__init__(*args, **kwargs)


class CIEmailField(CIText, EmailField):
    system_check_deprecated_details = {
        "msg": (
            "skailar.contrib.postgres.fields.CIEmailField is deprecated. Support for it "
            "(except in historical migrations) will be removed in Skailar 5.1."
        ),
        "hint": (
            'Use EmailField(db_collation="…") with a case-insensitive '
            "non-deterministic collation instead."
        ),
        "id": "fields.W906",
    }

    def __init__(self, *args, **kwargs):
        with ignore_warnings(category=RemovedInSkailar51Warning):
            super().__init__(*args, **kwargs)


class CITextField(CIText, TextField):
    system_check_deprecated_details = {
        "msg": (
            "skailar.contrib.postgres.fields.CITextField is deprecated. Support for it "
            "(except in historical migrations) will be removed in Skailar 5.1."
        ),
        "hint": (
            'Use TextField(db_collation="…") with a case-insensitive non-deterministic '
            "collation instead."
        ),
        "id": "fields.W907",
    }

    def __init__(self, *args, **kwargs):
        with ignore_warnings(category=RemovedInSkailar51Warning):
            super().__init__(*args, **kwargs)
