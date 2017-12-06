from django.core.management.base import BaseCommand, CommandError
import json
from primer_designer.models import Enzymes

class Command(BaseCommand):
    
    def handle(self, *args, **options):
        with open(options['file_name']) as f:
            enzymes = json.load(f)
            
            for enzyme in enzymes.values():
                Enzymes.objects.create(name = enzyme['name'], sequence = enzyme['target_site'])
                
    
    def add_arguments(self, parser):
         parser.add_argument('file_name')       