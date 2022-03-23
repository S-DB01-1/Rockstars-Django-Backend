from rest_framework.routers import DefaultRouter

from .views import TribesViewSet, RockstarsViewSet, ArticlesViewSet, OnDemandRequestsViewSet

router = DefaultRouter()
router.register(r'tribes', TribesViewSet)
router.register(r'rockstars', RockstarsViewSet)
router.register(r'articles', ArticlesViewSet)
router.register(r'ondemand', OnDemandRequestsViewSet)

urlpatterns = router.urls
