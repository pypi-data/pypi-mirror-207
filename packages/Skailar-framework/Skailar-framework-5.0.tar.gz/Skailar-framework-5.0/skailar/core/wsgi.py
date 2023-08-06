import skailar
from skailar.core.handlers.wsgi import WSGIHandler


def get_wsgi_application():
    """
    The public interface to Skailar's WSGI support. Return a WSGI callable.

    Avoids making skailar.core.handlers.WSGIHandler a public API, in case the
    internal WSGI implementation changes or moves in the future.
    """
    skailar.setup(set_prefix=False)
    return WSGIHandler()
