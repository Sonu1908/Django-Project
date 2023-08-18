# Generated by Django 4.2.2 on 2023-06-11 02:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_professor'),
    ]

    operations = [
        migrations.RenameField(
            model_name='professor',
            old_name='Student',
            new_name='student',
        ),
        migrations.AddField(
            model_name='professor',
            name='price',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
