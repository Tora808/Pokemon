from random import randint

ashscore = 0
teamrocketscore = 0
ties = 0

def ash():
	ash = input('Are you a boy or are you a girl?')
	if ash == 'boy':
		print('Welcome to the world of pokemon rps version')
	else:
		print('Ash blacked out')
		return ash
	professoroak = input('do you choose squirtle, bulbasaur, or charmander? ')
	return professoroak

def teamrocket():
	trainer = randint(0,2) 
	if trainer == 0:
		return 'bulbasaur'
	if trainer == 1:
		return 'charmander'
	if trainer == 2:
		return 'squirtle'
	


def battle(ash,teamrocket):
	global ties,ashscore,teamrocketscore
	if ash == teamrocket:
		print('both players are out of usable pokemon the match is a draw')
		ties += 1 
	if ash == "charmander" and teamrocket == "bulbasaur":
		print('were blasting off again!')
		ashscore += 1
	if ash == "charmander" and teamrocket == "squirtle":
		print('Ash is out of useable pokemon, you pay 400$ for loosing... ash blacked out!')
		teamrocketscore += 1
	if ash == "bulbasaur" and teamrocket == "squirtle":
		print('were blasting off again!')
		ashscore += 1
	if ash == "bulbasaur" and teamrocket == "charmander":
		print('Ash is out of useable pokemon, you pay 400$ for loosing... ash blacked out!')
		teamrocketscore += 1
	if ash == "squirtle" and teamrocket == "charmander":
		print('were blasting off again!')
		ashscore += 1
	if ash == "squirtle" and teamrocket == "bulbasaur":
		print('Ash is out of useable pokemon, you pay 400$ for loosing... ash blacked out!')
		teamrocketscore += 1
def gary():
	while(True): 
		ashchoice = ash()
		teamrocketchoice = teamrocket()
		battle(ashchoice,teamrocketchoice)
		gary = input('do you want to play again? yes/no?')
		if gary == 'no':
			print('ashscore: %s, teamrocketsscore: %s, ties: %s' % (ashscore,teamrocketscore,ties))
			break
gary()
