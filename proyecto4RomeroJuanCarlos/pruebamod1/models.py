from django.db import models

# Create your models here.
class Reporter(models.Model):
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)
    email=models.EmailField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    class Meta:
        db_table = 'reportero'
        verbose_name = 'Reportero'
        ordering=['-id']#Si ponemos '-id' lo ordena de manera descendiente
    
class Article(models.Model):
    headline = models.CharField(max_length=100)
    pub_date = models.DateField()
    reporter = models.ForeignKey(Reporter, on_delete=models.CASCADE)

    def __str__(self):
        return self.headline
    class Meta:
        db_table = 'articulo'
        verbose_name = 'Articulo'
        ordering=['headline']#Si ponemos '-id' lo ordena de manera descendiente