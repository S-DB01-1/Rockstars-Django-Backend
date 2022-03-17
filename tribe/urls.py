from rest_framework.routers import DefaultRouter
from .views import TribesViewSet, RockstarsViewSet, ArticlesViewSet

router = DefaultRouter()
router.register(r'tribes', TribesViewSet)
router.register(r'rockstars', RockstarsViewSet)
router.register(r'articles', ArticlesViewSet)

urlpatterns = router.urls