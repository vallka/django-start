from django.db import models

import logging

logger = logging.getLogger(__name__)

# Create your models here.
class Contact(models.Model):
    forename = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)

    def __str__(self):
        return f"{self.forename} {self.surname}: {self.email}"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)  # Call the "real" save() method.    

        logger.info( f"i- Contact saved with id={self.id}.")
        logger.debug( f"d- Contact saved with id={self.id}.")
        logger.error( f"e- Contact saved with id={self.id}.")
