from django.contrib import admin
from .models import Post, Comment, Category, Author, Subscription, PostCategory

admin.site.register(Category)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Author)
admin.site.register(Subscription)
admin.site.register(PostCategory)

# Register your models here.
