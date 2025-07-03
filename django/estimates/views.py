from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import TemplateView, DetailView
from django.utils.safestring import mark_safe
from django.contrib import messages
from django.contrib.admin.views.main import ERROR_FLAG
from django.contrib.admin.views.decorators import staff_member_required # function-based view
from django.contrib.auth.mixins import LoginRequiredMixin   # class-based view
from .models import Quotation, Order

# 僅Linux環境可執行
# from django_weasyprint import WeasyTemplateResponse

def index(request):
    return render(request, 'estimates/index.html')

@staff_member_required
def pdf(request, order_no):
    order = Order.objects.filter(pk=order_no).first()
    context = {'order': order,}

    response = WeasyTemplateResponse(
        request=request,
        template='estimates/quotation.html',   # html模板
        context=context,
        filename='report.pdf',         # 'report.pdf'預設為自動下載
        attachment=True
        # stylesheets=['pages/static/pages/assets/css/estimate.css'],   # 獨立css
    )
    return response

def admin_view(self, view, cacheable=False):
    """
    Decorator to create an admin view attached to this ``AdminSite``. This
    wraps the view and provides permission checking by calling
    ``self.has_permission``.

    You'll want to use this from within ``AdminSite.get_urls()``:

        class MyAdminSite(AdminSite):

            def get_urls(self):
                from django.urls import path

                urls = super().get_urls()
                urls += [
                    path('my_view/', self.admin_view(some_view))
                ]
                return urls

    By default, admin_views are marked non-cacheable using the
    ``never_cache`` decorator. If the view can be safely cached, set
    cacheable=True.
    """

@staff_member_required
def convert_quotation_to_order(request, pk):
    quotation = Quotation.objects.filter(pk = pk).first()
    order = quotation.convert_to_order()
    url = reverse("admin:estimates_order_change", args=[order.pk])
    link = f'<a href="{url}">{order.number}</a>'
    messages.success(request, mark_safe(f'成功新增了 order“{link}”。'))
    return redirect('/admin/estimates/order')


# class DetailView(DetailView):
#     model = Order
#     template_name = 'estimates/detail.html'
    
#     # overwrite default
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         order = self.get_object()
#         context['ordered_products'] = order.orderproduct_set.select_related('product').order_by('product__id')
#         return context

class QuotationPreviewView(LoginRequiredMixin, DetailView):
    model = Quotation
    template_name = 'estimates/quotation.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        quotation = self.get_object()
        context['quotationed_products'] = quotation.quotationproduct_set.select_related('product').order_by('product__id')
        return context

class CustomAdminPageView(TemplateView):
    template_name = "admin/custom_admin_page.html"
    admin_site = None  # 初始化 admin_site

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)  # 獲取原始的上下文數據

        # 獲取傳遞的 AdminSite 實例
        admin_site = self.admin_site or self.request.site

        if admin_site:
            # 獲取完整的 admin 上下文
            admin_context = admin_site.each_context(self.request)
            context.update(admin_context)

            # 添加額外的上下文數據
            context.update(
                {
                    "title": "Custom Admin Page",
                    "subtitle": None,
                    # 是否為 popup
                    "is_popup": False,
                    "has_permission": self.request.user.is_active
                    and self.request.user.is_staff,
                    # 是否啟用側邊欄
                    "is_nav_sidebar_enabled": admin_context.get(
                        "is_nav_sidebar_enabled", True
                    ),
                    # 獲取應用列表
                    "available_apps": admin_site.get_app_list(self.request),
                    ERROR_FLAG: admin_context.get(ERROR_FLAG, ""),
                }
            )
        return context

    # 重寫as_view方法，保存添加admin_site屬性
    @classmethod
    def as_view(cls, **initkwargs):
        view = super().as_view(**initkwargs)
        view.admin_site = initkwargs.get("admin_site")
        return view
    