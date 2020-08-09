from django.contrib import admin
from model_market.models import PreModel, Task, Framework

# Register your models here.
class TaskInline(admin.StackedInline):
    model = PreModel
    extra = 2
    
@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    inlines = (TaskInline, )
    list_display = ('id', 'name', 'description')

@admin.register(Framework)
class FrameWorkAdmin(admin.ModelAdmin):
    # inlines = (FrameWorkInline, )
    list_display = ('id', 'name', 'description')

@admin.register(PreModel)
class ModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'upload_date')

