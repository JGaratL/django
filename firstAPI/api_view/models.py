from django.db import models
import uuid
# Create your models here.
class Person(models.Model):
    id          = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="ID único para la entidad Person")
    first_name  = models.CharField(max_length=30)
    last_name   = models.CharField(max_length=30)
    group       = models.ForeignKey(
        "Group",
        on_delete=models.SET_NULL,
        null=True
    )

    # Metadata
    class Meta:
        ordering = ["-id"]

    # Métodos
    def get_absolute_url(self):
        """
        Devuelve la url para acceder a una instancia particular de MyModelName.
        """
        return reversed('person-detail', args=[str(self.id)])

    def __str__(self):
        """
        Cadena para representar el objeto MyModelName (en el sitio de Admin, etc.)
        """
        return self.first_name + ' ' + self.last_name
class Group(models.Model):
    id          = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="ID único para la entidad Person")
    name        = models.CharField(max_length=30, null=False)
    def __str__(self):
        """
        Cadena para representar el objeto MyModelName (en el sitio de Admin, etc.)
        """
        return self.name
