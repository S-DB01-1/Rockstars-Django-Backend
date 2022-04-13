from rest_framework.routers import DefaultRouter

from .views import TribesViewSet, RockstarsViewSet, ArticlesViewSet, OnDemandRequestsViewSet, PodcastsViewSet, \
    VideosViewset, PodcastEpisodeViewSet

router = DefaultRouter()
router.register(r'tribes', TribesViewSet)
router.register(r'rockstars', RockstarsViewSet)
router.register(r'articles', ArticlesViewSet)
router.register(r'ondemand', OnDemandRequestsViewSet)
router.register(r'podcasts', PodcastsViewSet)
router.register(r'episodes', PodcastEpisodeViewSet)
router.register(r'videos', VideosViewset)

urlpatterns = router.urls
