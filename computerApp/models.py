from django.db import models
from datetime import datetime

class Machine(models.Model):
    TYPE = (
        ('PC', ('PC - Run Windows')),
        ('Mac', ('%AC - Run MacOS')),
        ('Serveur', ('Serveur - Simple Server toi deploy virtual machines')),
        ('Switch', ('Switch - To maintain and connect servers')),
            )

    id = models.AutoField(primary_key= True, editable=False)
    nom = models.CharField(max_length=10)
    maintenanceDate = models.DateField(default = datetime.now())
    mach = models.CharField(max_length=32, choices=TYPE, default='PC')
    IP = models.GenericIPAddressField(protocol='both', default='192.168.0.1')

    def __str__(self):
        return str(self.id) + " --> " + self.nom + " " + self.IP

class Personnel(models.Model):

    TYPE = (
        ('Developer', ('Developer - Member of the dev team')),
        ('Assistant', ('Assistant - Helps the dev team')),
        ('Software_Engineer', ('Software_Engineer - designs and develops effective softwares solutions')),
        ('Team_Leader', ('Team_Leader - guides and leads a group of devs')),

    )
    socialsecurity = models.CharField(primary_key=True, max_length=13, editable=True)
    nom = models.CharField(max_length=10)
    prenom = models.CharField(max_length=20)

    def __str__(self):
        return str(self.socialsecurity) + " -->" + self.nom + " " + self.prenom