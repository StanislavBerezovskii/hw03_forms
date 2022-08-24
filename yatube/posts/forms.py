from django import forms

from .models import Post

from django.utils.translation import gettext_lazy as _


class PostForm(forms.ModelForm):
    # Форма для создания поста
    class Meta:
        model = Post
        fields = ('text', 'group',)
        labels = {
            'text': _('Текст'),
            'group': _('Группа'),
        }
        help_texts = {
            'text': _('Подсказка для админа.'),
            'group': _('Подсказка для админа.')
        }
