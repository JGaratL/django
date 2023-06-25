from rest_framework.routers import DefaultRouter

from . import view_sets

router = DefaultRouter()
router.register('person_view_set', view_sets.PersonViewSet, basename='person')
urlpatterns = router.urls
