from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
# Create your models here.

#Inicia bloque que me permite crear un nuevo usuario dentro de la aplicacion
class MyAccountManager(BaseUserManager):
    def create_user(self, nombre, apellido, email, usuario, password = None):
        if not email:
            raise ValueError('El usuario debe tener un Email')
        if not usuario:
            raise ValueError('El usuario debe tener un nombre de usuario')
        user = self.model(
            email = self.normalize_email(email),
            usuario = usuario,
            nombre = nombre,
            apellido = apellido,
        )

        user.set_password(password)
        user.save(using = self._db)
        return user
#Fin de bloque

# Variables declaradas para crear el super usuario
    def create_superuser(self, nombre, apellido, email, usuario, password):
        user = self.create_user(
            email = self.normalize_email(email),
            usuario = usuario,
            password = password,
            nombre = nombre,
            apellido = apellido,
        )
# Por default se deben incluir en la creacion del super usuario
        user.is_admin = True
        user.is_active = True
        user.is_superadmin = True
        user.is_staff = True
        user.save(using = self._db)
        return user

class Cuenta(AbstractBaseUser):
    nombre = models.CharField(max_length = 50)
    apellido = models.CharField(max_length = 50)
    usuario = models.CharField(max_length = 50, unique = True)
    email = models.CharField(max_length = 100, unique = True)
    telefono = models.CharField(max_length = 50)
# Campos atributo de django por defecto
    date_joined = models.DateTimeField(auto_now_add = True)
    last_login = models.DateTimeField(auto_now_add = True)
    is_admin = models.BooleanField(default = False)
    is_staff = models.BooleanField(default = True)
    is_active = models.BooleanField(default = False)
    is_superadmin = models.BooleanField(default = False)

    #Para indicarle que el usuario de django sea el Email(Login)
    USERNAME_FIELD = 'email'
    #Campos requeridos en el registro del usuario
    REQUIRED_FIELDS =['usuario','nombre','apellido']
    objects = MyAccountManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj = None):
        return self.is_admin

    def has_module_perms(self, add_label):
        return True
