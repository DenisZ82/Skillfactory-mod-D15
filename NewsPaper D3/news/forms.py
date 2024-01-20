from django import forms
from django.core.exceptions import ValidationError
from .models import Post, Author
from django_filters import ModelMultipleChoiceFilter


class PostForm(forms.ModelForm):
    # author = ModelMultipleChoiceFilter(
    #     field_name='author__author_id',
    #     queryset=Author.objects.all()
    # )

    class Meta:
        model = Post
        # fields = '__all__'
        fields = [
            'author',
            'category_post_many',
            'title',
            'text'
        ]

    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get('title')
        text = cleaned_data.get('text')
        if title is not None and len(title) > 128:
            raise ValidationError({
                'title': 'Название не может превышать 128 символа.'
            })
        if title == text:
            raise ValidationError({
                'text': 'Содержание названия и текста статьи/новости не должно совпадать.'
            })
        return cleaned_data
