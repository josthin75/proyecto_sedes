import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'configuracion.settings')
django.setup()

from django.contrib.auth.models import User
if not User.objects.filter(username='admin_sedes').exists():
    User.objects.create_superuser('admin_sedes', 'admin@example.com', 'SedesBeni2026')
    print("Superusuario creado con éxito")