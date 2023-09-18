# Generated by Django 4.2.5 on 2023-09-17 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64)),
                ('description', models.CharField(max_length=256)),
                ('expiratioDate', models.DateField()),
                ('state', models.DateField(max_length=40)),
            ],
        ),
    ]
