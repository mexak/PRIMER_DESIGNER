
from django.utils import timezone
from datetime import datetime

def my_cp(request):
	ctx = {
		"current_date": timezone.localtime(timezone.now()),
#		"current_date": datetime.now(),
#		"current_date": timezone.now(),
#		"current_date": datetime.now,
#		"current_date": datetime.datetime.now,
#		"current_date": timezone.now,
		"designed_in_year" : "2017",
	}
	return ctx
