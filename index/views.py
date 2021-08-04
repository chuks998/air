from django.shortcuts import render

# defining the landing page view...
def main_page(request):
    template_name = 'index.html'
    return render(request, template_name)
