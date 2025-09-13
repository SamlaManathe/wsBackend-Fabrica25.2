from django.urls import path
from .views import (
    EstadoListView,
    EstadoDetailView,
    EstadoCreateView,
    EstadoUpdateView,
    EstadoDeleteView,
)

urlpatterns = [
    path('estados/', EstadoListView.as_view(), name='estado_list'),
    path('estados/novo/', EstadoCreateView.as_view(), name='estado_create'),
    path('estados/<int:pk>/', EstadoDetailView.as_view(), name='estado_detail'),
    path('estados/<int:pk>/editar/', EstadoUpdateView.as_view(), name='estado_update'),
    path('estados/<int:pk>/deletar/', EstadoDeleteView.as_view(), name='estado_delete'),
]
