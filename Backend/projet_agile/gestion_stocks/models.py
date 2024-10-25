from django.db import models 

# Modèle pour représenter les catégories d'articles (ex: fruits, boissons, etc.)
class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

# Modèle pour les fournisseurs
class Supplier(models.Model):
    name = models.CharField(max_length=255)
    contact_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    address = models.TextField()

    def __str__(self):
        return self.name

# Modèle pour représenter les articles en stock
class Product(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="products")
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, related_name="supplied_products")
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Prix du produit
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

# Modèle pour gérer le stock des articles
class Stock(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()  # Quantité disponible en stock
    last_restock_date = models.DateField(blank=True, null=True)  # Dernière date de réapprovisionnement

    def __str__(self):
        return f"Stock de {self.product.name} - Quantité: {self.quantity}"

# Modèle pour représenter une vente
class Sale(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity_sold = models.PositiveIntegerField()  # Quantité vendue
    sale_date = models.DateTimeField(auto_now_add=True)  # Date de la vente
    total_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Vente de {self.quantity_sold} {self.product.name} - {self.sale_date}"

    def save(self, *args, **kwargs):
        # Mettre à jour la quantité en stock lors de la vente
        stock = Stock.objects.get(product=self.product)
        if stock.quantity >= self.quantity_sold:
            stock.quantity -= self.quantity_sold
            stock.save()
            self.total_price = self.quantity_sold * self.product.price
            super().save(*args, **kwargs)
        else:
            raise ValueError("Quantité en stock insuffisante.")
