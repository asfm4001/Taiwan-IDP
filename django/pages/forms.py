from django import forms
from django_recaptcha.fields import ReCaptchaField
from django_recaptcha.widgets import ReCaptchaV3

class ContactForm(forms.Form):
    # 可使用tuple or list, but it's must be 'key' to 'value'.
    SERVICES_LIST = [
    ('水利監測測報工程', '水利監測測報工程'),
    ('下水道檢監測工程', '下水道檢監測工程'),
    ('土石流監測工程', '土石流監測工程'),
    ('無人飛機調查', '無人飛機調查'),
    ('環境監測工程', '環境監測工程'),
    ('基樁試驗', '基樁試驗'),
    ('大地監(觀)測工程', '大地監(觀)測工程'),
    ('橋梁檢測工程', '橋梁檢測工程'),
    ('道路調查', '道路調查'),
    ('工程地質', '工程地質'),
]
    name = forms.CharField(label='姓名', max_length=30, required=False, widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    phone = forms.CharField(label='聯絡電話', max_length=11, min_length=10, required=False, widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    email = forms.EmailField(label='Email', required=False, widget=forms.EmailInput(
        attrs={'class': 'form-control'}))
    line_id = forms.CharField(label='LIND ID', max_length=30, required=False, widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    services = forms.MultipleChoiceField(label='選擇您的服務需求(可複選)', required=False, choices=SERVICES_LIST, widget=forms.CheckboxSelectMultiple(
        attrs={'class': 'form-check-input'}))
    message = forms.CharField(label='請留下您的訊息', required=False, widget=forms.Textarea(
        attrs={'class': 'form-control', 'row': 4, 'placeholder': '輸入訊息...'}))
    captcha = ReCaptchaField()