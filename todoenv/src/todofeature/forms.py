from django import forms
from todofeature.models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = "__all__"
        
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs["class"] = "form-control"
            
        # widgets = {
        #     'name' : (forms.TextInput(attrs={'class':'form-control'})),
        #     'description' : (forms.Textarea(attrs={'class':'form-control','row':3,'placeholder':'description'})),
        #     'image' : (forms.FileInput(attrs={'class':'form-control'})),
        #     'task_data' : (forms.SelectDateWidget()),
        #     'priority' : (forms.Select(attrs={'class':'form-control'})),
        #     'Category' : (forms.Select(attrs={'class':'form-control'})),
        #     'labels' : (forms.CheckboxInput(attrs={'class':'form-control'})),
        # }
        #exclude = ("image",) -> excludes image and loads evertything except image
        
    def clean_name(self):
        name = self.cleaned_data.get("name")
        if name.isdigit():
            raise forms.ValidationError("Name cannot be number")
        return name
        