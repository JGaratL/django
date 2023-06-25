import json
from django.http import JsonResponse
from rest_framework import permissions, authentication
from rest_framework.mixins import ListModelMixin, CreateModelMixin, DestroyModelMixin, RetrieveModelMixin, \
    UpdateModelMixin
from .models import Person, Group
from rest_framework.generics import ListAPIView, GenericAPIView
from .serializer import PersonSerializer, GroupSerializer


class PersonListView(ListAPIView):
    model = Person
    serializer_class = PersonSerializer
    queryset = Person.objects.all()


class PersonView(RetrieveModelMixin, ListModelMixin, DestroyModelMixin, CreateModelMixin, UpdateModelMixin,
                 GenericAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    lookup_field = 'id'
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, *kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class GroupListView(ListAPIView):
    model = Person
    serializer_class = GroupSerializer
    queryset = Group.objects.all()
    permission_classes = [permissions.IsAuthenticated]


class GroupView(RetrieveModelMixin, ListModelMixin, DestroyModelMixin, CreateModelMixin, UpdateModelMixin,
                GenericAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    lookup_field = 'id'
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, *kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


def api_home(request, group_id):
    queryset = Person.objects.filter(group=group_id)
    permission_classes = [permissions.IsAuthenticated]
    return JsonResponse(PersonSerializer(queryset, many=True).data, safe=False)
