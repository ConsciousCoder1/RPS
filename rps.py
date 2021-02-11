import random

def play():
  user = input("Hello! Ready? 'r' for rock, 'p' for paper, 's' for scissors..\nWhat is your choice?")
  computer = random.choice(['r', 'p', 's'])

  if user == computer:
    return "It's a tie!"

  # r > s, s > p, p > r
  if is_win(user, computer):
    return 'You won!'

  return 'You lost!'

def is_win(player, opponent):
  #return if the player wins
  if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
    return True

print(play())