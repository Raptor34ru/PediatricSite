# Generated by Django 4.0.5 on 2022-06-22 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('department', '0003_tablecat_tables'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tablecat',
            options={'verbose_name': 'Курс', 'verbose_name_plural': 'Курсы'},
        ),
        migrations.RemoveField(
            model_name='sotr',
            name='rank',
        ),
        migrations.AddField(
            model_name='sotr',
            name='education',
            field=models.CharField(blank=True, max_length=100, verbose_name='Звание'),
        ),
    ]
