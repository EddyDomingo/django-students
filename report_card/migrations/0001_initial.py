# Generated by Django 3.1.5 on 2021-01-10 02:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ReportCard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Fname', models.CharField(max_length=100)),
                ('Lname', models.CharField(max_length=100)),
                ('Email', models.EmailField(max_length=254)),
                ('Math', models.IntegerField()),
                ('English', models.IntegerField()),
                ('Physics', models.IntegerField()),
                ('Chemistry', models.IntegerField()),
                ('year_in_school', models.CharField(choices=[('1st', '1st'), ('2nd', '2nd'), ('3rd', '3rd'), ('4th', '4th'), ('5th', '5th')], default='1st', max_length=3)),
            ],
        ),
    ]
