import os
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from gestion_carnets import views 
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('inicio/', views.inicio, name='inicio'),
    
    # Rutas de Gestión
    path('editar/<int:beneficiario_id>/', views.editar_beneficiario, name='editar_beneficiario'),
    path('eliminar/<int:beneficiario_id>/', views.eliminar_beneficiario, name='eliminar_beneficiario'),
    path('examen/<int:beneficiario_id>/', views.cargar_examen, name='cargar_examen'),
    path('medico/<int:beneficiario_id>/', views.revision_medica, name='revision_medica'),
    path('descargar-carnet/<int:beneficiario_id>/', views.generar_pdf_carnet, name='descargar_carnet'),
    
    path('accounts/', include('django.contrib.auth.urls')),
    path('logout/', views.salir, name='logout'), 
]

# ESTA PARTE ES LA QUE HACE QUE EL LOGO SE VEA EN TU PC
if settings.DEBUG:
    # Opción 1: Servir desde STATIC_ROOT
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    # Opción 2: Servir directamente desde la carpeta static del escritorio
    urlpatterns += static(settings.STATIC_URL, document_root=os.path.join(settings.BASE_DIR, 'static'))