# Generated by Django 4.2 on 2023-04-09 22:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_pessoa_wallpaper'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pessoa',
            name='wallpaper',
            field=models.TextField(default='https://e1.pxfuel.com/desktop-wallpaper/208/877/desktop-wallpaper-shounen-manga-panel-anime-all-manga.jpg'),
        ),
    ]
