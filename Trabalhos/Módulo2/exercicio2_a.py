import random
from collections import Counter

def fonte_simbolos(alfabeto, probabilidades, N):
    """
    Fonte de símbolos genérica.
    Gera uma sequência de N símbolos a partir de um alfabeto X,
    de acordo com as probabilidades p(x).
    """
    # random.choices devolve uma lista de tamanho k, pesada pelas probabilidades
    return random.choices(alfabeto, weights=probabilidades, k=N)

def testa_fonte_generica():
    # 1. Definir os dados de teste
    alfabeto_teste = ['A', 'B', 'C', 'D']
    probabilidades_teste = [0.50, 0.25, 0.15, 0.10] # A FMP tem de somar 1 (100%)
    N = 100000 # Vamos gerar 100 mil símbolos para a estatística ficar bem visível
    nome_ficheiro = 'teste_fonte_generica.txt'
    
    print(f"A gerar {N} símbolos...")
    
    # 2. Chamar a nossa fonte genérica
    sequencia_gerada = fonte_simbolos(alfabeto_teste, probabilidades_teste, N)
    
    # 3. Guardar num ficheiro de texto, como pede o enunciado
    with open(nome_ficheiro, 'w', encoding='utf-8') as f:
        f.write("".join(sequencia_gerada))
        
    print(f"Símbolos guardados no ficheiro '{nome_ficheiro}'.")
    
    # 4. Apresentar os resultados para mostrar o "funcionamento correto"
    contagem = Counter(sequencia_gerada)
    
    print("\n=== VALIDAÇÃO DA FONTE DE SÍMBOLOS ===")
    print(f"{'Símbolo':<10} | {'Prob. Pedida':<15} | {'Prob. Obtida':<15}")
    print("-" * 45)
    
    for i, simbolo in enumerate(alfabeto_teste):
        prob_pedida = probabilidades_teste[i]
        prob_obtida = contagem[simbolo] / N
        print(f"{simbolo:<10} | {prob_pedida:<15.4f} | {prob_obtida:<15.4f}")
        
    print("-" * 45)
    print("Como podes ver, a probabilidade obtida aproxima-se muito da pedida!\n")

# Executar o teste
testa_fonte_generica()