# Generated by Django 4.2.2 on 2023-06-20 02:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Conference',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('dates', models.CharField(max_length=255)),
                ('location', models.CharField(max_length=255)),
                ('topics', models.CharField(max_length=255)),
            ],
        ),
    ]
