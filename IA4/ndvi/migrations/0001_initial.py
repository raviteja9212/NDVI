# Generated by Django 2.2.1 on 2019-05-23 12:39

from django.db import migrations, models
import django.utils.timezone
import ndvi.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NDVIModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now)),
                ('image', models.ImageField(upload_to=ndvi.models.ndvi_images)),
                ('min_ndvi', models.FloatField(default=0)),
                ('max_ndvi', models.FloatField(default=0)),
                ('avg_ndvi', models.FloatField(default=0)),
            ],
        ),
    ]