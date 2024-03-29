# Generated by Django 2.0.2 on 2020-09-19 17:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('spaced_repitition', '0002_card_copied'),
    ]

    operations = [
        migrations.CreateModel(
            name='Added',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AddField(
            model_name='card',
            name='added_total',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='added',
            name='cardID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='spaced_repitition.Card'),
        ),
        migrations.AddField(
            model_name='added',
            name='userID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
