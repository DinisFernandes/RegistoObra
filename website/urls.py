from django.urls import path, include
from .views import PostList
from .views import PostBusca
from .views import PostDetail
from .views import MapaBarroselas
from .views import MapaChafe
from .views import MapaDarque
from .views import MapaPortuzelo
from .views import MapaPerre
from .views import MapaEspregueira
from .views import MapaUrsulinas
from .views import MapaCardielos
from .views import MapaFincao
from .views import MapaPortela

# from .views import PostBusca
# from .views import MapaView
# from .views import TesteView
# from django.urls import include

urlpatterns = [
    path('', PostList.as_view(), name="post_list"),
    path('post/<int:pk>/', PostDetail.as_view(), name="post_detail"),
    path('busca/', PostBusca.as_view(), name="post_busca"),
    path('barroselas/', MapaBarroselas.as_view(), name="barroselas"),
    path('vilanovaanha/', MapaChafe.as_view(), name="vilanovaanha"),
    path('darque/', MapaDarque.as_view(), name="darque"),
    path('portuzelo/', MapaPortuzelo.as_view(), name="portuzelo"),
    path('perre/', MapaPerre.as_view(), name="perre"),
    path('espregueiramendes/', MapaEspregueira.as_view(), name="espregueiramendes"),
    path('ursulinas/', MapaUrsulinas.as_view(), name="ursulinas"),
    path('cardielos/', MapaCardielos.as_view(), name="cardielos"),
    path('fincao/', MapaFincao.as_view(), name="fincao"),
    path('portela/', MapaPortela.as_view(), name="portela"),
]