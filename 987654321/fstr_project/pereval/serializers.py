from rest_framework import serializers  
from .models import Pereval, Coords  

class CoordsSerializer(serializers.ModelSerializer):  
    class Meta:  
        model = Coords  
        fields = ['latitude', 'longitude', 'height']  

class PerevalSerializer(serializers.ModelSerializer):  
    coord = CoordsSerializer()  

    class Meta:  
        model = Pereval  
        fields = ['id', 'beauty_title', 'title', 'other_titles', 'connect', 'coord', 'status']  
    
    def create(self, validated_data):  
        coords_data = validated_data.pop('coord')  
        
        try: 
            print("Принятые данные:", validated_data)  
            print("Данные координат:", coords_data)
            coord = Coords.objects.create(**coords_data)  
            pereval = Pereval.objects.create(coord=coord, **validated_data)  
        except Exception as e:
            print("Ошибка создания объекта:", e)  
            raise serializers.ValidationError("Ошибка при создании объекков.")
    
        return pereval