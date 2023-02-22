# Generated by Django 4.1.6 on 2023-02-20 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pid', models.CharField(max_length=5)),
                ('name', models.CharField(max_length=10)),
                ('price', models.PositiveIntegerField()),
                ('size', models.CharField(choices=[('S', 'SMALL'), ('L', 'LARGE'), ('M', 'MEDIUM')], max_length=1)),
            ],
        ),
    ]