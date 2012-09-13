from django.contrib import admin

from tasktrack.models import Project, Task

class TaskAdmin(admin.ModelAdmin):
    ordering = ("status", "start_date", "due_date", "id")
    date_hierarchy = "start_date"
    list_display = ("project", "title", "start_date", "due_date", "hours", "status")
    list_display_links = ("project", "title")
    list_editable = ("start_date", "due_date", "hours", "status")
    list_filter = ("project", "status")
    actions_selection_counter = False

    def queryset(self, request):
        qs = super(TaskAdmin, self).queryset(request)
        return qs.exclude(status=Task.STATUS_DONE)

admin.site.register(Project)
admin.site.register(Task, TaskAdmin)

