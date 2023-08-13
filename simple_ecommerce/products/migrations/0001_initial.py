# Generated by Django 4.2.2 on 2023-08-13 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_created=True)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(max_length=500, null=True)),
                ('product_id', models.CharField(max_length=50)),
                ('price', models.FloatField()),
                ('sale', models.BooleanField(default=False)),
            ],
        ),
    ]