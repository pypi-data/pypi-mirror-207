from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils.translation import gettext as _
# Create your models here.

class Human(models.Model):
    image = models.ImageField(upload_to='humansImages/', default='humansImages/default.webp', verbose_name=_("Your humans image"))
    name = models.TextField(null=True)
    position = models.TextField(null=True)
    smallDescription = RichTextUploadingField(null=True, blank=True)
    description = RichTextUploadingField(null=True, blank=True)
    isPublished = models.BooleanField(default=False, null=True)
    customSlug = models.TextField(blank=False, null=False, verbose_name=_("Custom slug"), unique=True)
    websiteUrl = models.URLField(null=True, blank=True)
    twitterUrl = models.URLField(null=True, blank=True)
    linkedInUrl = models.URLField(null=True, blank=True)
    class Meta:
        verbose_name_plural = "Humans"