import random

options = ("piedra", "papel", "tijera")

computer_wins = 0
user_wins = 0
rounds = 1

while True:

  print('*' * 10)
  print('ROUND ', rounds)
  print('*' * 10)

  print('computer_wins', computer_wins)
  print('user_wins', user_wins)

  user = input("piedra, papel o tijera => ")
  user = user.lower()
  
  if not user in options:
    print("Esa opcion no es valida")
    continue
  
  computer = random.choice(options)
  
  print("user option =>", user)
  print("computer option =>", computer)
  
  if user == computer:
    print("Empate!")
  elif user == "piedra":
    if computer == "tijera":
      print("Piedra gana a tijera")
      print("User gano")
      user_wins += 1
    else:
      print("Papel gana a piedra")
      print("Computer gano")
      computer_wins +=1
  elif user == "papel":
    if computer == "piedra":
      print("Papel gana a piedra")
      print("User gano")
      user_wins += 1
    else:
      print("tijera gana a papel")
      print("Computer gano")
      computer_wins +=1
  elif user == "tijera":
    if computer == "papel":
      print("Tijera gana a papel")
      print("User gana")
      user_wins += 1
    else:
      print("Piedra gana a tijera")
      print("Computer gano")
      computer_wins +=1

  if computer_wins == 2:
    print('*' * 10)
    print("El ganador es la computadora")
    print('*' * 10)
    break
    
  if user_wins == 2:
    print('*' * 10)
    print("EL GANADOR ES EL USUARIO")
    print('*' * 10)
    break
    
  rounds += 1