from django.db import models

# Create your models here.


class Blogs(models.Model):
    title = models.CharField(verbose_name="title", max_length=250, null=True)
    description = models.TextField(
        verbose_name="description", null=True, blank=True)
    image = models.ImageField(verbose_name="image", null=True, blank=True)

    date_created = models.DateTimeField(
        verbose_name="date_created", auto_now_add=True, null=True)
    date_updated = models.DateTimeField(
        verbose_name="date_updated", auto_now=True, null=True)

    def __str__(self):
        return self.title

    def get_image(self):
        return 'img/' + str(self.image)
