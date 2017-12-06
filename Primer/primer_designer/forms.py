from django import forms
from .models import Plasmids
from django.forms import Form, ModelForm
from betterforms.multiform import MultiModelForm

#class PlasmidChoice(forms.Form):
#    plasmid_name = forms.ChoiceField(choices=[("None", "None")])
#    
#    class Meta:
#        model = Plasmids
#     
#    def __init__(self, *args, **kwargs):
#        super(PlasmidChoice, self).__init__(*args, **kwargs)
#        self.fields['name'].choices=get_plasmids()
        
class PlasmidChoice(forms.Form):
    plasmids = forms.ModelChoiceField(queryset=Plasmids.objects.order_by("name"), empty_label="Plasmids")
    # jeszcze, zeby wybierało sie cos zawierające znaki
    insert_sequence = forms.CharField(label="Enter sequence of your insert ",
                                         widget=forms.Textarea
                                        ) #jeszcze walidator   
    
class EnzymeChoice(forms.Form):

    def __init__(self, *args, **kwargs):
        enzymes = kwargs.pop('enzymes')
        
        super(EnzymeChoice, self).__init__(*args, **kwargs)
        
        for enzyme in enzymes:
            self.fields['enzyme_%s' %enzyme['enzyme_name']] = forms.BooleanField(
                initial=False, required=False, label= '%s  %s' %(enzyme['enzyme_name'], enzyme['enzyme_sequence']))
        
        
        
    
    
    