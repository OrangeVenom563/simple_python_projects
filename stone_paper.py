import random

paper = '''                             
          _______
      ---'   ____)____
                ______)
                _______)
               _______)
      ---.__________)
'''

scissor = ''' 
          _______ 
      ---'   ____)____
                ______)
             __________)
            (____)
      ---.__(___)
 '''
rock = '''
          _______
      ---'   ____)
            (_____)
            (_____)
            (____)
      ---.__(___)
 '''

signs = [rock, paper, scissor]
op = input("Enter 0 for rock 1 for paper or 2 scissors ")
if (op != '0' and op != '1' and op != '2'):
    print('You\'ve Entered wrong input you loose')
else:
    op = int(op)
    print(f'Your sign{signs[op]}')
    sysop = random.randint(0, 2)
    print('system\'s sign ' + signs[sysop])

if(op == sysop):
    print('draw')
elif(op == 0 and sysop == 2):
    print('You win')
elif(sysop == 0 and op == 2):
    print('You loose')
elif(sysop > op):
    print('You loose')
else:
    print('You win')
