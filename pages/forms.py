
from django import forms
from.models import blogs
class blogform(forms.Form):
    subtitle:forms.CharField(max_length=100)
    title = forms.CharField(max_length=100,min_length=5)
    image:forms.ImageField()
    paragraph:forms.CharField(max_length=100)
    btntext:forms.CharField(max_length=100)
   


class blogmodelform(forms.ModelForm):
    class meta:
        model=blogs
        fields=['title','subtitle','paragraph','image']
        widgets ={
            'paragraph': forms.TextInput(attrs={'class':'form-control'}),
            'title':forms.Textarea(attrs={'class':'form-control'}),
           
        }
        labels ={
            'title':'blogtitle',
            'subtitle':'blog subtitle',
            'paragraph':'blog paragraph',
            'image':'blog image',

        }
       