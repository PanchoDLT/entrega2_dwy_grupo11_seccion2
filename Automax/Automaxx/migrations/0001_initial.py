# Generated by Django 2.2.16 on 2020-10-30 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('cod', models.IntegerField(primary_key=True, serialize=False)),
                ('imagen', models.ImageField(upload_to='Slider')),
            ],
        ),
    ]