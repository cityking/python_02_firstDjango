from django import forms
from hello.models import Publisher
from django.core.exceptions import ValidationError

# def validate_name(value):
#     try:
#         Publisher.objects.get(name=value)
#         raise ValidationError("%s的信息已经存在"%value)
#     except Publisher.DoesNotExist:
#         pass




class Publisher_form(forms.ModelForm):
    # name = forms.CharField(label='名称',error_messages={'required':'这个项必须填写'})
    # address = forms.CharField(label='地址')
    # city = forms.CharField(label='城市')
    # state_province = forms.CharField(label='省份')
    # state_province = forms.CharField(label='省份')
    # country = forms.CharField(label='国家')
    # website = forms.URLField(label='网址')
    # name = forms.CharField(label='名称',validators=[validate_name])

    # def clean_name(self):
    #     value = self.cleaned_data['name']
    #     try:
    #         Publisher.objects.get(name=value)
    #         raise ValidationError("%s的信息已经存在" % value)
    #     except Publisher.DoesNotExist:
    #         pass
    #     return value

    def clean(self):
        cleaned_data = super(Publisher_form, self).clean()
        value = cleaned_data.get('name')
        try:
            Publisher.objects.get(name=value)
            self._errors['name']=self.error_class(["%s的信息已经存在" % value])
        except Publisher.DoesNotExist:
            pass
        return cleaned_data


    class Meta:
        model = Publisher
        exclude = ('id',)