from django import forms
# from .widgets import CustomClearableFileInput
from .models import Course, Category, Comment


class CourseForm(forms.ModelForm):

    class Meta:
        model = Course
        fields = '__all__'

    # image = forms.ImageField(label='Image', required=False, widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-gray rounded'


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)