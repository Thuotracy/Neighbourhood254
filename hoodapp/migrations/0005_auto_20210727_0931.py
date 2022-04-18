from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hoodapp', '0004_auto_20210726_1637'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Post',
            new_name='News',
        ),
        migrations.DeleteModel(
            name='BlogPost',
        ),
    ]
