"""
based purely on fantasy points
based on fantasy points & other status
Halving Algorithm: Regret bound _, Mistake bound _

Write a program that predicts which QB you should select in each Week based on
Fantasy Points.

It chooses randomly in first week & then eliminates gradually after...But this is only good
for binary prediction

new loss value each round
"""
import numpy as np
import random



def hedge_algorithm(player_list, all_values, max_values):
	n = len(input)
	T = 18
	weights = [1] * n
	loss = [0] * n
	alg_loss = 0
	epsilon = sqrt(log(n)/T)
	
	for round in range(T):
		#pick based on probability
		random_selection, selected_i = pick_randomly(player_list, weights)
		updated_loss = incur_loss(loss[loss_i])
		alg_loss += updated_loss
		loss = [0] * n
		loss[selected_i] = updated_loss
		weights = update_weights(weights, epsilon, loss, 55)
		
	return

def pick_randomly(player_list, weights):
	sum_of_weights = sum(weights)
	probabilities = [weight_i / sum_of_weights for i in weights]
	choice = random.choices(player_list, weights = probabilities, k=1)
	return choice[0], player_list.index(choice[0])

def update_weights(weights, epsilon, loss, L):
	weights = [weights[weight_i]*(1-(epsilon*loss[weight_i])/L) for weight_i in range(len(weights))]
	return

def incur_loss(loss, max_value, actual_value):
	return max_value - weight * actual_value