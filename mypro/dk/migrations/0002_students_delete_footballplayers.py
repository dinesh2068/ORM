# Generated by Django 4.2.6 on 2023-12-31 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dk', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='students',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rollno', models.IntegerField()),
                ('name', models.CharField(default=0, max_length=100)),
                ('age', models.IntegerField()),
                ('mobileno', models.IntegerField()),
                ('city', models.CharField(default=0, max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='footballplayers',
        ),
    ]