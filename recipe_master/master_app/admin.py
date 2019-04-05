from django.contrib import admin
from .models import Recipe, Review
# Register your models here.

#To ciew the model/filter options in admin
class ReviewAdmin(admin.ModelAdmin):
    model = Review
    list_display= ('recipe', 'rating', 'authenticityRating' ,'comment', 'user')
    list_filter = ['user', 'rating']
    search_fields = ['comment']
    
admin.site.register(Recipe)
admin.site.register(Review,ReviewAdmin)