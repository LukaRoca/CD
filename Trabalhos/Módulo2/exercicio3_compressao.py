import os
import time
import math
import zipfile
import matplotlib.pyplot as plt
from collections import Counter

def calcular_entropia(caminho):
    with open(caminho, 'rb') as f:
        dados = f.read()
    
    tamanho = len(dados)
    if tamanho == 0:
        return 0, tamanho
        
    frequencias = Counter(dados)
    entropia = 0
    for contagem in frequencias.values():
        prob = contagem / tamanho
        entropia -= prob * math.log2(prob)
        
    return entropia, tamanho

def analisa_e_comprime(caminho_ficheiro):
    nome_ficheiro = os.path.basename(caminho_ficheiro)
    pasta_trabalho = 'Resultados/Compressao'
    os.makedirs(pasta_trabalho, exist_ok=True)
    
    caminho_zip = os.path.join(pasta_trabalho, f"{nome_ficheiro}.zip")
    caminho_extraido = os.path.join(pasta_trabalho, f"extraido_{nome_ficheiro}")
    
    # 1. Calcular Entropia e Tamanho Original
    entropia, tam_original = calcular_entropia(caminho_ficheiro)
    if tam_original == 0:
        return None
        
    # 2. Comprimir (Medir Tempo)
    inicio_comp = time.time()
    with zipfile.ZipFile(caminho_zip, 'w', zipfile.ZIP_DEFLATED) as zf:
        # Guarda o ficheiro no ZIP apenas com o seu nome (sem as pastas todas atrás)
        zf.write(caminho_ficheiro, arcname=nome_ficheiro)
    tempo_comp = time.time() - inicio_comp
    
    # 3. Descomprimir (Medir Tempo)
    inicio_decomp = time.time()
    with zipfile.ZipFile(caminho_zip, 'r') as zf:
        # Extrai o ficheiro para uma pasta temporária e muda-lhe o nome
        zf.extract(nome_ficheiro, path=pasta_trabalho)
        os.rename(os.path.join(pasta_trabalho, nome_ficheiro), caminho_extraido)
    tempo_decomp = time.time() - inicio_decomp
    
    # 4. Verificar se são iguais (Original vs Descomprimido)
    with open(caminho_ficheiro, 'rb') as f1, open(caminho_extraido, 'rb') as f2:
        sao_iguais = (f1.read() == f2.read())
        
    # 5. Calcular Métricas de Compressão
    tam_comprimido = os.path.getsize(caminho_zip)
    # Compressão em bits por byte = (Tamanho Comprimido em bits) / (Tamanho Original em bytes)
    bits_por_byte = (tam_comprimido * 8) / tam_original
    razao_compressao = tam_original / tam_comprimido
    
    # Limpar o ficheiro extraído para não ocupar espaço desnecessário
    if os.path.exists(caminho_extraido):
        os.remove(caminho_extraido)
        
    return {
        'nome': nome_ficheiro,
        'entropia': entropia,
        'tam_orig': tam_original,
        'tam_comp': tam_comprimido,
        'bits_byte': bits_por_byte,
        'razao': razao_compressao,
        't_comp': tempo_comp,
        't_decomp': tempo_decomp,
        'iguais': sao_iguais
    }

def executar_exercicio_3():
    # Vamos criar uma lista com ficheiros do Professor e alguns que gerámos
    pasta_testes = 'TestFilesCD'
    pasta_resultados = 'Resultados'
    
    ficheiros_a_testar = []
    
    # Adicionar ficheiros do professor
    if os.path.exists(pasta_testes):
        for f in os.listdir(pasta_testes):
            caminho = os.path.join(pasta_testes, f)
            if os.path.isfile(caminho):
                ficheiros_a_testar.append(caminho)
                
    # Adicionar 3 ficheiros gerados por nós (ex: a tabela de pessoas e os registos)
    extra_files = ['tabela_pessoas_1.csv', 'passwords_nivel_alto.txt', 'registo_dados_jogo_1.txt']
    for f in extra_files:
        caminho = os.path.join(pasta_resultados, f)
        if os.path.exists(caminho):
            ficheiros_a_testar.append(caminho)

    print("A iniciar testes de compressão (WinZip / Deflate)...\n")
    
    lista_entropias = []
    lista_bits_byte = []
    
    # Tabela de resultados na consola
    print(f"{'Ficheiro':<25} | {'Entropia':<8} | {'Bits/Byte':<9} | {'Razão':<7} | {'T. Comp(s)':<10} | {'Iguais?'}")
    print("-" * 80)
    
    for caminho in ficheiros_a_testar:
        res = analisa_e_comprime(caminho)
        if res:
            print(f"{res['nome']:<25} | {res['entropia']:<8.4f} | {res['bits_byte']:<9.4f} | {res['razao']:<7.2f} | {res['t_comp']:<10.4f} | {'Sim' if res['iguais'] else 'NÃO'}")
            
            # Guardar valores para o gráfico
            lista_entropias.append(res['entropia'])
            lista_bits_byte.append(res['bits_byte'])
            
    print("-" * 80)
    
    # 6. Gerar o gráfico Entropia vs Compressão (bits/byte)
    plt.figure(figsize=(10, 6))
    plt.scatter(lista_entropias, lista_bits_byte, color='red', marker='o')
    plt.title('Relação entre Entropia e Compressão (WinZip/Deflate)')
    plt.xlabel('Entropia do Ficheiro (bits/símbolo)')
    plt.ylabel('Compressão Obtida (bits/byte)')
    plt.grid(True, linestyle='--', alpha=0.7)
    
    # Linha de referência (y = x). Num compressor ideal, bits/byte ~= entropia
    min_x, max_x = min(lista_entropias), max(lista_entropias)
    plt.plot([min_x, 8], [min_x, 8], color='blue', linestyle='--', label='Compressão Ideal Teórica (bits/byte = Entropia)')
    plt.legend()
    
    # Guardar o gráfico
    caminho_grafico = 'Resultados/grafico_compressao_entropia.png'
    plt.savefig(caminho_grafico)
    print(f"\nGráfico guardado em '{caminho_grafico}'.")
    plt.show()

# Correr o exercício
executar_exercicio_3()