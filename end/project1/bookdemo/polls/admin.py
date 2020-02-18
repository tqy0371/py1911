from django.contrib import admin

# Register your models here.
from .models import *

class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 1

class QuertionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]

class ChoiceAdmin(admin.ModelAdmin):
    pass

admin.site.register(Question,QuertionAdmin)
admin.site.register(Choice,ChoiceAdmin)
admin.site.register(User)
