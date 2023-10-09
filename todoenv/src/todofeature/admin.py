from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from todofeature.models import Task,Category,Label
from django.contrib.auth import get_user_model

User = get_user_model()

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    pass

# Register your models here.
@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("name", "priority", "task_date", "category", "is_done", )
    list_filter = ("priority", )
    search_fields = ("name","category__name", )
    
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", )


@admin.register(Label)
class LabelAdmin(admin.ModelAdmin):
    list_display = ("name", )