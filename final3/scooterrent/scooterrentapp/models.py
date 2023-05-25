from django.db import models
from django.utils import timezone


ID_PROOF_CHOICES = (
    ('driving_license', 'Driving License'),
    ('aadhar', 'Aadhar'),
)

class Scooter(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='scooters/')
    kilometer_range = models.IntegerField()
    price = models.IntegerField()

    def __str__(self):
        return self.name


class Booking(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    mobile_number = models.CharField(max_length=10)
    permanent_address = models.TextField()
    id_proof_type = models.CharField(max_length=50, choices=ID_PROOF_CHOICES)
    id_proof_image = models.ImageField(upload_to='id_proof_images')
    id_proof_number = models.CharField(max_length=50)
    rider_image = models.ImageField(upload_to='rider_images')
    scooter = models.ForeignKey(Scooter, on_delete=models.CASCADE)
    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField()

    def __str__(self):
        local_start_date = timezone.localtime(self.start_datetime).date()
        local_end_date = timezone.localtime(self.end_datetime).date()
        return f'{self.name} - {self.scooter.name} ({local_start_date} to {local_end_date})'

        
