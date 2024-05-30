from django.db import models

# Create your models here.

class ContactModel(models.Model):
  auto_field = models.AutoField(primary_key=True)
  name = models.CharField(max_length=20)
  email_field = models.EmailField()
  bio=models.TextField()
  last_modified = models.DateTimeField()
  big_integer_field = models.BigIntegerField()
  date_field = models.DateField()
  date_time_field = models.DateTimeField()
  decimal_field = models.DecimalField(max_digits=5, decimal_places=2)
  duration_field = models.DurationField()
  float_field = models.FloatField()
  generic_ip_address_field = models.GenericIPAddressField()
  integer_field = models.IntegerField()
  slug_field = models.SlugField()
  time_field = models.TimeField()
  url_field = models.URLField()
  uuid_field = models.UUIDField()
  aggree=models.BooleanField()
 