# Generated by Django 4.1.5 on 2024-04-27 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_alter_corporate_phone'),
    ]

    operations = [
        migrations.CreateModel(
            name='Larq',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=155)),
                ('date', models.DateField()),
            ],
        ),
    ]
