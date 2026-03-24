import random

# A nossa fonte de símbolos da alínea (a)
def fonte_simbolos(alfabeto, probabilidades, N):
    return random.choices(alfabeto, weights=probabilidades, k=N)

# Função para lançar dois dados usando a fonte de símbolos
def lanca_dois_dados():
    alfabeto = [1, 2, 3, 4, 5, 6]
    # Um dado não viciado tem 1/6 (aprox. 16.67%) de probabilidade para cada face
    probabilidades = [1/6, 1/6, 1/6, 1/6, 1/6, 1/6] 
    
    # Geramos N=2 símbolos (dois dados)
    return fonte_simbolos(alfabeto, probabilidades, 2)

# Simula o turno de um jogador (inclui a regra de voltar a jogar se tirar duplos)
def turno_jogador(nome_jogador):
    pontos_turno = 0
    registo = ""
    
    while True:
        dados = lanca_dois_dados()
        soma = sum(dados)
        pontos_turno += soma
        
        registo += f"  {nome_jogador} lançou {dados} (soma: {soma}). "
        
        # Verificar se são duplos (os dois dados são iguais)
        if dados[0] == dados[1]:
            registo += "DUPLOS! Tem direito a jogar de novo.\n"
        else:
            registo += "\n"
            break # Fim do turno, sai do ciclo
            
    return pontos_turno, registo

# Função principal do jogo
def simula_jogo(numero_do_jogo, L=10):
    registo_completo = f"=== JOGO DE DADOS #{numero_do_jogo} ({L} Jogadas) ===\n\n"
    pontos_A = 0
    pontos_B = 0
    
    for jogada in range(1, L + 1):
        registo_completo += f"--- Jogada {jogada} ---\n"
        
        # Turno Jogador A
        pts_a, log_a = turno_jogador("Jogador A")
        pontos_A += pts_a
        registo_completo += log_a
        
        # Turno Jogador B
        pts_b, log_b = turno_jogador("Jogador B")
        pontos_B += pts_b
        registo_completo += log_b
        
        registo_completo += "\n"
        
    # Apuramento do Vencedor
    registo_completo += "=== RESULTADO FINAL ===\n"
    registo_completo += f"Pontuação Total Jogador A: {pontos_A}\n"
    registo_completo += f"Pontuação Total Jogador B: {pontos_B}\n"
    
    if pontos_A > pontos_B:
        registo_completo += "-> VENCEDOR: Jogador A!\n"
    elif pontos_B > pontos_A:
        registo_completo += "-> VENCEDOR: Jogador B!\n"
    else:
        registo_completo += "-> EMPATE!\n"
        
    # Guardar o registo num ficheiro (conforme pede o enunciado)
    nome_ficheiro = f"registo_dados_jogo_{numero_do_jogo}.txt"
    with open(nome_ficheiro, 'w', encoding='utf-8') as f:
        f.write(registo_completo)
        
    print(f"Jogo {numero_do_jogo} concluído! Guardado em '{nome_ficheiro}'.")

# O professor pede 3 ficheiros resultantes (vamos simular 3 jogos com 10 jogadas cada)
print("A simular os jogos de dados...")
for i in range(1, 4):
    simula_jogo(numero_do_jogo=i, L=10)