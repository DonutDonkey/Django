# Generated by Django 3.2.7 on 2021-09-08 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appImdbTutorial', '0007_auto_20210908_1503'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rating',
            old_name='movie',
            new_name='film',
        ),
        migrations.AlterField(
            model_name='additionalinfo',
            name='genre',
            field=models.PositiveSmallIntegerField(choices=[(3, 'Sci-fi'), (0, 'Else'), (2, 'Comedy'), (4, 'Drama'), (1, 'Horror')], default=0),
        ),
    ]