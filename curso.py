

1. Por que o link do NotebookLM não funciona?
Como mostram as suas imagens, você está tentando colar um link do Google NotebookLM em um campo que exige um repositório de projeto. Esses sistemas geralmente só aceitam links do GitHub, GitLab ou Bitbucket.

Se você precisa entregar o código do desafio mostrado na última imagem, você deve hospedar esse código no GitHub.

2. Resolução do Desafio (Python)
Baseado na descrição do desafio de Excel e SQL no contexto bancário, aqui está o código em Python que você deve salvar e enviar para o seu repositório:

Python
def programa_bancario():
    # Lê a entrada do usuário
    entrada = input().strip()

    # Dicionário mapeando as entradas para as saídas correspondentes
    opcoes = {
        "Relatorio de juros em planilha Excel": "Calculo de juros sobre saldos usando colunas da planilha",
        "Tabela de clientes com limite de credito": "Lista dados de clientes e campo com limite de credito",
        "Consulta SQL de saldo por cliente": "Filtra tabela de contas para mostrar saldo de cada cliente",
        "Consulta SQL de historico de transacoes": "Usa SQL para buscar transacoes antigas de uma conta"
    }

    # Verifica se a entrada existe no dicionário e imprime a resposta
    if entrada in opcoes:
        print(opcoes[entrada])
    else:
        print("Tecnica desconhecida")

# Executa o programa
programa_bancario()
