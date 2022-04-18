from django.db import migrations
import url_or_relative_url_field.fields


class Migration(migrations.Migration):

    dependencies = [
        ('hoodapp', '0002_auto_20210726_1455'),
    ]

    operations = [
        migrations.AlterField(
            model_name='business',
            name='facebook',
            field=url_or_relative_url_field.fields.URLOrRelativeURLField(default='https://web.facebook.com/', max_length=100),
        ),
        migrations.AlterField(
            model_name='business',
            name='instagram',
            field=url_or_relative_url_field.fields.URLOrRelativeURLField(default='https://www.instagram.com/', max_length=100),
        ),
        migrations.AlterField(
            model_name='business',
            name='twitter',
            field=url_or_relative_url_field.fields.URLOrRelativeURLField(default='https://twitter.com/', max_length=100),
        ),
    ]
