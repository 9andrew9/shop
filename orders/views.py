from django.shortcuts import render

# Create your views here.
from .models import OrderItem
from .models import Product
from .forms import OrderCreateForm
from cart.cart import Cart
from .tasks import OrderCreated
from .models import Order


def OrderCreate(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order, product=item['product'],
                                         price=item['price'],
                                         quantity=item['quantity'])
            oof = OrderItem.objects.filter(order_id=order.id)
            for i in oof:
                po_f = Product.objects.filter(id=i.product_id)
                #print(po_f.values())
                for gh in po_f:
                    if gh.stock >= i.quantity:
                        count_summ = gh.stock - i.quantity
                        po_f.values().update(stock=count_summ)
                    else:
                        #cart.clear()
                        Order.objects.filter(id=order.id).delete()
                        return render(request, 'cart/detail_cart_fail.html', {'cart': cart})

            product_name = cart.get_product()
            total_price = cart.get_total_price()
            cart.clear()
            OrderCreated(order.id, total_price, product_name)
            return render(request, 'orders/order/created.html', {'order': order})

    form = OrderCreateForm()
    return render(request, 'orders/order/create.html', {'cart': cart,
                                                        'form': form})
