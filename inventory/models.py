from django.db import models


class Device(models.Model): # name of the table
    type = models.CharField(max_length=100, blank=False) # name of col
    price = models.IntegerField()

    # Restrict the available user choices for device status
    choices = (
        ("AVAILABLE", "Item ready to be purchased"),
        ("SOLD", "Item Sold"),
        ("RESTOCKING", "Item restocking in few days")
    )

    status = models.CharField(max_length=10, choices=choices, default="SOLD") # Available, Sold, Restocking
    issues = models.CharField(max_length=100, default="No issues")


    # Override class meta to make this an abstract class,
    # so django ignores when creating the db
    class Meta:
        abstract = True


    def __str__(self):
        return f"Type: {self.type} \nPrice: {self.price}"


class Laptop(Device):
    pass

class Desktop(Device):
    pass

class Mobile(Device):
    pass
