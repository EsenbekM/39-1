from django import forms

from post.models import Post


class PostForm(forms.Form):
    title = forms.CharField(max_length=100, min_length=5)
    text = forms.CharField(widget=forms.Textarea)
    image = forms.ImageField(required=False)
    rate = forms.FloatField()

    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get('title')
        text = cleaned_data.get('text')

        if title and text and title.lower() == text.lower():
            raise forms.ValidationError('Заголовок и текст не должны совпадать')
        return cleaned_data

    def clean_title(self):
        title = self.cleaned_data['title']
        if 'python' in title.lower():
            raise forms.ValidationError('Слово "python" недопустимо в заголовке')
        return title
    
    def clean_rate(self):
        rate = self.cleaned_data['rate']
        if rate < 0:
            raise forms.ValidationError('Оценка не может быть отрицательной')
        return rate


class PostForm2(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'text', 'image', 'rate', 'tags']
        # exclude = ['rate']
        widgets = {
            'text': forms.Textarea(
                attrs={
                    'placeholder': 'Введите текст',
                    'rows': 5,
                    'cols': 30,
                    'class': 'form-control'
                }
            ),
            'title': forms.TextInput(
                attrs={
                    'placeholder': 'Введите заголовок',
                    'class': 'form-control'
                }
            ),
            'rate': forms.NumberInput(
                attrs={
                    'placeholder': 'Введите оценку',
                    'class': 'form-control'
                }
            ),
            'image': forms.ClearableFileInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'tags': forms.SelectMultiple(
                attrs={
                    'class': 'form-control'
                }
            )
        }
        
    
    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get('title')
        text = cleaned_data.get('text')

        if title and text and title.lower() == text.lower():
            raise forms.ValidationError('Заголовок и текст не должны совпадать')
        return cleaned_data

    def clean_title(self):
        title = self.cleaned_data['title']
        if 'python' in title.lower():
            raise forms.ValidationError('Слово "python" недопустимо в заголовке')
        return title
    
    def clean_rate(self):
        rate = self.cleaned_data['rate']
        if rate < 0:
            raise forms.ValidationError('Оценка не может быть отрицательной')
        return rate
    