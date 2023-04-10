# Generated by Django 4.2 on 2023-04-08 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_pessoa_sobrenome'),
    ]

    operations = [
        migrations.AddField(
            model_name='pessoa',
            name='imagem',
            field=models.CharField(default='https://cdn.myanimelist.net/images/characters/11/497292.jpg', max_length=255),
        ),
        migrations.AlterField(
            model_name='pessoa',
            name='sobrenome',
            field=models.CharField(default='', max_length=100),
        ),
    ]
