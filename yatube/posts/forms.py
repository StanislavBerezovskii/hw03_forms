from django import forms

from .models import Post


class PostForm(forms.ModelForm):
    # Форма для создания поста
    class Meta:
        model = Post
        fields = ('text', 'group',)
        labels = {
            'text': 'Текст поста',
            'group': 'Группа',
        }
        help_texts = {
            'text': 'Какая-то подсказка для админа.',
            'group': 'Группа',
        }
