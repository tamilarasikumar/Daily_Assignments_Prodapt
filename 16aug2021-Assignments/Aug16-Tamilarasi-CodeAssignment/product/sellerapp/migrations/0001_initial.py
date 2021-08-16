# Generated by Django 3.0.6 on 2021-08-16 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sellerapp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sell_id', models.IntegerField()),
                ('sell_name', models.CharField(max_length=50)),
                ('sell_address', models.CharField(max_length=50)),
                ('sell_mblno', models.BigIntegerField(default=1)),
            ],
        ),
    ]
