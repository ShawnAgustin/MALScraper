# Generated by Django 2.1.7 on 2019-03-12 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anime', '0002_auto_20190312_1156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='show',
            name='weebtitle',
            field=models.CharField(max_length=100),
        ),
    ]
