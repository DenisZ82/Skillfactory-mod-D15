from django.contrib import admin
from .models import Post, Comment, Category, Author, Subscription, PostCategory
from modeltranslation.admin import TranslationAdmin  # импортируем модель амдинки
# (вспоминаем модуль про переопределение стандартных админ-инструментов)

# Регистрируем модели для перевода в админке


class CategoryTrAdmin(TranslationAdmin):
    model = Category


class PostTrAdmin(TranslationAdmin):
    model = Post


class PostAdmin(admin.ModelAdmin):
    def subject_post(self, obj):
        return ', '.join([category.name for category in obj.category_post_many.all()])

    # list_display = [field.name for field in Post._meta.get_fields()]
    # list_display = list_display[2:7]
    list_display = ('author', 'category_post', 'time_in', 'title', 'rating', 'subject_post')
    list_filter = ('author', 'category_post', 'rating', 'category_post_many__name')
    search_fields = ('author__user__username', 'category_post', 'title', 'category_post_many__name',)


admin.site.register(Category)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
admin.site.register(Author)
admin.site.register(Subscription)
admin.site.register(PostCategory)

# Register your models here.
