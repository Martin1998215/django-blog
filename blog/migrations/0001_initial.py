# Generated by Django 4.1 on 2022-10-12 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('intro', models.TextField()),
                ('body', models.TextField()),
                ('my_date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-my_date'],
            },
        ),
    ]
