
from django.utils import timezone
import datetime

def my_cp(request):
	ctx = {
		"current_date": timezone.now(),
#		"current_date": datetime.datetime.now(),
		"designed_in_year" : "2017",
	}
	return ctx
