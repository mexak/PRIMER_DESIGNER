from django.db import models

class Plasmids(models.Model):
        name = models.CharField(max_length=64) #albo Charfield
        sequence = models.TextField()
        
        def __str__(self):
            return self.name
        
class Enzymes(models.Model):
        name = models.CharField(max_length=64)
        sequence = models.CharField(max_length=64)
        
        @property
        def cleared_sequence(self):
            sequence = self.sequence
            cleared_sequence = ""
            for nucleotide in sequence:
                if nucleotide.isalpha():
                    cleared_sequence += nucleotide 
            return cleared_sequence 
        
        def __str__(self):
            return self.name
        
        def __str__(self):
            return self.cleared_sequence
        
class Insert(models.Model):
        sequence = models.TextField(help_text= "Enter sequence of your insert:" )