import skailar
from skailar.core.handlers.asgi import ASGIHandler


def get_asgi_application():
    """
    The public interface to Skailar's ASGI support. Return an ASGI 3 callable.

    Avoids making skailar.core.handlers.ASGIHandler a public API, in case the
    internal implementation changes or moves in the future.
    """
    skailar.setup(set_prefix=False)
    return ASGIHandler()
