from django.contrib import admin
from .models import Spot
from import_export.admin import ExportActionModelAdmin, ImportExportMixin, ImportMixin
# Register your models here.
class SpotAdmin(ImportExportMixin, admin.ModelAdmin):
    pass

admin.site.register(Spot, SpotAdmin)