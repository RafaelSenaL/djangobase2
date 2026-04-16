# cadastro/context_processors.py

def global_context(request):
    return {
        'dono': 'Joca da Silva',
    }