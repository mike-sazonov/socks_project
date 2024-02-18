from django import forms


class SocksForm(forms.Form):
    GENDER = [
        ('Не выбран', 'Не выбран'),
        ('Мужской', 'Мужской'),
        ('Женский', 'Женский'),
        ('Детский', 'Детский'),
        ]
    winter = forms.BooleanField(required=False, label='Зима')
    summer = forms.BooleanField(required=False, label='Лето')
    gender = forms.ChoiceField(choices=GENDER, required=False, label='Пол: ')

    def full_clean(self): # переназначаем метод full_clean чтобы добавить в clean_data значение для gender
        clean = super().full_clean()
        if self.cleaned_data['gender'] == 'Не выбран':
            self.cleaned_data['gender'] = 'Мужской Женский Детский' # если не выбран, задаем строкой все гендеры
        return clean