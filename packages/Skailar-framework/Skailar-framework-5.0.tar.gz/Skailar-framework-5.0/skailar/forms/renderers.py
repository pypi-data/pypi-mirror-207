import functools
import warnings
from pathlib import Path

from skailar.conf import settings
from skailar.template.backends.skailar import SkailarTemplates
from skailar.template.loader import get_template
from skailar.utils.deprecation import RemovedInSkailar60Warning
from skailar.utils.functional import cached_property
from skailar.utils.module_loading import import_string


@functools.lru_cache
def get_default_renderer():
    renderer_class = import_string(settings.FORM_RENDERER)
    return renderer_class()


class BaseRenderer:
    form_template_name = "skailar/forms/div.html"
    formset_template_name = "skailar/forms/formsets/div.html"
    field_template_name = "skailar/forms/field.html"

    def get_template(self, template_name):
        raise NotImplementedError("subclasses must implement get_template()")

    def render(self, template_name, context, request=None):
        template = self.get_template(template_name)
        return template.render(context, request=request).strip()


class EngineMixin:
    def get_template(self, template_name):
        return self.engine.get_template(template_name)

    @cached_property
    def engine(self):
        return self.backend(
            {
                "APP_DIRS": True,
                "DIRS": [Path(__file__).parent / self.backend.app_dirname],
                "NAME": "skailarforms",
                "OPTIONS": {},
            }
        )


class SkailarTemplates(EngineMixin, BaseRenderer):
    """
    Load Skailar templates from the built-in widget templates in
    skailar/forms/templates and from apps' 'templates' directory.
    """

    backend = SkailarTemplates


class Jinja2(EngineMixin, BaseRenderer):
    """
    Load Jinja2 templates from the built-in widget templates in
    skailar/forms/jinja2 and from apps' 'jinja2' directory.
    """

    @cached_property
    def backend(self):
        from skailar.template.backends.jinja2 import Jinja2

        return Jinja2


# RemovedInSkailar60Warning.
class SkailarDivFormRenderer(SkailarTemplates):
    """
    Load Skailar templates from skailar/forms/templates and from apps'
    'templates' directory and use the 'div.html' template to render forms and
    formsets.
    """

    def __init__(self, *args, **kwargs):
        warnings.warn(
            "The SkailarDivFormRenderer transitional form renderer is deprecated. Use "
            "SkailarTemplates instead.",
            RemovedInSkailar60Warning,
        )
        super.__init__(*args, **kwargs)


# RemovedInSkailar60Warning.
class Jinja2DivFormRenderer(Jinja2):
    """
    Load Jinja2 templates from the built-in widget templates in
    skailar/forms/jinja2 and from apps' 'jinja2' directory.
    """

    def __init__(self, *args, **kwargs):
        warnings.warn(
            "The Jinja2DivFormRenderer transitional form renderer is deprecated. Use "
            "Jinja2 instead.",
            RemovedInSkailar60Warning,
        )
        super.__init__(*args, **kwargs)


class TemplatesSetting(BaseRenderer):
    """
    Load templates using template.loader.get_template() which is configured
    based on settings.TEMPLATES.
    """

    def get_template(self, template_name):
        return get_template(template_name)
