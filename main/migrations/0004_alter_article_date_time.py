# Generated by Django 3.2.8 on 2021-10-31 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_article_date_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='date_time',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
