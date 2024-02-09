from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Prediction
from .serializers import PredictionSerializer
from .pdPredict import predictPd
from .recommendation import getRecommendation


class PredictionAPIView(APIView):
    queryset = Prediction.objects.all()
    serializer_class = PredictionSerializer

    def get(self, request, format=None):
        predictions = Prediction.objects.all()
        serializer = PredictionSerializer(predictions, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = PredictionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = serializer.data

            imgUrl = data["retinalScan"]
            name = data["name"]
            age = data["age"]
            sex = data["sex"]
            country = data["country"]

            output = predictPd(imgUrl, name, age, country, sex)
            if not output:
                return Response({
                    "success": False,
                    "prediction": False,
                    "chances": 0,
                    "segmentedImage": imgUrl
                }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

            recomendations = getRecommendation(name,age,country)
            prediction, chances = output
            responseData = {
                "prediction": prediction,
                "chances": chances,
                "success": True,
                "segmentedImage": imgUrl,
                "recommendation":recomendations
            }
            return Response(responseData, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
