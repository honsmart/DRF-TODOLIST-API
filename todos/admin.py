from django.contrib import admin
from todos.models import Todo

class TodoAdmin(admin.ModelAdmin):

    list_display = ('title','desc', 'is_complete', 'owner')
    search_fields = ('title','desc', 'is_complete', 'owner')
    list_per_page =25

# Register your models here.
admin.site.register(Todo, TodoAdmin)