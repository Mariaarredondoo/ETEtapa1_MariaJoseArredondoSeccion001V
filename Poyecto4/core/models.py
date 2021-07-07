from django.db import models

# Create your models here.

class Registro(models.Model):
    numIdentificacion = models.IntegerField(primary_key=True, verbose_name='Número Identificación')
    fotografia = models.ImageField(verbose_name='Fotografía')
    nomCompleto = models.CharField(max_length=50, verbose_name='Nombre Completo')
    telefono = models.IntegerField( verbose_name='Número de telefono')
    direccion = models.CharField(max_length= 100, verbose_name='Dirección')
    mail = models.CharField(max_length=100, verbose_name='Correo Electrónico')
    pais = models.CharField(max_length=50,verbose_name='País')
    contraseña = models.CharField(max_length=10, verbose_name='Contraseña')    
    monedaPago = models.CharField(max_length=10, verbose_name='Moneda de Pago')
    
    
    def _str_(self):
        return self.nomCompleto
