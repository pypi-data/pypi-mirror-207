import skailar.contrib.postgres.fields
from skailar.db import migrations, models


class Migration(migrations.Migration):
    dependencies = []

    operations = [
        migrations.CreateModel(
            name="IntegerArrayDefaultModel",
            fields=[
                (
                    "id",
                    models.AutoField(
                        verbose_name="ID",
                        serialize=False,
                        auto_created=True,
                        primary_key=True,
                    ),
                ),
                (
                    "field",
                    skailar.contrib.postgres.fields.ArrayField(
                        models.IntegerField(), size=None
                    ),
                ),
            ],
            options={},
            bases=(models.Model,),
        ),
    ]
