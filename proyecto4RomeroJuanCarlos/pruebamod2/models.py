from django.db import models


class Publication(models.Model):
    title = models.CharField(max_length=30)

    class Meta:
        db_table = 'Publication'
        verbose_name = 'Publication'
        ordering=['id']#Si ponemos '-id' lo ordena de manera descendiente

    def __str__(self):
        return self.title


class Noticia(models.Model):
    headline = models.CharField(max_length=100)
    publications = models.ManyToManyField(Publication)

    class Meta:
        db_table = 'Noticia'
        verbose_name = 'Noticia'
        ordering=['headline']#Si ponemos '-id' lo ordena de manera descendiente

    def __str__(self):
        return self.headline