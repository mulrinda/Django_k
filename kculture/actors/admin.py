from django.contrib import admin
from .models import Actor, Drama
from import_export.admin import ExportActionModelAdmin, ImportExportMixin, ImportMixin
# Register your models here.
class ActorAdmin(ImportExportMixin, admin.ModelAdmin):
    pass

class DramaAdmin(ImportExportMixin, admin.ModelAdmin):
    pass

admin.site.register(Actor, ActorAdmin)
admin.site.register(Drama, DramaAdmin)