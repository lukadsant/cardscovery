# Generated by Django 4.2 on 2023-04-09 23:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_pessoa_info_pessoa_powerimg1_pessoa_powerimg2_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pessoa',
            name='powerimg2',
            field=models.TextField(default='https://media.tenor.com/ZTU55HQaVWIAAAAd/one-punch-man-opm.gif'),
        ),
        migrations.AlterField(
            model_name='pessoa',
            name='powerimg3',
            field=models.TextField(default='https://i.pinimg.com/originals/88/13/63/8813632e9591a260e59a195bd5b6c7d3.gif'),
        ),
    ]