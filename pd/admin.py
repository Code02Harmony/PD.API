from django.contrib import admin
from .models import Feedback,Prediction
# Register your models here.

admin.site.register(Prediction)
admin.site.register(Feedback)
