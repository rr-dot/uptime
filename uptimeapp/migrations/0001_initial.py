# Generated by Django 3.2.16 on 2022-12-31 21:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Url',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=2500)),
                ('cur_status', models.IntegerField()),
                ('exception_msg', models.CharField(default='', max_length=3000)),
            ],
        ),
    ]