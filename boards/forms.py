from django import forms
from .models import Topic

class NewTopicForm(forms.ModelForm):    # ModelForm is SubClass in DjangoForms Module
    message = forms.charfield(widget=forms.Textarea(attrs={'rows':5 , 'placehplder': 'what on your mind'}),max_length=4000,
        help_text='The max length must be .....')
    class Meta:
        model = Topic
        fields = ['subject' , 'message']


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields=['message',]