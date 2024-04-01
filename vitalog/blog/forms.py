from django import forms
from cloudinary.forms import CloudinaryFileField
from .models import Post


class PostForm(forms.ModelForm):
    image = CloudinaryFileField()

    class Meta:
        model = Post
        fields = '__all__'

    def __init__(self, *args, **kwargs):
       super().__init__(*args, **kwargs)
       self.fields['image'].options={
           'tags': 'new_image',
           'format': 'png'
    }