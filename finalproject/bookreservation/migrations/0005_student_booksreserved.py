# Generated by Django 4.2.8 on 2023-12-14 03:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookreservation', '0004_alter_student_year'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='booksReserved',
            field=models.IntegerField(default=0),
        ),
    ]
