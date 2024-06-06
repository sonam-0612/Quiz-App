from django.contrib import admin
from . import models
# Register your models here.

admin.site.register(models.QuizCategory)
admin.site.register(models.QuizResult)

class QuizQuestionAdmin(admin.ModelAdmin):
    list_display=['question','level']
admin.site.register(models.QuizQuestion)
# admin.site.register(admin.QuizQuestionAdmin)

