from django.conf import settings
from django.contrib import admin
from django.db import models

class Project(models.Model):
    name = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name

class Task(models.Model):
    project = models.ForeignKey("Project")
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    start_date = models.DateField(blank=True)
    due_date = models.DateField(blank=True)

    def __unicode__(self):
        return self.title


class TaskAdmin(admin.ModelAdmin):
    ordering = ("start_date", "due_date")
    date_hierarchy = "start_date"
    list_display = ("project", "title", "start_date", "due_date")
    list_display_links = ("project", "title")
    list_editable = ("start_date", "due_date")
    list_filter = ("project",)
    actions_selection_counter = False

admin.site.register(Project)
admin.site.register(Task, TaskAdmin)

