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

            return Response({
                    "success": False,
                    "prediction":False,
                    "chances":0
                }, status=status.HTTP_201_CREATED)
        







            output = predictPd(serializer.data)

            if not output:
                return Response({
                    "success": False,
                    "prediction":False,
                    "chances":0
                }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

            prediction, chances = output
            responseData = {
                "prediction": prediction,
                "chances": chances,
                "success": True
            }
            
        
            return Response(responseData, status=status.HTTP_201_CREATED)
        print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
