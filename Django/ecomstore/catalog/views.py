from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.template import RequestContext, loader

from .models import Category, Product


def index(request, template_name="catalog/index.html"):
    page_title = "Music Instruments and Sheet Music for Musicans"
    categories = Category.objects.all().values()
    context = {
        "page_title": page_title,
        "categories": categories,
    }
    template = loader.get_template(template_name)
    return HttpResponse(template.render(context, request))


def show_category(request, category_slug, template_name="catalog/category.html"):
    c = get_object_or_404(Category, slug=category_slug)
    products = c.product_set.all()
    pate_title = c.name
    meta_keywords = c.meta_keywords
    meta_description = c.meta_description
    template = loader.get_template(template_name)
    return HttpResponse(template.render(locals()))


def show_product(request, product_slug, template_name="catalog/product.html"):
    p = get_object_or_404(Product, slug=product_slug)
    categories = p.categories.filter(is_active=True)
    page_title = p.name
    meta_keywords = p.meta_keywords
    meta_description = p.meta_description
    template = loader.get_template(template_name)
    return HttpResponse(template.render(locals()))
