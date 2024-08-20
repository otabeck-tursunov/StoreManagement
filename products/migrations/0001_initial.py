# Generated by Django 5.0.7 on 2024-08-17 09:45

import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('brand', models.CharField(blank=True, max_length=50, null=True)),
                ('import_price', models.FloatField(validators=[django.core.validators.MinValueValidator(0)])),
                ('export_price', models.FloatField(validators=[django.core.validators.MinValueValidator(0)])),
                ('amount', models.FloatField(validators=[django.core.validators.MinValueValidator(0)])),
                ('unit', models.CharField(max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
