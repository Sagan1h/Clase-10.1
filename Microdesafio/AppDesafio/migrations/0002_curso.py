# Generated by Django 4.2.6 on 2023-10-29 23:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppDesafio', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('curso', models.CharField(max_length=100)),
                ('camada', models.IntegerField()),
            ],
        ),
    ]