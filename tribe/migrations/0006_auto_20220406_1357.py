# Generated by Django 3.2.12 on 2022-04-06 13:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tribe', '0005_auto_20220406_1340'),
    ]

    operations = [
        migrations.AlterField(
            model_name='podcasts',
            name='TribeId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tribe.tribes'),
        ),
        migrations.CreateModel(
            name='Videos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('VideoUrl', models.URLField()),
                ('TribeId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tribe.tribes')),
            ],
        ),
    ]
