from django import forms

# Products
class PostProductForm(forms.Form):
    name = forms.CharField(label='Name', max_length=30)
    description = forms.CharField(label='Description', max_length=300)
    price = forms.DecimalField(label='Price', max_digits=9, decimal_places=2)
    
class GetProductForm(forms.Form):
    name = forms.CharField(label='Name', max_length=30)
    
# Categories
class PostCategoryForm(forms.Form):
    name = forms.CharField(label='Name', max_length=30)
    description = forms.CharField(label='Description', max_length=300)
    
class GetCategoryForm(forms.Form):
    name = forms.CharField(label='Name', max_length=30)

# Orders
class PostOrderForm(forms.Form):
    number = forms.IntegerField(label='Number')
    total = forms.DecimalField(label='Total', max_digits=9, decimal_places=2)
    
class GetOrdersForm(forms.Form):
    number = forms.IntegerField(label='Number')
    