from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from primer_designer.forms import PlasmidChoice
from django.views.generic.edit import FormView
from django.views.generic import TemplateView
from django.views import View
from django.urls import reverse
from .forms import EnzymeChoice

from .models import Enzymes

class StartView(TemplateView):
    template_name = "start_page.html"
    
class GetData(FormView):
    template_name = 'plasmids.html'
    form_class = PlasmidChoice
    success_url = '/'
    
    def form_valid(self, form):
        plasmid_sequence = form.cleaned_data['plasmids'] #z formularza nazwa
        insert_sequence = form.cleaned_data['insert_sequence']

        enzymes_applicable = []
        #enzymes = Enzymes.objects.all()
        enzymes = Enzymes.objects.filter(name__in = ['BglII', 'XhoI', 'SacI', 'HindIII', 'EcorI', 'PstI', 'SalI', 'KpnI', 'SacII', 'XmaI', 'ApaI', 'SmaI', 'BamHI', 'XbaI', 'BclI', 'HpaI', 'NotI', 'EagI', 'NheI', 'NdeI', 'NcoI', 'AflII', 'NruI', 'KpnI', 'EagI', 'SpeI', 'PstI', 'BstBI', 'AatII'])
        for enzyme in enzymes:
            if len(enzyme.cleared_sequence) == 6 and enzyme.cleared_sequence in plasmid_sequence.sequence and enzyme.cleared_sequence not in insert_sequence:
                enzymes_applicable.append({'enzyme_name': enzyme.name, 'enzyme_sequence': enzyme.sequence, 'enzyme_cleared_sequence': enzyme.cleared_sequence })
        
        self.request.session['plasmid_name'] = plasmid_sequence.name
        self.request.session['plasmid_sequence'] = plasmid_sequence.sequence
        self.request.session['insert_sequence'] = insert_sequence
        self.request.session['enzymes_applicable'] = enzymes_applicable
        
        return HttpResponseRedirect(reverse('enzymes'))
    
class ShowEnzymes(View):
    def get(self, request):
        plasmid = request.session['plasmid_sequence']
        plasmid_name = request.session['plasmid_name']
        insert = request.session['insert_sequence']
        enzymes = request.session['enzymes_applicable']
        
        form = EnzymeChoice(enzymes=enzymes)
        return render(request, "enzymes.html", {"form": form})
    
            
        # x = request.session['plasmid_sequence']
        # x.name
        
    #for nacid in plasmid_sequence:
    #    if len[0,nacid 
    
