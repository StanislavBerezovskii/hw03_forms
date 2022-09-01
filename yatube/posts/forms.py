from django import forms

from django.utils.translation import gettext_lazy as _

from .models import Post, Group


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
            'group': _('Выберите группу для поста.')
        }
        error_messages = {
            'text': {
                'required': _('Это поле обязательно для заполнения.'),
            },
        }
        widgets = {
            'text': forms.Textarea(attrs={'cols': 97, 'rows': 8}),
            'group': forms.Select(class= "form-control", id="id_group", choices=Group.objects.all()[:10]),
        }
