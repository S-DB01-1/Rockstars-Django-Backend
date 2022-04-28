# Generated by Django 3.2.12 on 2022-04-13 10:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tribe', '0002_auto_20220413_1002'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='podcasts',
            name='SpotifyUrl',
        ),
        migrations.AddField(
            model_name='podcasts',
            name='Description',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='podcasts',
            name='Name',
            field=models.CharField(default='test podcast', max_length=255),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='PodcastEpisode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SpotifyUrl', models.URLField()),
                ('Podcast', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='tribe.podcasts')),
            ],
        ),
    ]