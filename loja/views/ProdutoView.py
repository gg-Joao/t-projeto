from django.http import JsonResponse, HttpResponse
from django.utils import timezone
from datetime import timedelta, datetime

from ..models import Produto


def produto_view(request):
    # 2. Capturar parâmetros da URL
    produto = request.GET.get('produto')
    destaque = request.GET.get('destaque')
    promocao = request.GET.get('promocao')
    categoria = request.GET.get('categoria')
    fabricante = request.GET.get('fabricante')
    pid = request.GET.get('id')
    dias = request.GET.get('dias')

    # 4. Primeira consulta ORM
    produtos_qs = Produto.objects.all()

    # 5. Mostrar resultado no terminal
    print('Produtos (inicial):', produtos_qs)

    # 9. Mostrar parâmetros recebidos
    if produto is not None:
        print('param produto =', produto)
    if destaque is not None:
        print('param destaque =', destaque)
    if promocao is not None:
        print('param promocao =', promocao)
    if categoria is not None:
        print('param categoria =', categoria)
    if fabricante is not None:
        print('param fabricante =', fabricante)
    if pid is not None:
        print('param id =', pid)
    if dias is not None:
        print('param dias =', dias)

    # 11-13. Filtrar dinamicamente usando parâmetros
    # filtrar por id
    if pid:
        produtos_qs = produtos_qs.filter(id=pid)

    # filtrar por nome do produto (partial search usando contains)
    if produto:
        produtos_qs = produtos_qs.filter(nome__icontains=produto)

    # filtros de booleano promocao/destaque
    def str_to_bool(s):
        if s is None:
            return None
        s = s.lower()
        if s in ('1', 'true', 't', 'yes', 'y'):
            return True
        if s in ('0', 'false', 'f', 'no', 'n'):
            return False
        return None

    promocao_bool = str_to_bool(promocao)
    destaque_bool = str_to_bool(destaque)
    if promocao_bool is not None:
        produtos_qs = produtos_qs.filter(promocao=promocao_bool)
    if destaque_bool is not None:
        produtos_qs = produtos_qs.filter(destaque=destaque_bool)

    # filtro por nome de categoria e fabricante (assumindo foreign keys com campo 'nome')
    if categoria:
        produtos_qs = produtos_qs.filter(categoria__nome__iexact=categoria)
    if fabricante:
        produtos_qs = produtos_qs.filter(fabricante__nome__iexact=fabricante)

    # 23-26. filtro por dias (produtos cadastrados nos últimos N dias)
    if dias:
        try:
            dias_int = int(dias)
            cutoff = timezone.now() - timedelta(days=dias_int)
            # assume que há campo 'created' ou 'created_at' ou 'data_criacao' — tentamos alguns
            if hasattr(Produto, 'created'):
                produtos_qs = produtos_qs.filter(created__gte=cutoff)
            elif hasattr(Produto, 'created_at'):
                produtos_qs = produtos_qs.filter(created_at__gte=cutoff)
            elif hasattr(Produto, 'data_criacao'):
                produtos_qs = produtos_qs.filter(data_criacao__gte=cutoff)
            else:
                print('Nenhum campo de data conhecido em Produto para filtro por dias')
        except ValueError:
            print('param dias inválido:', dias)

    # 6/8/10/12 etc: mostrar resultados e primeiro()
    print('Produtos (final queryset):', produtos_qs)
    primeiro = produtos_qs.first()
    print('Primeiro produto:', primeiro)

    # Serializar resultados para resposta (valores básicos)
    produtos_list = list(produtos_qs.values())

    return JsonResponse({'count': len(produtos_list), 'produtos': produtos_list})
from django.http import HttpResponse

def produto_view(request, id=None):
    if id is None:
        return HttpResponse("ID não fornecido")
    return HttpResponse(f"Produto ID: {id}")