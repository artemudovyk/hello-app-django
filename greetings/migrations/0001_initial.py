# Generated by Django 4.0 on 2022-01-09 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Greeting',
            fields=[
                ('email', models.EmailField(max_length=40, primary_key=True, serialize=False)),
            ],
        ),
    ]
