# Generated by Django 2.0.2 on 2020-08-24 18:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=100)),
                ('answer', models.TextField()),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('days_till_study', models.IntegerField(default=1)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Deck',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('description', models.TextField(blank=True, max_length=200)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='card',
            name='decks',
            field=models.ManyToManyField(to='spaced_repitition.Deck'),
        ),
    ]
