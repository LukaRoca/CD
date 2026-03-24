import random
import string
import os

# A nossa fonte de símbolos
def fonte_simbolos(alfabeto, probabilidades, N):
    return random.choices(alfabeto, weights=probabilidades, k=N)

# Alfabetos base para as passwords
letras_min = list(string.ascii_lowercase)
letras_mai = list(string.ascii_uppercase)
numeros = list(string.digits)
especiais = list("!@#$%^&*()-_=+[]{}|;:,.<>?")

def gerar_password(nivel):
    if nivel == "baixo":
        # Critério: Apenas minúsculas, 6 caracteres
        alfabeto = letras_min
        N = 6
    elif nivel == "medio":
        # Critério: Minúsculas + Maiúsculas + Números, 8 caracteres
        alfabeto = letras_min + letras_mai + numeros
        N = 8
    elif nivel == "alto":
        # Critério: Todos os caracteres, 14 caracteres
        alfabeto = letras_min + letras_mai + numeros + especiais
        N = 14
    else:
        return ""
        
    # Probabilidades equiprováveis para o alfabeto escolhido
    probabilidades = [1/len(alfabeto)] * len(alfabeto)
    
    # Gerar a password usando a fonte de símbolos e juntar a lista numa string
    sequencia = fonte_simbolos(alfabeto, probabilidades, N)
    return "".join(sequencia)

def gerar_ficheiro_passwords(nivel, quantidade=1000):
    pasta_resultados = 'Resultados'
    os.makedirs(pasta_resultados, exist_ok=True)
    
    nome_ficheiro = f"passwords_nivel_{nivel}.txt"
    caminho_completo = os.path.join(pasta_resultados, nome_ficheiro)
    
    print(f"A gerar {quantidade} passwords de nível {nivel.upper()}...")
    
    # Criar e escrever as 1000 passwords
    with open(caminho_completo, 'w', encoding='utf-8') as f:
        f.write(f"=== PASSWORDS DE NÍVEL {nivel.upper()} ===\n")
        f.write("Critérios:\n")
        if nivel == "baixo": f.write("- Apenas letras minúsculas\n- Tamanho: 6\n\n")
        elif nivel == "medio": f.write("- Letras minúsculas, maiúsculas e números\n- Tamanho: 8\n\n")
        elif nivel == "alto": f.write("- Letras (min/mai), números e especiais\n- Tamanho: 14\n\n")
        
        for _ in range(quantidade):
            pwd = gerar_password(nivel)
            f.write(pwd + "\n")
            
    print(f"Ficheiro guardado em '{caminho_completo}'.\n")

# Gerar os 3 ficheiros pedidos (Baixo, Médio, Alto), cada um com 1000 linhas
gerar_ficheiro_passwords("baixo", 1000)
gerar_ficheiro_passwords("medio", 1000)
gerar_ficheiro_passwords("alto", 1000)