from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Prediction
from .serializers import PredictionSerializer
from .pdPredict import predictPd


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
            img = data["retinalScan"]
            output = predictPd(data)


            print(serializer.data)
            if not output:
                return Response({
                    "success": False,
                    "prediction":False,
                    "chances":0,
                    "segmentedImage":img
                }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

            prediction, chances = output
            responseData = {
                "prediction": prediction,
                "chances": chances,
                "success": True,
                "segmentedImage":img
            }
            return Response(responseData, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
