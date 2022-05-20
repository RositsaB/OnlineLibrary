from django import forms

from online_library.web.models import Profile, Book


class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('first_name', 'last_name', 'image')
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Last Name'}),
            'image': forms.URLInput(attrs={'placeholder': 'URL'}),
        }
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last name',
            'image': 'Image URL',
        }


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('first_name', 'last_name', 'image')
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last name',
            'image': 'Image URL',
    }


class DeleteProfileForm(forms.ModelForm):
    def save(self, commit=True):
        self.instance.delete()
        Book.objects.all().delete()
        return self.instance

    class Meta:
        model = Profile
        fields = ('first_name', 'last_name', 'image')
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last name',
            'image': 'Image URL',
        }


class AddBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('title', 'description', 'image', 'type')
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Title'}),
            'last_name': forms.Textarea(attrs={'placeholder': 'Description'}),
            'image': forms.URLInput(attrs={'placeholder': 'Image'}),
            'type': forms.TextInput(attrs={'placeholder': 'Fiction, Novel, Crime..'})
        }


class EditBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('title', 'description', 'image', 'type')
