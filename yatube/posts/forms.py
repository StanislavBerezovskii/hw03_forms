from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    # Форма для создания поста
    class Meta:
        model = Post
        fields = ('text', 'group',)

    def clean_data(self):
        data = self.cleaned_data['text']
        if data == '':
            return forms.ValidationError(
                'Это поле обязательно для заполнения.')
        return data
