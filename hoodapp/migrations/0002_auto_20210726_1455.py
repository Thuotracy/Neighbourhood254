import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hoodapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='business',
            name='bs_email',
            field=models.EmailField(max_length=50),
        ),
        migrations.AlterField(
            model_name='business',
            name='bs_logo',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name='image'),
        ),
    ]
