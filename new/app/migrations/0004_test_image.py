# Generated by Django 4.1.4 on 2023-03-02 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_remove_test_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='test',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
