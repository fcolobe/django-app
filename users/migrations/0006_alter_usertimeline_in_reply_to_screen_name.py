# Generated by Django 4.1 on 2023-04-01 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0005_alter_follower_description_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="usertimeline",
            name="in_reply_to_screen_name",
            field=models.CharField(max_length=15, null=True),
        ),
    ]