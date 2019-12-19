from django import forms
from api.models import *
from django.contrib.auth.forms import UserCreationForm


class DeviceForm(forms.ModelForm):
    def clean(self):
        device_id = self.cleaned_data.get('device_id')
        device_cnt=IrrigaiaDeviceModel.objects.filter(device_id=device_id).count()
        if device_cnt == 0:
            raise forms.ValidationError("ouaaaa")
        return self.cleaned_data
    class Meta:
        model = IrrigaiaDeviceModel
        fields = ['device_id']
        labels = {
            'device_id': ('Identifiant irrigaia'),
        }

        error_messages = {
            'device_id': {
                'max_length': ("erreur appairage"),
            },
        }
class UserProfileForm(forms.ModelForm):

    class Meta:
        model = UserProfileModel
        fields = [ 'nickname','bio','avatar']


    # clean email field
    def clean_email(self):
        email = self.cleaned_data["email"]
        try:
            User._default_manager.get(email=email)
        except User.DoesNotExist:
            return email
        raise forms.ValidationError('duplicate email')

    # modify save() method so that we can set user.is_active to False when we first create our user
    def save(self, commit=True):
        user = super(UserProfileForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.is_active = False  # not active until he opens activation link
            user.save()

        return user