from rest_framework import routers
from .api import ProjectViewset

router = routers.DefaultRouter()  # router crea las rutas por si solo ( get, post, put, delete, etc)

router.register('api/projects', ProjectViewset, 'projects')
''' ruta - vista/api  - nombre de la ruta '''

urlpatterns = router.urls

