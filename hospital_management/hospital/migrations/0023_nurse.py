# Generated by Django 5.0.1 on 2024-06-10 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0022_delete_staff'),
    ]

    operations = [
        migrations.CreateModel(
            name='Nurse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=150)),
                ('password', models.CharField(max_length=128)),
            ],
        ),
    ]
