from django.db import models


# Create your models here.

class TranslationResponse(models.Model):
    source = models.CharField(max_length=10)
    confidence = models.FloatField()
    translation = models.TextField()
    destination = models.CharField(max_length=10)

    def get_source(self):
        return self.source

    def get_confidence(self):
        return self.confidence

    def get_translation(self):
        return self.translation

    def get_destination(self):
        return self.destination

    def set_source(self, source):
        self.source = source

    def set_confidence(self, confidence):
        self.confidence = confidence

    def set_translation(self, translation):
        self.translation = translation

    def set_destination(self, destination):
        self.destination = destination
