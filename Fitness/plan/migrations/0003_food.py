# Generated by Django 4.1.3 on 2022-11-15 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plan', '0002_alter_exercises_day_exercises'),
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meal', models.TextField()),
                ('colres', models.FloatField()),
            ],
        ),
    ]