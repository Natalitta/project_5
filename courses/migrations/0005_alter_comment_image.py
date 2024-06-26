# Generated by Django 3.2.23 on 2024-04-16 21:45

import django.core.validators
from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0004_comment_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='image',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, force_format=None, keep_meta=True, null=True, quality=75, scale=None, size=[300, 300], upload_to='images/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png', 'gif'])]),
        ),
    ]
