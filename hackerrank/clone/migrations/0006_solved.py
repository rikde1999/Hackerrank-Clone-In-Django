# Generated by Django 4.0.3 on 2022-07-11 08:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('clone', '0005_remove_user_details_created_at_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Solved',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clone.code')),
                ('fk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
