from django.shortcuts import render, HttpResponse

html_base="""
<h1>Mi web Personal</h1>
<ul>
    <li><a href="/home">Portada</a></li>
    <li><a href="/about-me">Acerca de</a></li>
    <li><a href="/portfolio">Portfolio</a></li>
    <li><a href="/contact">Contact</a></li>
</ul>
"""

# Create your views here.
def home(request):
    return render(request,"core/home.html")

def about(request):
    return render(request,"core/about.html")

 
def contact(request):
    return render(request,"core/contact.html")

# def portfolio(request):
#     return HttpResponse(html_base + """
#                         <p>Este es mi primer portfolio</p>
#                         <p>Este es mi segundo portfolio</p>
#                         """)
    
# def contacto(request):
#     return HttpResponse(html_base + """
#                         <p>Lorem ipsum es el texto que se usa habitualmente en diseño gráfico en demostraciones de tipografías o
#                         de borradores de diseño para probar el diseño visual antes de insertar el texto final.</p>
#                         """)