from django.contrib import admin
from .models import Article,Category,Comment,Tag

admin.site.register(Article)
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Tag)
# Register your models here.
