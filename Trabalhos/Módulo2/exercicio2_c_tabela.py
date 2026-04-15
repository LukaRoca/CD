import random
import math
import os

def fonte_simbolos(alfabeto, probabilidades, N):
    return random.choices(alfabeto, weights=probabilidades, k=N)

def carregar_lista(caminho):
    try:
        with open(caminho, 'r', encoding='utf-8') as f:
            return [linha.strip() for linha in f if linha.strip()]
    except UnicodeDecodeError:
        with open(caminho, 'r', encoding='latin-1') as f:
            return [linha.strip() for linha in f if linha.strip()]
    except FileNotFoundError:
        print(f"Erro: O ficheiro '{caminho}' não foi encontrado.")
        return ["Desconhecido"]

def gerar_tabela_pessoas(numero_ficheiro, quantidade=1000):
    pasta_recursos = 'Recursos' 
    
    nomes = carregar_lista(os.path.join(pasta_recursos, 'Nomes.txt'))
    apelidos = carregar_lista(os.path.join(pasta_recursos, 'Apelidos.txt'))
    localidades = carregar_lista(os.path.join(pasta_recursos, 'Localidades.txt'))
    profissoes = carregar_lista(os.path.join(pasta_recursos, 'Profissoes.txt'))
    
    prob_nomes = [1/len(nomes)] * len(nomes)
    prob_apelidos = [1/len(apelidos)] * len(apelidos)
    prob_locs = [1/len(localidades)] * len(localidades)
    prob_profs = [1/len(profissoes)] * len(profissoes)
    
    alfabeto_benford = [str(d) for d in range(1, 10)]
    prob_benford = [math.log10(1 + 1/d) for d in range(1, 10)]
    
    alfabeto_digitos = [str(d) for d in range(10)]
    prob_digitos = [0.1] * 10
    
    pasta_resultados = 'Resultados'
    os.makedirs(pasta_resultados, exist_ok=True)
    nome_ficheiro = os.path.join(pasta_resultados, f'tabela_pessoas_{numero_ficheiro}.csv')
    
    print(f"A gerar a tabela {numero_ficheiro} com {quantidade} registos...")
    
    with open(nome_ficheiro, 'w', encoding='utf-8') as f:
        f.write("ID;Nome;Localidade;Profissao\n")
        
        for _ in range(quantidade):
            prim_digito = fonte_simbolos(alfabeto_benford, prob_benford, 1)[0]
            resto_digitos = "".join(fonte_simbolos(alfabeto_digitos, prob_digitos, 7))
            id_final = prim_digito + resto_digitos
            
            p_nome = fonte_simbolos(nomes, prob_nomes, 1)[0]
            apelido = fonte_simbolos(apelidos, prob_apelidos, 1)[0]
            nome_completo = f"{p_nome} {apelido}"
            
            localidade = fonte_simbolos(localidades, prob_locs, 1)[0]
            profissao = fonte_simbolos(profissoes, prob_profs, 1)[0]
            
            # Escrever a linha
            f.write(f"{id_final};{nome_completo};{localidade};{profissao}\n")
            
    print(f"Ficheiro guardado em '{nome_ficheiro}'.")

for i in range(1, 4):
    gerar_tabela_pessoas(i, 1000)