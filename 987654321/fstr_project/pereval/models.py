from django.db import models  

class Coords(models.Model):  
    latitude = models.FloatField()  
    longitude = models.FloatField()  
    height = models.FloatField()  

    def __str__(self):  
        return f"Coords({self.latitude}, {self.longitude}, {self.height})"  

class Pereval(models.Model):  
    STATUS_CHOICES = [  
        ('active', 'Active'),  
        ('inactive', 'Inactive'),  
        ('new', 'New'),  
        ('pending', 'Pending'),  
        ('accepted', 'Accepted'),  
        ('rejected', 'Rejected'),  
    ]  
    
class Pereval(models.Model): 
    beauty_title = models.CharField(max_length=255)  
    title = models.CharField(max_length=255)  
    other_titles = models.TextField()  
    connect = models.CharField(max_length=255)  
    coord = models.OneToOneField(Coords, on_delete=models.CASCADE)  
    status = models.CharField(max_length=50)   
    
    def __str__(self):  
        return self.title