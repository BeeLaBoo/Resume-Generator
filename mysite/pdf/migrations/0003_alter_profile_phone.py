# Generated by Django 4.0.5 on 2022-06-25 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pdf', '0002_remove_profile_experience_profile_github_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='phone',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
