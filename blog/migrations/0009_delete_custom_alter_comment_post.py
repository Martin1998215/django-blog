# Generated by Django 4.1 on 2022-11-01 18:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_delete_customer'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Custom',
        ),
        migrations.AlterField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.mypost'),
        ),
    ]
