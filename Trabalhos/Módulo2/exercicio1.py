import math
import matplotlib.pyplot as plt
from collections import Counter
import os

def processa_ficheiros_automaticamente(pasta_origem, ficheiro_saida_txt):
    pasta_graficos = 'Graficos'
    os.makedirs(pasta_graficos, exist_ok=True)

    with open(ficheiro_saida_txt, 'w', encoding='utf-8') as f_out:
        f_out.write("=== RESULTADOS DA ANÁLISE DE FONTES DE SÍMBOLOS ===\n\n")

    if not os.path.exists(pasta_origem):
        print(f"Erro: A pasta '{pasta_origem}' não foi encontrada.")
        return

    print("A processar os ficheiros... Aguarda um momento.")
    
    for nome_ficheiro in os.listdir(pasta_origem):
        caminho_ficheiro = os.path.join(pasta_origem, nome_ficheiro)
        
        if not os.path.isfile(caminho_ficheiro):
            continue
            
        with open(caminho_ficheiro, 'rb') as f:
            dados = f.read()
            
        total_simbolos = len(dados)
        if total_simbolos == 0:
            continue

        frequencias = Counter(dados)
        
        simbolo_mais_frequente, contagem_max = frequencias.most_common(1)[0]
        prob_mais_frequente = contagem_max / total_simbolos
        info_propria = -math.log2(prob_mais_frequente)
        
        entropia = 0
        for simbolo, contagem in frequencias.items():
            prob = contagem / total_simbolos
            entropia += -prob * math.log2(prob)
            
        if 32 <= simbolo_mais_frequente <= 126:
            rep_simbolo = f"'{chr(simbolo_mais_frequente)}'"
        else:
            rep_simbolo = f"Hex: 0x{simbolo_mais_frequente:02x}"
            
        with open(ficheiro_saida_txt, 'a', encoding='utf-8') as f_out:
            f_out.write(f"--- Ficheiro: {nome_ficheiro} ---\n")
            f_out.write(f"Total de símbolos: {total_simbolos}\n")
            f_out.write(f"Símbolo mais frequente: {simbolo_mais_frequente} ({rep_simbolo})\n")
            f_out.write(f"Probabilidade: {prob_mais_frequente:.6f}\n")
            f_out.write(f"Informação própria: {info_propria:.6f} bits\n")
            f_out.write(f"Entropia da fonte: {entropia:.6f} bits/símbolo\n\n")
            
        eixo_x = list(range(256))
        eixo_y = [frequencias.get(i, 0) for i in eixo_x]
        
        plt.figure(figsize=(10, 5))
        plt.bar(eixo_x, eixo_y, color='royalblue', width=1.0)
        plt.title(f'Histograma de Símbolos - {nome_ficheiro}')
        plt.xlabel('Símbolo (Valor do Byte 0-255)')
        plt.ylabel('Frequência Absoluta')
        plt.xlim([0, 255])
        plt.grid(axis='y', linestyle='--', alpha=0.7)
        plt.tight_layout()
        
        caminho_imagem = os.path.join(pasta_graficos, f'histograma_{nome_ficheiro}.png')
        plt.savefig(caminho_imagem)
        plt.close()
        
        print(f"Processado: {nome_ficheiro}")

    print(f"\nConcluído! Os valores estão no ficheiro '{ficheiro_saida_txt}'.")
    print(f"Os gráficos foram guardados na pasta '{pasta_graficos}'.")

processa_ficheiros_automaticamente('TestFilesCD', 'resultados_exercicio1.txt')