# Generated by Django 4.0.6 on 2022-08-25 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('name', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
        ),
    ]
