# Generated by Django 3.0.8 on 2020-10-08 19:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0011_auto_20201008_1738'),
    ]

    operations = [
        migrations.AlterField(
            model_name='graphs',
            name='nnb_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='test', to='service.NeuralNetworks'),
        ),
    ]
