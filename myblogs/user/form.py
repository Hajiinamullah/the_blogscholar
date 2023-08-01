from django import forms
from django.contrib.auth.forms import PasswordChangeForm

class CustomPasswordChangeForm(PasswordChangeForm):
    username = forms.CharField()

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        old_password = cleaned_data.get('old_password')

        user = self.user
        if user.username != username or not user.check_password(old_password):
            raise forms.ValidationError("Invalid username or old password.")
        return cleaned_data
