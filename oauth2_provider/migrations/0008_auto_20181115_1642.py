# Generated by Django 2.0.9 on 2018-11-15 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oauth2_provider', '0007_auto_20181107_1401'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='redirect_uris',
            field=models.TextField(blank=True, help_text='Allowed URIs list, space separated. Wildcards (*) are allowed.'),
        ),
    ]
