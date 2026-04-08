from django.db import models

class Facilities(models.Model):

    FACILITY_TYPES = [
        ('public', 'Public'),
        ('private', 'Private'),
        ('pharmacy', 'Pharmacy'),
    ]

    facility_id = models.AutoField(primary_key=True)
    provider = models.ForeignKey(
        'providers.Providers',  
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='facilities'
    )
    facility_name = models.CharField(max_length=100, blank=False)
    facility_address = models.CharField(max_length=200, blank=True)
    facility_city = models.CharField(max_length=100, blank=False)
    facility_state = models.CharField(max_length=100, blank=False)
    facility_type = models.CharField(max_length=20, choices=FACILITY_TYPES, default='private')
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    is_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.facility_name

    class Meta:
        verbose_name_plural = 'Facilities'
