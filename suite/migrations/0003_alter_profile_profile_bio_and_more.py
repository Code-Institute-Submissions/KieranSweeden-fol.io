# Generated by Django 4.0.3 on 2022-05-04 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('suite', '0002_alter_folio_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_bio',
            field=models.TextField(max_length=300),
        ),
        migrations.AlterField(
            model_name='project',
            name='project_description',
            field=models.TextField(max_length=300),
        ),
        migrations.AlterField(
            model_name='skill',
            name='skill_description',
            field=models.TextField(max_length=300),
        ),
    ]