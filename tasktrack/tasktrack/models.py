from django.conf import settings
from django.contrib import admin
from django.db import models

class Project(models.Model):
    name = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name

class Task(models.Model):
    STATUS_TODO = 0
    STATUS_ACTIVE = 100
    STATUS_DEFERRED = 200
    STATUS_OUTOFSCOPE = 300
    STATUS_DONE = 400
    STATUS_CHOICES = (
        (STATUS_TODO, "Todo"),
        (STATUS_ACTIVE, "Active"),
        (STATUS_DEFERRED, "Deferred"),
        (STATUS_OUTOFSCOPE, "Out of Scope"),
        (STATUS_DONE, "Complete"),

    )
    project = models.ForeignKey("Project")
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    start_date = models.DateField(blank=True, null=True)
    due_date = models.DateField(blank=True, null=True)
    hours = models.CharField(max_length=255, blank=True)
    status = models.IntegerField(choices=STATUS_CHOICES, default=STATUS_TODO)

    def __unicode__(self):
        return self.title
