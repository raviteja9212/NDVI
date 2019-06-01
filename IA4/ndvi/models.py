import os
from django.db import models
from django.utils import timezone


# RENAMING THE UPLOADED IMAGE
def ndvi_images(instance, filename):
    upload_to = 'ndvi_images'
    ext = filename.split('.')[-1]
    filename = f'{instance.title}_{instance.timestamp}.{ext}'
    return os.path.join(upload_to, filename)


class NDVIModel(models.Model):
    # Input
    title = models.CharField(max_length=50)
    timestamp = models.DateTimeField(default=timezone.now)  # Auto filled
    # Pass to the ndvi_images for renaming and storing
    image = models.ImageField(upload_to=ndvi_images)

    # TAKE THE IMAGE AND RETURN 3 FLOAT VALUES (MIN, MAX and MEAN)
    # Output expected in same table, assigning 0's initially to construct the model
    min_ndvi = models.FloatField(default=0)
    max_ndvi = models.FloatField(default=0)
    avg_ndvi = models.FloatField(default=0)

    # MODEL OBJECT REFERENCE/NAME - ignore this
    def __str__(self):
        return f'{self.title}_{self.timestamp}'

    # THIS IS TO SAVE IN TABLE - ignore this
    def save(self, *args, **kwargs):
        super(NDVIModel, self).save(*args, **kwargs)
