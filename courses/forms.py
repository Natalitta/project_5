from django import forms
from .models import Course, Category, Comment


class CourseForm(forms.ModelForm):

    class Meta:
        model = Course
        fields = '__all__'

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
        fields = ('body', 'image')

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.fields['body'].label = 'Tell us what you think about the course.'
        self.fields['image'].label = 'You can share your course art.'
        self.fields['image'].widget.attrs['accept'] = 'image/*'