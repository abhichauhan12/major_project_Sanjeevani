# Generated by Django 3.1.7 on 2021-06-06 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_remove_profile_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(upload_to='', verbose_name='ansh.jpg'),
        ),
    ]
