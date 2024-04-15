from .models import Category

def global_categories_context(request):    
    return {
        "categories_context" : Category.objects.all(),
    }