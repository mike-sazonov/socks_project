from django import forms


class SocksForm(forms.Form):
    GENDER = [
        ('Мужской', 'Мужской'),
        ('Женский', 'Женский'),
        ('Детский', 'Детский')
    ]
    winter = forms.BooleanField(required=False, label='Зима')
    summer = forms.BooleanField(required=False, label='Лето')
    gender = forms.ChoiceField(choices=GENDER, required=False, label='Пол: ')

