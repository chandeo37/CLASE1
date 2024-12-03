from django.db import models

HEIGHTS = (
    ('S', 'Small'),
    ('B', 'Big')
)

STATUS = [
    ('DISPONIBLE', 'DISPONIBLE'),
    ('AGOTADO', 'AGOTADO')
]


class Smartphone(models.Model):
    model = models.CharField(max_length=50)
    ram = models.CharField(max_length=50, default='')
    pantalla = models.CharField(max_length=50, default='')
    height = models.CharField(
        max_length=1,
        choices=HEIGHTS,
        default='S'

    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )
    status = models.CharField(max_length=15, choices=STATUS, default='DISPONIBLE')

    class Meta:
        permissions = [
            ("can_publish", "Can publish smartphones"),
            ("can_view_details", "Can view detailed smartphone information"),
        ]
    def __str__(self):
        return f"{self.model} - {self.ram}"

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)

    def __str__(self):
        return self.title
#relacion de unos a muchos
class Chapter(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='chapters')
    title = models.CharField(max_length=100)
    pages = models.PositiveIntegerField()

    def __str__(self):
        return f"Capitulo {self.title}: Pages{self.pages}"
