'''
 in this class, there are few assumptions assumed in designing table "Car_Rental".
 #1 -> name of table that car_Rental references is "Location".
 #2 -> the foreign key is assumed to be of type CharField (although this is not an issue).
'''

from django.db        import models

from Profile.models   import User
from Countries.models import locations

# Create your models here.
#class representing table for car rentals services
class Car_Rental (models.Model):


    # setting fields of the table
    car_rental_id = models.CharField(max_length=15)
    car_rental_name = models.CharField(max_length=45)
    location_ID = models.ForeignKey(locations)

    def __str__(self):
        return self.rental_id

class Car_Reservation(models.Model):

    reservation_id = models.AutoField(primary_key=True)
    rental_id = models.ForeignKey(Car_Rental)
    user_id = models.ForeignKey(User)
    pick_up = models.CharField(max_length = 200)
    drop_off = models.CharField(max_length = 200)
    def __str__(self):
        return self.reservation_id
