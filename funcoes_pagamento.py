# Aumentar funções de pagamento
# Essa função recebe um valor, se o valor for menor ou igual a 0, então não tem nada pra pagar, não faz sentido efetuar o pagamento. Em qualquer outro caso, ele retorna que o pagamento deu certo.
# Se houver algum erro de valor, então da erro no pagamento. Tratamento de erro de novo.
def realizar_pagamento(valor, forma_pagamento):
    try:
        if valor <= 0:
            raise ValueError("O valor do pagamento deve ser positivo.")
        print(f"Pagamento de R${valor} realizado com sucesso via {forma_pagamento}.")
    except ValueError as e:
        print(f"Erro no pagamento: {e}")