# models.py
class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)

class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20)

class Item(models.Model):
    order = models.ForeignKey(Order, related_name="items", on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()

# views.py
def recent_orders(request):
    data = []
    for order in Order.objects.filter(status="paid").order_by("-created_at")[:50]:
        data.append({
            "id": order.id,
            "customer": order.customer.username,
            "items": [
                {"product": i.product.name, "qty": i.quantity}
                for i in order.items.all()
            ],
        })
    return JsonResponse(data, safe=False)