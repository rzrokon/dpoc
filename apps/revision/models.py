from django.db import models

class Page(models.Model):
    name = models.CharField(max_length=60)
    description = models.TextField()
    
    def __str__(self):
        return self.name


class AutoResponse(models.Model):
    response = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.response


class MatchingText(models.Model):
    auto_response = models.ForeignKey(AutoResponse, null=True, blank=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.title