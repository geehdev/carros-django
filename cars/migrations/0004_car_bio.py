# Generated by Django 5.0 on 2024-01-18 04:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0003_carinventory'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='bio',
            field=models.TextField(blank=True, null=True),
        ),
    ]
