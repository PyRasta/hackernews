# Generated by Django 3.2.8 on 2021-11-02 22:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_auto_20211103_0219'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='createaccount',
            options={'verbose_name': 'Пользователь', 'verbose_name_plural': 'Пользователи'},
        ),
        migrations.AlterModelOptions(
            name='findaccount',
            options={'verbose_name': 'Авторизированный Пользователь', 'verbose_name_plural': ' Авторизированные Пользователи'},
        ),
    ]