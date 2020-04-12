from django.db import models
from django.utils import timezone
from datetime import datetime



class Forms(models.Model):
    form_title = models.CharField(max_length=200)
    form = models.FileField(upload_to='files/%Y/%m/%d/', blank=True)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    is_published=models.BooleanField(default=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
            return self.form_title

class Record_log(models.Model):
    form_name= models.CharField(max_length=50)
    form_id=models.IntegerField()
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=100)
    employee_id=models.CharField(max_length=50)
    phone=models.CharField(max_length=50)
    upload_form=models.FileField(upload_to='uploadedfiles/%Y/%m/%d/', blank=True)
    comments=models.TextField()
    uploaded_date=models.DateTimeField(default=datetime.now, blank=True)
    #user_id=models.IntegerField()
    def __str__(self):
        return self.name

class Station(models.Model):
    station_name=models.CharField(max_length=100)
    Street=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=100)
    def __str__(self):
        return self.station_name



class Record(models.Model):
    #supervisor=models.ForeignKey(Supervisor, on_delete=models.DO_NOTHING())
    name=models.CharField(max_length=50)
    #employee_id = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    #user_id = models.IntegerField(blank=True)
    form_name = models.CharField(max_length=50)
    #form_id=models.IntegerField(blank=True)
    status=models.CharField(max_length=50)
    supervisor_comments=models.TextField()
    created_date=models.DateTimeField(default=datetime.now, blank=True)
    def __str__(self):
        return self.name








