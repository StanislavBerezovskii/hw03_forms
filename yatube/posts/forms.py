from django import forms

from django.utils.translation import gettext_lazy as _
# Понятно, что можно и без "_", но так ведь короче :)

from .models import Post


class PostForm(forms.ModelForm):
    # Форма для создания поста
    class Meta:
        model = Post
        fields = ('text', 'group',)
        labels = {
            'text': _('Текст поста'),
            'group': _('Группа поста'),
        }
        help_texts = {
            'text': _('Введите текст поста.'),
            'group': _('Группа поста.')
        }
        error_messages = {
            'text': {
                'not_empty': _('Это поле обязательно для заполнения.'),
            },
        }
