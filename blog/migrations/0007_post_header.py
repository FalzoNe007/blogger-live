# Generated by Django 4.0 on 2022-01-05 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_alter_post_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='header',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]