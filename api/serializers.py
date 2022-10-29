from rest_framework import serializers
from datetime import datetime
from api.models import ToDoList


class ToDoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDoList
        fields = ["to_do", "until_date"]

    def create(self, validated_data):
        done = True if validated_data.get("until_date") < datetime.now().date() else False
        to_do_model = ToDoList(to_do=validated_data.get("to_do"), until_date=validated_data.get("to_do"), done=done)
        to_do_model.save()
        return super(ToDoListSerializer, self)

