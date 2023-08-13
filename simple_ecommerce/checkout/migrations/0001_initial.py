# Generated by Django 4.2.2 on 2023-08-13 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Checkout',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_created=True)),
                ('address', models.CharField(max_length=255)),
                ('contact', models.EmailField(max_length=254)),
                ('item', models.ManyToManyField(related_name='cart_checkout', to='cart.cart')),
            ],
        ),
    ]
