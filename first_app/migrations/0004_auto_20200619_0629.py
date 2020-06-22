# Generated by Django 3.0.3 on 2020-06-19 06:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('first_app', '0003_auto_20200516_0642'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accesslog',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='first_app.Webpage'),
        ),
        migrations.CreateModel(
            name='UserProfileInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField(blank=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
