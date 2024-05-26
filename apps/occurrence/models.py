from django.db import models

class Occurrence(models.Model):
    TYPE_CHOICES = (
        ('broken_cable', 'Cabo Rompido'),
        ('fallen_tree', 'Árvore Caída/Poda'),
        ('rubble', 'Entulho'),
        ('public_lighting', 'Iluminação Pública'),
        ('asphalt', 'Asfalto'),
        ('flooding', 'Alagamento'),
        ('high_grass', 'Mato Alto'),
        ('zoonoses', 'Zoonoses'),
        ('robbery', 'Assalto/Roubo'),
        ('sewer', 'Esgoto'),
        ('loud_noise', 'Som Alto'),
        ('illegal_fire', 'Incêndio Clandestino'),
        # acidente de transito?
    )

    type = models.CharField(max_length=50, choices=TYPE_CHOICES)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    neighborhood = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    number = models.IntegerField()
    complement = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    reported_by = models.CharField(max_length=100, default='Anônimo')
    image = models.ImageField(upload_to='occurrences/', null=True, blank=True)
