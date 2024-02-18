from rest_framework import serializers
from .models import Prediction

class PredictionSerializerPost(serializers.ModelSerializer):
    class Meta:
        model = Prediction
        fields =["name",'age',"sex","country","retinalScan"]


class PredictionSerializerGet(serializers.ModelSerializer):
    class Meta:
        model = Prediction
        fields =["name",'age',"sex","country","retinalScan","segmentedImage","prediction","recommendation","chances"]