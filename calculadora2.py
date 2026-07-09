while True:
  opcao = int(input(
  """---Calculadora de números reais---

0.Sair
1.Soma
2.Subtração
3.Multiplicação
4.Divisão

Digite uma opção (0/1/2/3/4): """))

  if opcao == 0:
    print("Programa encerrado")
    break
  elif opcao > 4:
    print("Opção inválida")
    continue

  numero1 = float(input("Digite o primeiro número: "))
  numero2 = float(input("Digite o segundo número: "))

  if opcao == 1:
    print(f"O resultado da soma é: {numero1 + numero2}")
  elif opcao == 2:
    print(f"O resultado da subtração é: {numero1 - numero2}")
  elif opcao == 3:
    print(f"O resultado da multiplicação é: {numero1 * numero2}")
  elif opcao == 4:
    if numero2 != 0:
      print(f"O resultado da divisão é: {numero1 / numero2}")
    else:
      print("Erro, divisão por zero. Escolha outro número")
     
