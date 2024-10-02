import requests
from django.http import JsonResponse

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from budu.serializer import UserSerializer


@api_view(['POST'])
def sign_up(request):
    serializer = UserSerializer(data=request.data)
    print(serializer)
    if serializer.is_valid():
        user = serializer.save()
        return Response({'message': 'User created Successfully'}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Create your views here.

@api_view(['GET'])
def live_matches(request):
    headers = {
        'x-rapidapi-key': "8a60983099msh98a4bb32c3510ebp17ce79jsne8914bd97eca",
        'x-rapidapi-host': "livescore6.p.rapidapi.com"
    }
    url = 'https://livescore6.p.rapidapi.com/v2/search?Category=soccer&Query=chel'
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()

        data = response.json()
        if data.get("success"):
            matches = data.get('data', {}).get('matches', [])
            return JsonResponse({'data': matches}, status=200)
        else:
            return JsonResponse({'error': 'API response indicates failure'}, status=400)

    except requests.exceptions.RequestException as e:
        return JsonResponse({'error': str(e)}, status=500)
    except Exception as e:
        return JsonResponse({'error': 'An unexpected error occurred.'}, status=500)