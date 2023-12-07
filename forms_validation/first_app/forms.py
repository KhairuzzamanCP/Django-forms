from django import forms
from django.core import validators

class contactFrom(forms.Form):
    name = forms.CharField(label='Full Name:', initial='Rahim', help_text='total lenght must be 70 chartears', required= False, disabled=True)
    # file = forms.FileField()
    # email = forms.EmailField(label= 'User Email')
    # Age = forms.IntegerField()
    # weaight = forms.FloatField()
    # balance = forms.DecimalField()
    brithday = forms.DateField(widget=forms.DateInput(attrs={'type':'date'})) 
    appoinment = forms.DateTimeField(widget=forms.DateInput(attrs={'type':'datetime-local'})) 
    CHOICES = [('S','Small'),('M','Medium'),('L','Large')]
    size = forms.ChoiceField(choices = CHOICES ,widget=forms.RadioSelect)
    MEAL = [('P','Paperoni'),('M','Masroom'), ('B','Beef')]
    pizza = forms.MultipleChoiceField(choices=MEAL, widget=forms.CheckboxSelectMultiple)
    # check = forms.BooleanField()
    
    
# class StudenData(forms.Form):
#     name = forms.CharField(widget= forms.TextInput)
#     email = forms.CharField(widget= forms.EmailInput)
    # def clean_name(self):
    #     valname = self.cleaned_data['name']
    #     if len(valname) <10:
    #         raise forms.ValidationError('Enter a name at lest must be 10 chartres')
    #     return valname
    # def clean_email(self):
    #     valemail = self.cleaned_data['email']
    #     if '.com' not in valemail:
    #         raise forms.ValidationError('Your email content must .com')
    #     return valemail
    # def clean(self):
    #     clean_data = super().clean()
    #     valname = self.cleaned_data['name']
    #     valemail = self.cleaned_data['email']
    #     if len(valname) <10:
    #         raise forms.ValidationError('Enter a name at lest must be 10 chartres')
    #     if '.com' not in valemail:
    #         raise forms.ValidationError('Your email content must .com')
        
        
class StudenData(forms.Form):
    name = forms.CharField(widget=forms.TextInput, validators=[validators.MinLengthValidator(10, message='Enter a name at lest must be 10 chartres')])
    email = forms.CharField(widget= forms.EmailInput, validators=[validators.EmailValidator(message='Enter your vaild email')])
    Age = forms.IntegerField(validators=[validators.MaxValueValidator(34, message='max age must be 34'), validators.MinValueValidator(24, message= 'min age best be 24')])
    file = forms.FileField(validators=[validators.FileExtensionValidator(allowed_extensions=['pdf','png'], message='file extension must be ended ended with .pdf and .png' )])
    
class passwordValidationProjects(forms.Form):
    name = forms.CharField(widget= forms.TextInput)
    password = forms.CharField(widget= forms.PasswordInput)
    confirm_password = forms.CharField(widget= forms.PasswordInput)
    def clean(self):
        clean_data = super().clean()
        val_name = self.cleaned_data['name']
        val_pass = self.cleaned_data['password']
        val_conpass = self.cleaned_data['confirm_password']
        if len(val_name) < 15:
            raise forms.ValidationError('name must be at least 15 charters')
        if val_conpass != val_pass:
            raise forms.ValidationError('password dont match?please vaild password')
        
        
