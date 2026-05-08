from django.http import HttpResponse

def produto_view(request, id=None):
    if id is None:
        return HttpResponse("ID não fornecido")
    return HttpResponse(f"Produto ID: {id}")