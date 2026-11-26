from django.contrib import admin

from cases.models import Case


# Register your models here.
@admin.register(Case)
class CaseAdmin(admin.ModelAdmin):
    list_display = ["number", "title", "status", "filed_on"]
    list_filter = ["status"]
    search_fields = ["number", "title"]
