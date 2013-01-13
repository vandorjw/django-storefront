from storefront.models.product.categories import Category
from storefront.models.product.items import Item
from storefront.models.frontend.banners import Banner

from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView

class HomePage( TemplateView ):
    
    template_name="storefront/home.html"
	
    def get_context_data(self, **kwargs):
        context = super(HomePage, self).get_context_data(**kwargs)
        context['feature_list'] = Item.objects.filter(featured=True)
        context['category_list'] = Category.objects.all()
        context['banner_list'] = Banner.objects.all()
        return context


class AboutPage( TemplateView ):
    
    template_name="storefront/about.html"
    
    #queryset = ''
	
    def get_context_data(self, **kwargs):
        context = super(AboutPage, self).get_context_data(**kwargs)
        return context
        
class ContactPage( TemplateView ):
    
    template_name="storefront/contact.html"
	
    def get_context_data(self, **kwargs):
        context = super(ContactPage, self).get_context_data(**kwargs)
        return context
