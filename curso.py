
Python
def programa_bancario():
  
    entrada = input().strip()

    opcoes = {
        "Relatorio de juros em planilha Excel": "Calculo de juros sobre saldos usando colunas da planilha",
        "Tabela de clientes com limite de credito": "Lista dados de clientes e campo com limite de credito",
        "Consulta SQL de saldo por cliente": "Filtra tabela de contas para mostrar saldo de cada cliente",
        "Consulta SQL de historico de transacoes": "Usa SQL para buscar transacoes antigas de uma conta"
    }

    if entrada in opcoes:
        print(opcoes[entrada])
    else:
        print("Tecnica desconhecida")

# Executa o programa
programa_bancario()
