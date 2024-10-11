from sys import exit, intern
import random
import time
def sala_ouro(): 
  print("Esta sala está cheia de ouro. Quanto você pega?") 
  print("Digite um número para escolher a quantidade de ouro que você quer pegar.")
  escolha = input("> ")
  
  if escolha.isdigit():
    quanto = int(escolha)
  else: 
    inferno("Cara, aprenda a digitar um número.")
    
  if quanto < 50:
    print("Legal, você não é ganancioso!\nOlhando para o fim da sala você vê duas portas, qual das duas você irá abrir?")
    print("esquerda ou direita") 
    escolha = input("> ")
    if escolha == "esquerda": 
        sala_dragao()
    elif escolha == "direita": 
        ganhar_jogo()
  else: 
    inferno("Você é um ganancioso desgraçado!") 

def sala_urso():
  print("Há um urso aqui.")
  print("O urso tem um monte de mel.")
  print("O urso gordo está na frente de outra porta.")
  print("Ações disponíveis: 'pegar mel', 'provocar urso', 'abrir porta'.")  
  print("Como você vai mover o urso?") 
  urso_movido = False
  
  while True: 
    escolha = input("> ")
    if escolha == "pegar mel":
     inferno("O urso olha para você e então arranca sua cara.")
    elif escolha == "provocar urso" and not urso_movido: 
      print("O urso saiu da porta.")
      print("Agora você pode passar por ela.") 
      urso_movido = True
    elif escolha == "provocar urso" and urso_movido:
      inferno("O urso fica irritado e mastiga sua perna.") 
    elif escolha == "abrir porta" and urso_movido: 
      sala_ouro()
    else: 
      print("Não faço ideia do que isso significa. Tente novamente.")

def sala_cthulhu(): 
  print("Aqui você vê o grande mal Cthulhu.")
  print("Ele, isso, o que quer que seja, olha para você e você enlouquece.")
  print("Ações disponíveis: 'fugir', 'cabeça', 'porta da frente'.")
  time.sleep(1)
  print("Você foge para salvar sua vida ou come sua cabeça?")
  
  escolha = input("> ")
  if "porta da frente" in escolha: 
    sala_sacrificio()
  elif "cabeça" in escolha: 
    inferno("Bem, isso foi gostoso!")
  elif "fugir" in escolha:
    print("Você volta pela mesma porta que entrou, ainda se recuperando mentalmente.")
    inicio()
  else:
    print("Opção inválida. Tente novamente.")
    sala_cthulhu()

def sala_dragao():
  print("Mais a frente voce vê uma porta e decide abri-la\nVocê entra em uma sala e encontra um dragão gigantesco!")
  print("Ações disponíveis: 'lutar', 'fugir', 'oferecer ouro'.")
  escolha = input("> ")
  
  if escolha == "lutar":
    inferno("Você tenta lutar, mas o dragão é muito forte. Você é queimado.")
  elif escolha == "fugir":
    inicio()
  elif escolha == "oferecer ouro":
    print("O dragão aceita o ouro e permite que você passe. Você ganhou o jogo!")
    ganhar_jogo()
  else:
    print("Opção inválida. Tente novamente.")
    sala_dragao()

def sala_sacrificio():
  print("Você entra em uma sala ritualística. Há uma faca cerimonial no centro.")
  print("Ações disponíveis: 'sacrificar', 'fugir'.")
  escolha = input("> ")
  
  if escolha == "sacrificar":
    morto("Você se sacrifica... mas o ritual falha. Você é consumido pela escuridão.")
  elif escolha == "fugir":
    ganhar_jogo()
  else:
    print("Opção inválida. Tente novamente.")
    sala_sacrificio()

def inferno(mensagem):
  print(f"{mensagem} Bem-vindo ao inferno!")
  time.sleep(2)
  print("Aqui você deve lutar contra um demônio para ter uma chance de escapar.")
  time.sleep(2)
  print("Rolando um dado...")
  time.sleep(3)
  resultado = random.randint(1, 20)
  print(f"Você rolou um {resultado}.")
  if resultado >= 15:
    print("Você derrotou o demônio e escapou do inferno!")
    inicio()
  else:
    print("Você falhou em derrotar o demônio.")
    morto("Sua alma está perdida para sempre no inferno.")

def morto(porque):
  print(porque, "Você morre!") 
  exit(0)

def ganhar_jogo():
  print("Parabéns! Você completou o jogo com sucesso e saiu vitorioso!")
  exit(0)

def inicio(): 
  print("Você está em uma sala escura.")
  print("Há uma porta à sua direita e outra à sua esquerda.") 
  print("Ações disponíveis: 'esquerda', 'direita'.")
  print("Qual você escolhe?")
  
  escolha = input("> ")
  if escolha == "esquerda": 
    sala_urso()
  elif escolha == "direita": 
    sala_cthulhu()
  else: 
    inferno("Você tropeça na sala até morrer de fome.")

inicio()