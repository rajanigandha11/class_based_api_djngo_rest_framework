from django.contrib import admin
from .models import Student

admin.site.register(Student)

class studentAdmin(admin.ModelAdmin):
	list_display=['id','name','roll','city']
