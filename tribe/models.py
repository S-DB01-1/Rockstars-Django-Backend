from django.db import models


class OnDemandRequest(models.Model):
    name = models.CharField(max_length=254)
    phone_number = models.CharField(max_length=254)
    date = models.DateTimeField()
    subject = models.CharField(max_length=254)


class Tag(models.Model):
    tagid = models.AutoField(db_column='TagId', primary_key=True)
    name = models.TextField(db_column='Name', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Tags'


class Tribe(models.Model):
    tribeid = models.AutoField(db_column='TribeId', primary_key=True)
    tag = models.ForeignKey(Tag, models.CASCADE, db_column='TagId', blank=True, null=True)
    name = models.TextField(db_column='Name', blank=True, null=True)
    description = models.TextField(db_column='Description', blank=True, null=True)
    spotify = models.TextField(db_column='Spotify', blank=True, null=True)
    leadaddress = models.TextField(db_column='LeadAddress', blank=True, null=True)

    # blocknumber = models.IntegerField(db_column='BlockNumber')
    # imagenumber = models.IntegerField(db_column='ImageNumber')

    class Meta:
        managed = False
        db_table = 'Tribes'


class Rockstar(models.Model):
    rockstarid = models.AutoField(db_column='RockstarId', primary_key=True)
    tribe = models.ForeignKey('Tribe', models.CASCADE, db_column='TribeId', blank=True, null=True)
    chapter = models.IntegerField(db_column='Chapter')
    name = models.TextField(db_column='Name', blank=True, null=True)
    linkedin = models.TextField(db_column='LinkedIn', blank=True, null=True)
    description = models.TextField(db_column='Description', blank=True, null=True)
    quote = models.TextField(db_column='Quote', blank=True, null=True)
    img = models.TextField(db_column='IMG', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Rockstars'


class ArticleText(models.Model):
    articletextblockid = models.TextField(db_column='ArticleTextBlockId', primary_key=True)
    article = models.ForeignKey('Article', models.CASCADE, db_column='ArticleId', blank=True, null=True)
    text = models.TextField(db_column='Text', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ArticleTextBlocks'


class Article(models.Model):
    articleid = models.AutoField(db_column='ArticleId', primary_key=True)
    rockstar = models.ForeignKey('Rockstar', models.CASCADE, db_column='RockstarId', blank=True, null=True)
    title = models.TextField(db_column='Title', blank=True, null=True)
    description = models.TextField(db_column='Description', blank=True, null=True)
    tribe = models.ForeignKey('Tribe', models.CASCADE, db_column='TribeId', blank=True, null=True)
    datecreated = models.DateTimeField(db_column='DateCreated')
    datemodified = models.DateTimeField(db_column='DateModified')
    datepublished = models.DateTimeField(db_column='DatePublished')
    publishedstatus = models.BooleanField(db_column='PublishedStatus')
    viewcount = models.IntegerField(db_column='ViewCount')

    class Meta:
        managed = False
        db_table = 'Article'


class ArticleImage(models.Model):
    articleimageid = models.AutoField(db_column='ArticleImageId', primary_key=True)
    article = models.ForeignKey(Article, models.CASCADE, db_column='ArticleId', blank=True, null=True)
    url = models.TextField(db_column='URL', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ArticleImages'


class PodcastEpisodes(models.Model):
    podcastepisodeid = models.AutoField(db_column='PodcastEpisodeId', primary_key=True)
    title = models.TextField(db_column='Title', blank=True, null=True)
    description = models.TextField(db_column='Description', blank=True, null=True)
    url = models.TextField(db_column='URL', blank=True, null=True)
    datecreated = models.DateTimeField(db_column='DateCreated')
    datemodified = models.DateTimeField(db_column='DateModified')
    datepublished = models.DateTimeField(db_column='DatePublished')
    publishedstatus = models.BooleanField(db_column='PublishedStatus')
    viewcount = models.IntegerField(db_column='ViewCount')
    rockstar = models.ForeignKey('Rockstar', models.CASCADE, db_column='RockstarId', blank=True, null=True)
    tribe = models.ForeignKey('Tribe', models.CASCADE, db_column='TribeId', blank=True, null=True)
    podcast = models.ForeignKey('Podcast', related_name='episodes', on_delete=models.CASCADE, db_column='PodcastId', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'PodcastEpisodes'

class Podcast(models.Model):
    podcastid = models.AutoField(db_column='PodcastId', primary_key=True)
    title = models.TextField(db_column='Title', blank=True, null=True)
    description = models.TextField(db_column='Description', blank=True, null=True)
    spotifyurl = models.TextField(db_column='URL', blank=True, null=True)
    datecreated = models.DateTimeField(db_column='DateCreated')
    datemodified = models.DateTimeField(db_column='DateModified')
    datepublished = models.DateTimeField(db_column='DatePublished')
    publishedstatus = models.BooleanField(db_column='PublishedStatus')
    viewcount = models.IntegerField(db_column='ViewCount')
    tribe = models.ForeignKey('Tribe', models.CASCADE, db_column='TribeId', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Podcasts'


class Video(models.Model):
    videoid = models.AutoField(db_column='VideoId', primary_key=True)
    title = models.TextField(db_column='Title')
    description = models.TextField(db_column='Description', blank=True, null=True)
    link = models.TextField(db_column='Link', blank=True, null=True)
    linktype = models.IntegerField(db_column='LinkType', blank=True, null=True)
    datecreated = models.DateTimeField(db_column='DateCreated')
    datemodified = models.DateTimeField(db_column='DateModified')
    datepublished = models.DateTimeField(db_column='DatePublished')
    publishedstatus = models.BooleanField(db_column='PublishedStatus')
    viewcount = models.IntegerField(db_column='ViewCount')
    tribe = models.ForeignKey('Tribe', models.CASCADE, db_column='TribeId', blank=True, null=True)
    rockstar = models.ForeignKey('Rockstar', models.CASCADE, db_column='RockstarId', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Videos'

    def get_link(self):
        if self.linktype == 0:
            return 'https://youtube.com/' + self.link
        if self.linktype == 1:
            return 'https://vimeo.com/' + self.link
