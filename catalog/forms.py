from django.forms import ModelForm
from .models import Product
from django.core.exceptions import ValidationError

FORBIDDEN_WORDS = [
'казино',
'криптовалюта',
'крипта',
'биржа',
'дешево',
'бесплатно',
'обман',
'полиция',
'радар',
]


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

    def clean_name(self):
        name = self.cleaned_data.get('name', '')
        for word in FORBIDDEN_WORDS:
            if word.lower() in name.lower():
                raise ValidationError(f'Название содержит запрещенное слово "{word}"')
            return name

    def clean_description(self):
        description = self.cleaned_data.get('description', '')
        for word in FORBIDDEN_WORDS:
            if word.lower() in description.lower():
                raise ValidationError(f'Описание содержит запрещенное слово: "{word}"')
            return description

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price is not None and price < 0:
            raise ValidationError('Цена не может быть отрицательной')
        return price