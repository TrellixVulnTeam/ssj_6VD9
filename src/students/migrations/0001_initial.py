# Generated by Django 2.2.2 on 2019-06-05 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('gender', models.TextField()),
                ('mobile', models.TextField()),
                ('email_id', models.TextField()),
                ('dept_id', models.IntegerField()),
                ('course_id', models.IntegerField()),
                ('password', models.TextField()),
                ('address', models.TextField()),
            ],
        ),
    ]
