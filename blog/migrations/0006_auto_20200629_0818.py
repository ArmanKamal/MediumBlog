# Generated by Django 3.0.7 on 2020-06-29 15:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20200629_0814'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blogpost',
            options={'ordering': ['-publish_date', '-update', '-timestamp']},
        ),
    ]
