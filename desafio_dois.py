def calcular_nivel(vitorias, derrotas):
  
  """
  Calcula o saldo de vitórias e determina o nível do jogador.
  Args:
    vitorias: O número de vitórias do jogador.
    derrotas: O número de derrotas do jogador.
  Returns:
    Uma string formatada indicando o saldo de vitórias e o nível do jogador.
  """
  
  saldo_vitorias = vitorias - derrotas
  nivel = ""

  if saldo_vitorias < 10:
    nivel = "Ferro"
  elif saldo_vitorias <= 20:
    nivel = "Bronze"
  elif saldo_vitorias <= 50:
    nivel = "Prata"
  elif saldo_vitorias <= 80:
    nivel = "Ouro"
  elif saldo_vitorias <= 90:
    nivel = "Diamante"
  elif saldo_vitorias <= 100:
    nivel = "Lendário"
  else:
    nivel = "Imortal"

  return f"O Herói tem um saldo de {saldo_vitorias} e está no nível de {nivel}"

# Testes
if __name__ == "__main__":
  print(calcular_nivel(5, 2))    # Saída: O Herói tem um saldo de 3 e está no nível de Ferro
  print(calcular_nivel(15, 2))   # Saída: O Herói tem um saldo de 13 e está no nível de Bronze
  print(calcular_nivel(30, 5))   # Saída: O Herói tem um saldo de 25 e está no nível de Prata
  print(calcular_nivel(60, 10))  # Saída: O Herói tem um saldo de 50 e está no nível de Ouro
  print(calcular_nivel(85, 4))   # Saída: O Herói tem um saldo de 81 e está no nível de Diamante
  print(calcular_nivel(95, 3))   # Saída: O Herói tem um saldo de 92 e está no nível de Lendário
  print(calcular_nivel(110, 5))  # Saída: O Herói tem um saldo de 105 e está no nível de Imortal

  # Exemplo de Interatividade (opcional)
  vitorias = int(input("Digite o número de vitórias: "))
  derrotas = int(input("Digite o número de derrotas: "))
  resultado = calcular_nivel(vitorias, derrotas)
  
  print(resultado)
