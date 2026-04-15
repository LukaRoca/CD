import random
from collections import Counter

def fonte_simbolos(alfabeto, probabilidades, N):
    """
    Fonte de símbolos genérica.
    Gera uma sequência de N símbolos a partir de um alfabeto X,
    de acordo com as probabilidades p(x).
    """
    return random.choices(alfabeto, weights=probabilidades, k=N)

def testa_fonte_generica():
    alfabeto_teste = ['A', 'B', 'C', 'D']
    probabilidades_teste = [0.50, 0.25, 0.15, 0.10]
    N = 100000
    nome_ficheiro = 'teste_fonte_generica.txt'
    
    print(f"A gerar {N} símbolos...")
    
    sequencia_gerada = fonte_simbolos(alfabeto_teste, probabilidades_teste, N)
    
    with open(nome_ficheiro, 'w', encoding='utf-8') as f:
        f.write("".join(sequencia_gerada))
        
    print(f"Símbolos guardados no ficheiro '{nome_ficheiro}'.")
    
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

testa_fonte_generica()