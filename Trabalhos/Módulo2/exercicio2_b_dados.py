import random

def fonte_simbolos(alfabeto, probabilidades, N):
    return random.choices(alfabeto, weights=probabilidades, k=N)

def lanca_dois_dados():
    alfabeto = [1, 2, 3, 4, 5, 6]
    probabilidades = [1/6, 1/6, 1/6, 1/6, 1/6, 1/6] 
    
    return fonte_simbolos(alfabeto, probabilidades, 2)

def turno_jogador(nome_jogador):
    pontos_turno = 0
    registo = ""
    
    while True:
        dados = lanca_dois_dados()
        soma = sum(dados)
        pontos_turno += soma
        
        registo += f"  {nome_jogador} lançou {dados} (soma: {soma}). "
        
        if dados[0] == dados[1]:
            registo += "DUPLOS! Tem direito a jogar de novo.\n"
        else:
            registo += "\n"
            break
            
    return pontos_turno, registo

def simula_jogo(numero_do_jogo, L=10):
    registo_completo = f"=== JOGO DE DADOS #{numero_do_jogo} ({L} Jogadas) ===\n\n"
    pontos_A = 0
    pontos_B = 0
    
    for jogada in range(1, L + 1):
        registo_completo += f"--- Jogada {jogada} ---\n"
        
        pts_a, log_a = turno_jogador("Jogador A")
        pontos_A += pts_a
        registo_completo += log_a
        
        pts_b, log_b = turno_jogador("Jogador B")
        pontos_B += pts_b
        registo_completo += log_b
        
        registo_completo += "\n"
        
    registo_completo += "=== RESULTADO FINAL ===\n"
    registo_completo += f"Pontuação Total Jogador A: {pontos_A}\n"
    registo_completo += f"Pontuação Total Jogador B: {pontos_B}\n"
    
    if pontos_A > pontos_B:
        registo_completo += "-> VENCEDOR: Jogador A!\n"
    elif pontos_B > pontos_A:
        registo_completo += "-> VENCEDOR: Jogador B!\n"
    else:
        registo_completo += "-> EMPATE!\n"
        
    nome_ficheiro = f"registo_dados_jogo_{numero_do_jogo}.txt"
    with open(nome_ficheiro, 'w', encoding='utf-8') as f:
        f.write(registo_completo)
        
    print(f"Jogo {numero_do_jogo} concluído! Guardado em '{nome_ficheiro}'.")

print("A simular os jogos de dados...")
for i in range(1, 4):
    simula_jogo(numero_do_jogo=i, L=10)