# Generated by Django 4.1 on 2022-10-28 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_alter_project_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.FilePathField(path='project_portfolio/static/img'),
        ),
    ]