from django.db import models



# Create your models here.

class Mascota(models.Model):
    nombre_animal= models.CharField(max_length=50)
    edad= models.IntegerField()
    tipo= models.CharField(max_length=40)
    motivo= models.CharField(max_length=40)
    fecha= models.DateField()
    costo= models.IntegerField()
    def __str__(self):
        return f"Nombre de la Mascota: {self.nombre_animal} - Edad: {self.edad} - Tipo: {self.tipo} - Motivo de Estancia: {self.motivo} - Fecha: {self.fecha} - Costo: {self.costo} "

class Persona(models.Model):
    nombre= models.CharField(max_length=40)
    DNI = models.IntegerField()
    apellido= models.CharField(max_length=40)
    email= models.EmailField()
    telefono= models.IntegerField()
    def __str__(self):
        return f"Nombre: {self.nombre} - Apellido: {self.apellido} - Cedula de Identidad: {self.DNI} - Email: {self.email} - Telefono: {self.telefono} "


class Cuidador(models.Model):
    cuidador = models.CharField(max_length=20)
    apellido_cuidador = models.CharField(max_length=40)
    DNI_cuidador = models.IntegerField()
    def __str__(self):
        return f"Nombre del Cuidador: {self.cuidador} - Apellido: {self.apellido_cuidador} - Cedula de Identidad: {self.DNI_cuidador} "



