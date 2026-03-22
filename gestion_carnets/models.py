from django.db import models

class Beneficiario(models.Model):
    # Datos Personales
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    ci = models.CharField(max_length=15, unique=True)
    direccion = models.CharField(max_length=255)
    telefono = models.CharField(max_length=15)
    rubro_empresa = models.CharField(max_length=100)
    edad = models.IntegerField(null=True, blank=True)
    sexo = models.CharField(max_length=20, choices=[('M', 'Masculino'), ('F', 'Femenino')], null=True)
    
    # Datos de Control (Automáticos)
    fecha_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido} - {self.ci}"

class ExamenLaboratorio(models.Model):
    # Relacionamos el examen con un beneficiario
    beneficiario = models.ForeignKey(Beneficiario, on_delete=models.CASCADE)
    
    # Campos según tu proyecto del SEDES
    copropasitologico = models.CharField(max_length=100)
    frotis_faringeo = models.CharField(max_length=100)
    vdr_chagas = models.CharField(max_length=100)
    fecha_examen = models.DateField()
    observaciones = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Laboratorio: {self.beneficiario.nombre}"

class EvaluacionMedica(models.Model):
    beneficiario = models.OneToOneField(Beneficiario, on_delete=models.CASCADE)
    presion_arterial = models.CharField(max_length=20)
    peso_kg = models.FloatField()
    talla_cm = models.IntegerField()
    observaciones_medicas = models.TextField(blank=True)
    apto_para_carnet = models.BooleanField(default=False)
    fecha_evaluacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Evaluación de {self.beneficiario.nombre}"