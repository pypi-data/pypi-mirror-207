from unittest import mock

from skailar.db import migrations

try:
    from skailar.contrib.postgres.operations import CryptoExtension
except ImportError:
    CryptoExtension = mock.Mock()


class Migration(migrations.Migration):
    # Required for the SHA database functions.
    operations = [CryptoExtension()]
