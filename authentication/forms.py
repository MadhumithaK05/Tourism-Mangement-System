from django import forms
from authentication.models import Transaction

class place(forms.Form):
    class Meta:
        model = Transaction
        fields = ['place']
        pselect = {
            'place': forms.Select(choices=[('Jodhpur', 'Jodhpur'),
            ('Agra', 'Agra'),
            ('Mumbai', 'Mumbai'),
            ('Punjab', 'Punjab'),
            ('Jaipur', 'Jaipur'),
            ('Kerala', 'Kerala'),
            ('Meghalaya', 'Meghalaya'),
            ('Ladakh', 'Ladakh'),
            ('Goa', 'Goa'),
            ('Lakshadweep', 'Lakshadweep'),
            ('Tamil Nadu', 'Tamil Nadu'),
            ('Kashmir', 'Kashmir')]),
        }

class MyForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['completed']
        widgets = {
            'completed': forms.RadioSelect(choices=[('yes','yes'),('no','no')]),
        }