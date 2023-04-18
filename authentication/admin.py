from django.contrib import admin
from .models import Customers
from .models import Transaction

admin.site.register(Customers)
admin.site.register(Transaction)

