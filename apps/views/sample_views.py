from django.http import HttpResponse
from apps.models import Sample


def sample_view(request):
    sample = Sample.objects.get(name="sample")
    print(sample.name)
    return HttpResponse("Hello, from sample view!")
