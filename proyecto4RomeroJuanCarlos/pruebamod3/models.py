from django.db import models


class Place(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=80)

    def __str__(self):
        return f"{self.name} the place"
    class Meta:
        db_table = 'Place'
        verbose_name = 'Place'
        ordering=['id']#Si ponemos '-id' lo ordena de manera descendiente


class Restaurant(models.Model):
    place = models.OneToOneField(
        Place,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    serves_hot_dogs = models.BooleanField(default=False)
    serves_pizza = models.BooleanField(default=False)

    def __str__(self):
        return "%s the restaurant" % self.place.name
    class Meta:
        db_table = 'Restaurant'
        verbose_name = 'Restaurant'
        ordering=['place']#Si ponemos '-id' lo ordena de manera descendiente

class Waiter(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

    def __str__(self):
        return "%s the waiter at %s" % (self.name, self.restaurant)
    class Meta:
        db_table = 'Waiter'
        verbose_name = 'Waiter'
        ordering=['id']#Si ponemos '-id' lo ordena de manera descendiente