# Generated by Django 4.0.6 on 2022-10-06 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_bookings_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Configs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='Дата')),
                ('comment', models.TextField(verbose_name='Комментарий')),
            ],
            options={
                'verbose_name': 'Настройка',
                'verbose_name_plural': 'Настройки',
            },
        ),
    ]
