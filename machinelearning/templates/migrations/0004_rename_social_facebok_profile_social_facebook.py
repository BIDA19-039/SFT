# Generated by Django 3.2.7 on 2021-09-20 06:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('machinelearning', '0003_auto_20210920_0826'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='social_facebok',
            new_name='social_facebook',
        ),
    ]
