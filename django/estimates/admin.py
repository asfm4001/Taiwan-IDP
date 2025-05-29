from django.contrib import admin
from django.urls import path, reverse
from django.core.handlers.wsgi import WSGIRequest
from .models import Client, Order, Product, OrderProduct, Quotation, QuotationProduct
from .views import CustomAdminPageView as CustomView
# Register your models here.

class QuotationProductInline(admin.TabularInline):
    model = QuotationProduct
    extra = 1

class OrderProductInline(admin.TabularInline):
    model = OrderProduct
    extra = 1

class ClientAdmin(admin.ModelAdmin):
    fieldsets = [
        ('客戶資料', {
            'fields': [('name', 'phone'), 'gui'],
            # "classes": ["collapse"]
        })
    ]
    search_fields = ["name"]
    list_display = ["name", "phone", "gui"]
    
class ProductAdmin(admin.ModelAdmin):
    fieldsets = [
        ('施工品項', {
            'fields': ['name', 'price']
        })
    ]
    list_display = ['name']

class QuotationAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {
            "fields": ['client'],
            # "classes": ["collapse"]
            }),
        ("訂單資訊", {
            "fields": ['name', ('address', 'created_date'), 'area'],
            }),
        ("聯絡資訊", {
            "fields": [('contact_name'), 'note'],
            }),
    ]
    inlines = [QuotationProductInline]
    search_fields = ['address']
    list_display = ["address", "created_date", 'contact_name']
    view_on_site = True
    ordering = ['created_date']

class OrderAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {
            "fields": ['client'],
            # "classes": ["collapse"]
            }),
        ("訂單資訊", {
            "fields": [('address', 'created_date'), 'status'],
            }),
        ("聯絡資訊", {
            "fields": [('contact_name'), 'note'],
            }),
    ]
    inlines = [OrderProductInline]
    search_fields = ['address']
    # date_hierarchy = 'order_date'     # 日期分類
    list_display = ["address", "status", "created_date", 'contact_name']
    list_filter = ['status']
    view_on_site = True
    ordering = ['created_date']

class CustomAdminPageView(admin.AdminSite):
    # 自定義 admin 頁面 除了原本的 urls 之外,再添加一個自定義的 url
    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path(
                "custom_admin_page/",
                self.admin_view(CustomView.as_view(admin_site=self)),
                name="custom_admin_page",
            ),
        ]
        return custom_urls + urls

    # 自定義 admin 頁面的左側導航欄
    def get_app_list(self, request: WSGIRequest) -> list[any]:
        app_list = super().get_app_list(request)

        custom_admin_url = reverse("admin:custom_admin_page")

        app_list.append(
            {
                "name": ("Custom Admin Page"),
                "app_label": "custom_admin_page",
                "app_url": "",
                "has_module_perms": True,
                "models": [
                    {
                        "name": ("Custom Admin Page"),
                        "object_name": "CustomAdminPage",
                        "admin_url": custom_admin_url,
                    }
                ],
            }
        )
        return app_list

admin_site = CustomAdminPageView(name="admin")
admin_site.register(Client, ClientAdmin)
admin_site.register(Product, ProductAdmin)
admin_site.register(Order, OrderAdmin)
admin_site.register(Quotation, QuotationAdmin)

# admin.site.register(Client, ClientAdmin)
# admin.site.register(Product, ProductAdmin)
# admin.site.register(Order, OrderAdmin)
# admin.site.register(Quotation, QuotationAdmin)