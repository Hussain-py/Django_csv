from django.db import models

# Create your models here.

class keyword_info(models.Model):
    email = models.EmailField()
    number = models.CharField(max_length=20)
    title = models.CharField(max_length=500)

    def __str__(self):
        return self.title

class buisness_leads(models.Model):
    # results = (name, phone_number, address, website, status, rating, url)
    name = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=50)
    website = models.CharField(max_length=50)
    status = models.CharField(max_length=50)
    rating = models.CharField(max_length=500)
    url = models.CharField(max_length=500)

    def __str__(self):
        return self.name
