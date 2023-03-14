from django.http import JsonResponse
from .models  import MPackage
from .serializers import MPackageSerializer

def package_list(request):
    vPackage = MPackage.objects.all()
    vPackageSerializer = MPackageSerializer(vPackage, many=True)
    return JsonResponse({'package_list':vPackageSerializer.data}, safe=False)