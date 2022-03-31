from django.db import models


class OnDemandRequests(models.Model):
    Name = models.CharField(max_length=254)
    PhoneNumber = models.CharField(max_length=254)
    Date = models.DateTimeField()
    Subject = models.CharField(max_length=255)


class Tribes(models.Model):
    Name = models.CharField(max_length=255)
    Description = models.TextField(blank=True, null=True)
    BannerImage = models.CharField(max_length=255, null=True)


class Rockstars(models.Model):
    TribeId = models.ForeignKey(Tribes, on_delete=models.SET_NULL, null=True)
    Name = models.CharField(max_length=255)
    LinkedIn = models.URLField(null=True)
    Description = models.TextField(blank=True, null=True)
    Image = models.CharField(max_length=255, null=True)


class Articles(models.Model):
    TribeId = models.ForeignKey(Tribes, on_delete=models.SET_NULL, null=True)
    RockstarId = models.ForeignKey(Rockstars, on_delete=models.SET_NULL, null=True)
    Name = models.CharField(max_length=255)
    Description = models.TextField(blank=True)
    Image = models.CharField(max_length=255, null=True)
    CreatedAt = models.DateTimeField(auto_now_add=True)
    ModifiedAt = models.DateTimeField(auto_now=True)
    ThumbnailImage = models.CharField(max_length=255, null=True)
    Viewcount = models.PositiveIntegerField(default=0)
