# Generated by Django 4.0.4 on 2022-05-12 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('articleid', models.AutoField(db_column='ArticleId', primary_key=True, serialize=False)),
                ('title', models.TextField(blank=True, db_column='Title', null=True)),
                ('description', models.TextField(blank=True, db_column='Description', null=True)),
                ('datecreated', models.DateTimeField(db_column='DateCreated')),
                ('datemodified', models.DateTimeField(db_column='DateModified')),
                ('datepublished', models.DateTimeField(db_column='DatePublished')),
                ('publishedstatus', models.BooleanField(db_column='PublishedStatus')),
                ('viewcount', models.IntegerField(db_column='ViewCount')),
            ],
            options={
                'db_table': 'Article',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ArticleImage',
            fields=[
                ('articleimageid', models.AutoField(db_column='ArticleImageId', primary_key=True, serialize=False)),
                ('url', models.TextField(blank=True, db_column='URL', null=True)),
            ],
            options={
                'db_table': 'ArticleImages',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Podcast',
            fields=[
                ('podcastid', models.AutoField(db_column='PodcastId', primary_key=True, serialize=False)),
                ('titel', models.TextField(blank=True, db_column='Titel', null=True)),
                ('omschrijving', models.TextField(blank=True, db_column='Omschrijving', null=True)),
                ('spotifyurl', models.TextField(blank=True, db_column='URL', null=True)),
                ('datecreated', models.DateTimeField(db_column='DateCreated')),
                ('datemodified', models.DateTimeField(db_column='DateModified')),
                ('datepublished', models.DateTimeField(db_column='DatePublished')),
                ('publishedstatus', models.BooleanField(db_column='PublishedStatus')),
                ('viewcount', models.IntegerField(db_column='ViewCount')),
            ],
            options={
                'db_table': 'Podcasts',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Rockstar',
            fields=[
                ('rockstarid', models.AutoField(db_column='RockstarId', primary_key=True, serialize=False)),
                ('chapter', models.IntegerField(db_column='Chapter')),
                ('name', models.TextField(blank=True, db_column='Name', null=True)),
                ('linkedin', models.TextField(blank=True, db_column='LinkedIn', null=True)),
                ('description', models.TextField(blank=True, db_column='Description', null=True)),
                ('quote', models.TextField(blank=True, db_column='Quote', null=True)),
                ('img', models.TextField(blank=True, db_column='IMG', null=True)),
            ],
            options={
                'db_table': 'Rockstars',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('tagid', models.AutoField(db_column='TagId', primary_key=True, serialize=False)),
                ('name', models.TextField(blank=True, db_column='Name', null=True)),
            ],
            options={
                'db_table': 'Tags',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Tribe',
            fields=[
                ('tribeid', models.AutoField(db_column='TribeId', primary_key=True, serialize=False)),
                ('name', models.TextField(blank=True, db_column='Name', null=True)),
                ('description', models.TextField(blank=True, db_column='Description', null=True)),
                ('spotify', models.TextField(blank=True, db_column='Spotify', null=True)),
                ('leadaddress', models.TextField(blank=True, db_column='LeadAddress', null=True)),
                ('blocknumber', models.IntegerField(db_column='BlockNumber')),
                ('imagenumber', models.IntegerField(db_column='ImageNumber')),
            ],
            options={
                'db_table': 'Tribes',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('videoid', models.AutoField(db_column='VideoId', primary_key=True, serialize=False)),
                ('title', models.TextField(db_column='Title')),
                ('description', models.TextField(blank=True, db_column='Description', null=True)),
                ('link', models.TextField(blank=True, db_column='Link', null=True)),
                ('datecreated', models.DateTimeField(db_column='DateCreated')),
                ('datemodified', models.DateTimeField(db_column='DateModified')),
                ('datepublished', models.DateTimeField(db_column='DatePublished')),
                ('publishedstatus', models.BooleanField(db_column='PublishedStatus')),
                ('viewcount', models.IntegerField(db_column='ViewCount')),
            ],
            options={
                'db_table': 'Videos',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='OnDemandRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254)),
                ('phone_number', models.CharField(max_length=254)),
                ('date', models.DateTimeField()),
                ('subject', models.CharField(max_length=254)),
            ],
        ),
    ]
