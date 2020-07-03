# Generated by Django 3.0.8 on 2020-07-03 21:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_offer_products'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='offer',
            name='products',
        ),
        migrations.AddField(
            model_name='product',
            name='offer',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='products.Offer'),
        ),
    ]
