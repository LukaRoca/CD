import random
import os

# A nossa fonte de símbolos (igual à alínea a)
def fonte_simbolos(alfabeto, probabilidades, N):
    return random.choices(alfabeto, weights=probabilidades, k=N)

# Função para gerar uma chave (5 Números + 2 Estrelas) sem repetidos
def gera_chave_euromilhoes():
    # 1. Gerar os 5 Números (1 a 50)
    alfabeto_num = list(range(1, 51))
    prob_num = [1/50] * 50
    numeros = set()
    
    while len(numeros) < 5:
        # Pede 1 símbolo de cada vez à fonte. O set() ignora se for repetido.
        simbolo = fonte_simbolos(alfabeto_num, prob_num, 1)[0]
        numeros.add(simbolo)
        
    # 2. Gerar as 2 Estrelas (1 a 12)
    alfabeto_est = list(range(1, 13))
    prob_est = [1/12] * 12
    estrelas = set()
    
    while len(estrelas) < 2:
        simbolo = fonte_simbolos(alfabeto_est, prob_est, 1)[0]
        estrelas.add(simbolo)
        
    # Devolve as listas ordenadas para ficar bonito
    return sorted(list(numeros)), sorted(list(estrelas))

# Função para verificar os acertos e atribuir o prémio
def verifica_premio(aposta, chave_vencedora):
    # Intersetar as duas listas para ver quantos coincidem
    num_certos = len(set(aposta[0]).intersection(set(chave_vencedora[0])))
    est_certos = len(set(aposta[1]).intersection(set(chave_vencedora[1])))
    
    # Tabela de prémios oficial (resumida)
    if num_certos == 5 and est_certos == 2: return "1º Prémio (5N + 2E)"
    elif num_certos == 5 and est_certos == 1: return "2º Prémio (5N + 1E)"
    elif num_certos == 5 and est_certos == 0: return "3º Prémio (5N + 0E)"
    elif num_certos == 4 and est_certos == 2: return "4º Prémio (4N + 2E)"
    elif num_certos == 4 and est_certos == 1: return "5º Prémio (4N + 1E)"
    elif num_certos == 3 and est_certos == 2: return "6º Prémio (3N + 2E)"
    elif num_certos == 4 and est_certos == 0: return "7º Prémio (4N + 0E)"
    elif num_certos == 2 and est_certos == 2: return "8º Prémio (2N + 2E)"
    elif num_certos == 3 and est_certos == 1: return "9º Prémio (3N + 1E)"
    elif num_certos == 3 and est_certos == 0: return "10º Prémio (3N + 0E)"
    elif num_certos == 1 and est_certos == 2: return "11º Prémio (1N + 2E)"
    elif num_certos == 2 and est_certos == 1: return "12º Prémio (2N + 1E)"
    elif num_certos == 2 and est_certos == 0: return "13º Prémio (2N + 0E)"
    else: return "Sem prémio"

# Função principal de simulação
def simula_jogo(num_ficheiro, N_apostas_por_semana=5000, semanas=4):
    pasta_resultados = 'Resultados'
    os.makedirs(pasta_resultados, exist_ok=True) # Garante que a pasta existe
    
    registo = f"=== SIMULAÇÃO EURO MILHÕES #{num_ficheiro} ===\n"
    registo += f"Semanas simuladas: {semanas} | Apostas do jogador por semana: {N_apostas_por_semana}\n\n"
    
    estatisticas_premios = {}
    
    # Simular o número de semanas pedido
    for semana in range(1, semanas + 1):
        chave_sorteada = gera_chave_euromilhoes()
        registo += f"--- SEMANA {semana} ---\n"
        registo += f"CHAVE VENCEDORA: Números {chave_sorteada[0]} | Estrelas {chave_sorteada[1]}\n"
        
        premios_da_semana = []
        
        # Gerar N apostas para o jogador nesta semana
        for _ in range(N_apostas_por_semana):
            aposta = gera_chave_euromilhoes()
            resultado = verifica_premio(aposta, chave_sorteada)
            
            if resultado != "Sem prémio":
                premios_da_semana.append((aposta, resultado))
                estatisticas_premios[resultado] = estatisticas_premios.get(resultado, 0) + 1
                
        registo += f"Total de prémios ganhos nas {N_apostas_por_semana} apostas: {len(premios_da_semana)}\n"
        
        # Registar as apostas que ganharam alguma coisa
        for p in premios_da_semana:
            registo += f"  -> Aposta Números {p[0][0]} | Estrelas {p[0][1]} ganhou o {p[1]}\n"
        registo += "\n"
        
    # Resumo final do ficheiro
    registo += "=== RESUMO TOTAL DOS PRÉMIOS ===\n"
    if not estatisticas_premios:
        registo += "Nenhum prémio ganho em toda a simulação. Que falta de sorte!\n"
    else:
        # Ordenar os prémios por nome
        for premio, quantidade in sorted(estatisticas_premios.items()):
            registo += f"{premio}: {quantidade} vezes\n"
            
    # Guardar no ficheiro dentro da pasta Resultados
    nome_ficheiro = f"registo_euromilhoes_{num_ficheiro}.txt"
    caminho_completo = os.path.join(pasta_resultados, nome_ficheiro)
    
    with open(caminho_completo, 'w', encoding='utf-8') as f:
        f.write(registo)
        
    print(f"Simulação {num_ficheiro} guardada em '{caminho_completo}'.")

# O professor pede a geração de 3 ficheiros para cada jogo.
# Vamos simular 3 ficheiros. Em cada ficheiro, passam-se 4 semanas, com 5000 apostas feitas por semana!
print("A realizar as simulações e a verificar os sorteios do Euro Milhões...")
for i in range(1, 4):
    simula_jogo(num_ficheiro=i, N_apostas_por_semana=5000, semanas=4)