from rest_framework.routers import DefaultRouter

from .views import TribeViewSet, RockstarViewSet, ArticleViewSet, OnDemandRequestViewSet, PodcastViewSet, \
    VideoViewset, ArticleTextViewSet

router = DefaultRouter()
router.register(r'tribes', TribeViewSet)
router.register(r'rockstars', RockstarViewSet)
router.register(r'articles', ArticleViewSet)
router.register(r'ondemand', OnDemandRequestViewSet)
router.register(r'podcasts', PodcastViewSet)
# router.register(r'episodes', PodcastEpisodeViewSet)
router.register(r'videos', VideoViewset)
router.register(r'articletext', ArticleTextViewSet)

urlpatterns = router.urls
