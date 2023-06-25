import uuid

from rest_framework import serializers
from rest_framework.fields import UUIDField

from .models import Person, Group


class GroupSerializer(serializers.Serializer):
    id = serializers.UUIDField(required=False)
    name = serializers.CharField(max_length=30, required=False)
    def create(self, validated_data):
        group = Group(
            id          = uuid.uuid4(),
            name        = validated_data['name']
        )
        group.save()
        return group

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance

class PersonSerializer(serializers.Serializer):
    id          = serializers.UUIDField(required=False)
    first_name  = serializers.CharField(max_length=30, required=False)
    last_name   = serializers.CharField(max_length=30, required=False)
    group       = serializers.PrimaryKeyRelatedField(allow_null=True, queryset=Group.objects.all())

    def create(self, validated_data):
        person = Person(
            id          = uuid.uuid4(),
            first_name  = validated_data['first_name'],
            last_name   = validated_data['last_name'],
            group       = validated_data['group']
        )
        person.save()
        return person
    def update(self, instance, validated_data):
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.group = validated_data.get('group', instance.group)
        instance.save()
        return instance
