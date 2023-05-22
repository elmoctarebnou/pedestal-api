import json
from django.http import HttpResponse
from apps.models import Sample


def sample_view(request):
    sample = Sample.objects.get(name="sample")
    print(sample.name)
    context = {
        "name": sample.name,
        "description": sample.description,
        "created_at": sample.created_at.strftime("%m/%d/%Y, %H:%M:%S"),
    }
    return HttpResponse(json.dumps(context), content_type="application/json")
