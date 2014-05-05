'''
This program simulates the Monty Hall problem and plots the avg prob
that the player wins WITH switching, over repetitions.  
'''

from __future__ import division
import random 
import matplotlib.pyplot as plt

# Set number of simulations: 
n = 500

# Determine number of times player wins when she does not switch, and when she does switch
def prizes(repetitions): 
	won_switch = 0 
	won_noswitch = 0
	for i in range(0,n):
		doors = ['goat', 'goat', 'car'] # Possible doors
		ch_player = doors.pop(random.randint(0, len(doors)-1)) # Player randomly chooses a door 
		ch_host = doors.pop(doors.index('goat')) # Host chooses a door with a goat behind it
		won_switch += 1 if doors[0] == 'car' else 0 # Player does switch; Count if she wins
		won_noswitch += 1 if ch_player == 'car' else 0 # Player doesn't switch; Count if she wins 
	return {'Switch prizes': won_switch, 'No switch prize': won_noswitch}

# Run the simulation yo!
print "Chance of winning if player does switch: " + '%2f'%((prizes(n))['Switch prizes']/n)
print "Chance of winning if player does NOT switch: " + '%2f'%((prizes(n))['No switch prize']/n)

# Plot the prob of winning when player DOES switch over repititions
def plotProb(repetitions): 
	xvals = []
	yvals = []
	avgs = []
	for i in range(0,repetitions): 
		won_switched =	((prizes(i))['Switch prizes'])/repetitions	
		xvals.append(i)
		yvals.append(won_switched)
		avgs.append(100*(sum(yvals)/len(yvals)))
	plt.plot(xvals, avgs)
	plt.ylabel('Avg prob of winning prize after switching')
	plt.xlabel('Number of repetitions')
	plt.title('Prob. of winning prize after switching over reps')
	plt.show()

#Plot the prob
plotProb(n)