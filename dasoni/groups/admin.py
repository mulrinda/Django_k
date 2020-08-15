from django.contrib import admin
from import_export.admin import ExportActionModelAdmin, ImportExportMixin, ImportMixin
from .models import Star, Visit
# Register your models here.
class StarAdmin(ImportExportMixin, admin.ModelAdmin):
    pass
class VisitAdmin(ImportExportMixin, admin.ModelAdmin):
    pass

admin.site.register(Star, StarAdmin)
admin.site.register(Visit, VisitAdmin)