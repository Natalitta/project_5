from django.contrib import admin
from .models import Order, OrderItem


class OrderItemAdmin(admin.TabularInline):
    model = OrderItem
    readonly_fields = ('orderitem_total',)


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderItemAdmin,)

    readonly_fields = ('order_number', 'date',
                       'order_total', 'original_bag',
                        'stripe_pid',)

    fields = ('order_number', 'user_profile', 
                'date', 'full_name', 'email', 'phone_number', 
                'order_total', 'original_bag', 'stripe_pid',)

    list_display = ('order_number', 'date', 'full_name',
                    'order_total',)
    
    ordering = ('-date',)

admin.site.register(Order, OrderAdmin)

