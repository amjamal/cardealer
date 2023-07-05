from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=250, unique=True, blank=False)
    slug = models.SlugField(max_length=250, unique=True)
    description = models.CharField(max_length=300)
    image = models.ImageField(upload_to='category', blank=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def get_url(self):
        return reverse('carapp:cars_by_category', args=[self.slug])

    def __str__(self):
        return '{}'.format(self.name)


class Car(models.Model):
    brand = models.CharField(max_length=250, blank=False)
    name = models.CharField(max_length=250, unique=True, blank=False)
    slug = models.SlugField(max_length=250, unique=True)
    image1 = models.ImageField(upload_to='car')
    image2 = models.ImageField(upload_to='car')
    image3 = models.ImageField(upload_to='car')
    image4 = models.ImageField(upload_to='car')
    description = models.CharField(max_length=250)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    year = models.IntegerField()
    condition = models.CharField(max_length=250)
    availability = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        ordering = ('name',)
        verbose_name = 'car'
        verbose_name_plural = 'cars'

    def get_url(self):
        return reverse('carapp:carDetail', args=[self.category.slug, self.slug])

    def __str__(self):
        return '{}'.format(self.name)


class Booking(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=10, default='+91 ')
    district = models.CharField(max_length=50)
    date = models.DateField()
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=100)

    class Meta:
        ordering = ('name',)
        verbose_name = 'booking'
        verbose_name_plural = 'bookings'


    def __str__(self):
        return '{}'.format(self.name)
