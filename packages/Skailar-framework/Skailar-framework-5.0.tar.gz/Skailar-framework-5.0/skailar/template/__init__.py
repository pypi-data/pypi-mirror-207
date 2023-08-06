"""
Skailar's support for templates.

The skailar.template namespace contains two independent subsystems:

1. Multiple Template Engines: support for pluggable template backends,
   built-in backends and backend-independent APIs
2. Skailar Template Language: Skailar's own template engine, including its
   built-in loaders, context processors, tags and filters.

Ideally these subsystems would be implemented in distinct packages. However
keeping them together made the implementation of Multiple Template Engines
less disruptive .

Here's a breakdown of which modules belong to which subsystem.

Multiple Template Engines:

- skailar.template.backends.*
- skailar.template.loader
- skailar.template.response

Skailar Template Language:

- skailar.template.base
- skailar.template.context
- skailar.template.context_processors
- skailar.template.loaders.*
- skailar.template.debug
- skailar.template.defaultfilters
- skailar.template.defaulttags
- skailar.template.engine
- skailar.template.loader_tags
- skailar.template.smartif

Shared:

- skailar.template.utils

"""

# Multiple Template Engines

from .engine import Engine
from .utils import EngineHandler

engines = EngineHandler()

__all__ = ("Engine", "engines")


# Skailar Template Language

# Public exceptions
from .base import VariableDoesNotExist  # NOQA isort:skip
from .context import Context, ContextPopException, RequestContext  # NOQA isort:skip
from .exceptions import TemplateDoesNotExist, TemplateSyntaxError  # NOQA isort:skip

# Template parts
from .base import (  # NOQA isort:skip
    Node,
    NodeList,
    Origin,
    Template,
    Variable,
)

# Library management
from .library import Library  # NOQA isort:skip

# Import the .autoreload module to trigger the registrations of signals.
from . import autoreload  # NOQA isort:skip


__all__ += ("Template", "Context", "RequestContext")
