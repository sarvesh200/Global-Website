from django.db import models

from django.contrib.auth.models import User


# one to one relationship

class Userprofileinfo(models.Model):
    user  = models.OneToOneField(User,on_delete = models.CASCADE    )    # Excpet the default one's such as username, password, email, firstname, surname if you want to add some extra feature you can add below.
    portfolio = models.URLField(blank = False)
    profilepic = models.ImageField(upload_to = 'profile_pics',blank = True)

    def __str__(self):
       return self.user.username


'''
# one to many relationship like one company having many cars.
class Company(models.Model):
    pass

class Car(models.Model):
    owningcompany = models.ForignKey(Company,on_delete = models.CASCADE)

    color = models.Charfeild(max_lenght = 256, blank = True)
    modelnumber = models.IntegerField(max_lenght=10, blank = False)




#many to many relationships such as pizza and toppings.
class Toppings(models.Model):
    pass

class Pizza(models.Model):
    toppings = models.ManyToManyField(Toppings)


'''
