         ### This is your necessary model implemented into clustering.py ###






"""from django.db import models



# Create your models here.
from django.contrib.auth.models import User
class Cluster(models.Model):
    user=models.ForeignKey(User,onfrom django.db import models



# Create your models here.
from django.contrib.auth.models import User
class Cluster(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    cluster_name= models.CharField(max_length=50,blank=True)

    def __str__(self):
        return str(self.user)
"""