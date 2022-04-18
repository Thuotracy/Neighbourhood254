import cloudinary.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import tinymce.models
import url_or_relative_url_field.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Hood',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=60)),
                ('hoodimage', cloudinary.models.CloudinaryField(max_length=255)),
                ('description', tinymce.models.HTMLField()),
                ('police_number', models.IntegerField(blank=True, null=True)),
                ('emergency_no', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', tinymce.models.HTMLField(max_length=100)),
                ('profile_pic', cloudinary.models.CloudinaryField(default='https://res.cloudinary.com/playboard/image/upload/v1626529829/vjytnast5wblft8xvy9p.jpg', max_length=255)),
                ('full_name', models.CharField(blank=True, max_length=120)),
                ('profession', models.CharField(blank=True, max_length=120)),
                ('email_address', models.EmailField(blank=True, max_length=254, null=True)),
                ('website_url', url_or_relative_url_field.fields.URLOrRelativeURLField(blank=True, null=True)),
                ('facebook', url_or_relative_url_field.fields.URLOrRelativeURLField(blank=True, null=True)),
                ('instagram', url_or_relative_url_field.fields.URLOrRelativeURLField(blank=True, null=True)),
                ('twitter', url_or_relative_url_field.fields.URLOrRelativeURLField(blank=True, null=True)),
                ('mobile_number', models.IntegerField(blank=True, null=True)),
                ('location', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='members', to='hoodapp.Hood')),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120, null=True)),
                ('details', models.TextField()),
                ('post_date', models.DateTimeField(auto_now_add=True)),
                ('hood', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hood_post', to='hoodapp.Hood')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_owner', to='hoodapp.Profile')),
            ],
        ),
        migrations.AddField(
            model_name='hood',
            name='admin',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='admin', to='hoodapp.Profile'),
        ),
        migrations.CreateModel(
            name='Business',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bs_name', models.CharField(max_length=100)),
                ('description', tinymce.models.HTMLField(blank=True)),
                ('bs_logo', cloudinary.models.CloudinaryField(max_length=255)),
                ('bs_email', models.EmailField(blank=True, max_length=254)),
                ('facebook', url_or_relative_url_field.fields.URLOrRelativeURLField(blank=True, null=True)),
                ('instagram', url_or_relative_url_field.fields.URLOrRelativeURLField(blank=True, null=True)),
                ('twitter', url_or_relative_url_field.fields.URLOrRelativeURLField(blank=True, null=True)),
                ('hood', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='business', to='hoodapp.Hood')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='owner', to='hoodapp.Profile')),
            ],
        ),
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('blog_post', models.TextField()),
                ('posted', models.DateTimeField(auto_now_add=True)),
                ('neighborhood', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post', to='hoodapp.Hood')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_editor', to='hoodapp.Profile')),
            ],
        ),
    ]
