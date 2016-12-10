from django import forms


class login_Form(forms.Form):
    your_name = forms.CharField(
        label='名前',
        max_length=20,
        required=True,
        widget=forms.TextInput()
    )
    your_password = forms.CharField(
	    label='パスワード'
	    max_length=20,
	    required=True,
	    widget=forms.TextInput()
    )