from rest_framework import serializers
from datetime import datetime
from api.models import ToDoList


class ToDoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDoList
        fields = ["to_do", "until_date", "done", "created_at"]
        read_only_fields = ("done", "created_at")

    def create(self, validated_data):
        done = validated_data.get("until_date") <= datetime.now().date()
        to_do_model = ToDoList(to_do=validated_data.get("to_do"), until_date=validated_data.get("until_date"), done=done)
        to_do_model.save()
        return to_do_model

