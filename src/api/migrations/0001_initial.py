# Generated by Django 3.0.4 on 2020-03-14 05:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='noteModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('note', models.TextField(blank=True)),
                ('newUpdatedDate', models.DateTimeField()),
                ('lastUpdatedDate', models.DateTimeField(blank=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]