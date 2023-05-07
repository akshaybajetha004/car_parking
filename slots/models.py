from django.db import models
from datetime import datetime


class ParkingSlot(models.Model):
    date = models.DateField()
    time = models.TimeField()
    is_available = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=datetime.now)
    updated_at = models.DateTimeField(default=datetime.now)


class ParkingSlotSpace(models.Model):
    is_booked = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=datetime.now)
    updated_at = models.DateTimeField(default=datetime.now)
    start_time = models.DateTimeField(default=datetime.now)
    end_time = models.DateTimeField(default=datetime.now)
    parking_slot = models.ForeignKey(ParkingSlot, on_delete=models.CASCADE)
    # user = models.ForeignKey(User, on_delete=models.CASCADE)


class VehicleType(models.Model):
    name = models.CharField(max_length=255)

# how to make an entry in VehicleType DB
# car_type = VehicleType.objects.create(name='Car')
# bus_type = VehicleType.objects.create(name='Bus')
# bike_type = VehicleType.objects.create(name='Bike')


class Vehicle(models.Model):
    type = models.ForeignKey(VehicleType, on_delete=models.CASCADE)
    vehicle_no = models.CharField(max_length=10, null=False, blank=False)
    # user = models.ForeignKey(User, on_delete=models.CASCADE)

# how to make an entry in Vehicle DB
# car = Vehicle.objects.create(type=car_type)
# bus = Vehicle.objects.create(type=bus_type)
# bike = Vehicle.objects.create(type=bike_type)


class Wallet(models.Model):
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)


class Ledger(models.Model):
    wallet = models.ForeignKey(Wallet, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False)
    credited = models.BooleanField(default=False)
    debited = models.BooleanField(default=False)
    time = models.DateTimeField(default=datetime.now)

