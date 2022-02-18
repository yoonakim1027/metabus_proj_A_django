from django.contrib import admin
from streetanimal.models import Animal, Category


@admin.register(Animal)
class AnimalAdmin(admin.ModelAdmin):
    list_display = ["animal_no", "animal_reg_num", "category", "sex", "date_of_discovery", "start_date", "end_date"]
    list_display_links = ["animal_reg_num"]
    search_fields = ["animal_reg_num"]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name"]
    list_display_links = ["name"]
    search_fields = ["name"]

