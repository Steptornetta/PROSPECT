from django import forms

class ProspectForm(forms.Form):
	yourfirst_name = forms.CharField(label = "First Name", max_length = 100)
	yourlast_name = forms.CharField(label = "Last Name", max_length = 100)
	form = [yourfirst_name,  yourlast_name]
