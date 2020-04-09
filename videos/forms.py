from django import forms
from .models import Video,Comment
class Video_upload_form(forms.ModelForm):
    class Meta:
        model = Video
        fields = ["title","description","video_url"]
        widgets = {
            "title" : forms.TextInput(attrs={"class":"form-control border-primary","placeholder":"Name of Video"}),
            "description" : forms.Textarea(attrs={"class":"form-control border-primary","rows":4,"placeholder":"About the Video"}),
            'video_url' : forms.TextInput(attrs={'class':"form-control border-primary","placeholder":"Youtube url of The video"})
        }
    
class  Comment_form(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['description']
        widgets = {
            "description" : forms.Textarea(attrs={"class":"form-control","rows":4})
        }
        