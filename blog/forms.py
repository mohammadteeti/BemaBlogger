from django import forms

class CommentForm(forms.Form):
    author=forms.CharField(max_length=20,
                           widget=forms.TextInput(
                               attrs={
                                   "class":"form-control",
                                   "placeholder":"Your Name Here!"
                               }
                           ))
    
    body =forms.CharField(max_length=500,
        widget=forms.TextInput(attrs={
            "class":"form-control",
            "placeholder":"Comment Here! max 500 characters"
        }))
    
    