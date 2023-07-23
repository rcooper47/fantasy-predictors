"""
based purely on fantasy points
based on fantasy points & other status
Halving Algorithm: Regret bound _, Mistake bound _

Write a program that predicts which QB you should select in each Week based on
Fantasy Points.

It chooses randomly in first week & then eliminates gradually after...But this is only good
for binary prediction

Later Version: 
- Graphs
- Comparison Across Algorithms
- Option to Make Roster Predictions (built of players)
"""
import numpy as np
import random
import math

player_list = ["Patrick Mahomes", "Josh Allen", "Marcus Mariota"]
player_dict = {
"Patrick Mahomes":[34.9, 17.3, 17.08, 23.36, 30.48, 19.62], 
"Josh Allen":[33.5, 29.68, 26.7, 23.52, 35.16, 26.36], 
"Marcus Mariota":[19.8, 13.44, 15.56, 3.86, 17.98, 24.16]
}
max_values = [34.9, 29.68, 26.7, 23.52, 35.16, 26.36]

def hedge_algorithm(player_list, player_dict, max_values, T):
	"""
	Inputs: player_list: list<Player Names>, 
	player_dict: dict{Player Name:list<Scores>}, 
	max_values: list<Scores>, T: # rounds

	Outputs: alg_loss: (Float) Loss of Alogirithm, 
	predictions_made: list<Predicted Names>, 
	weights: list<Predictor Weights>
	"""
	n = len(player_list)
	weights = [1] * n
	loss = [0] * n
	alg_loss = 0
	epsilon = math.sqrt(math.log2(n)/T)
	predictions_made = []
	
	for round in range(T):
		#pick based on probability
		print(weights)
		random_selection, selected_i = pick_randomly(player_list, weights)
		print(round, max_values)
		predictions_made.append(random_selection)
		max_value = max_values[round]
		print(random_selection)
		actual_value = player_dict[random_selection][round]
		print(actual_value)
		updated_loss = incur_loss(loss[selected_i], max_value, actual_value)
		alg_loss += updated_loss
		loss = [0] * n
		loss[selected_i] = updated_loss
		weights = update_weights(weights, epsilon, loss, 40)
		
	return alg_loss, predictions_made, weights

def pick_randomly(player_list, weights):
	"""
	Output: Name of player chosen, Index of player chosen
	"""
	sum_of_weights = sum(weights)
	probabilities = [weight_i / sum_of_weights for weight_i in weights]
	choice = random.choices(player_list, weights = probabilities, k=1)
	return choice[0], player_list.index(choice[0])

def update_weights(weights, epsilon, loss, L):
	"""
	Output: Weights updated according to Formula
	"""
	weights = [weights[weight_i]*(1-(epsilon*loss[weight_i])/L) for weight_i in range(len(weights))]
	return weights

def incur_loss(loss, max_value, actual_value):
	"""
	Output: Loss incurred from choosing Choice
	TODO: UPDATE LOSS FUNC, UPDATE CUMULATIVE LOSS, L
	"""
	return  (1 * actual_value) - max_value


"""
TEST BASED ON MATHEMATICAL GUARANTEES & FANTASY FOOTBALL KNOWLEDGE
"""


def lineup_builder(rostered_players, lineup_rules):
	"""
	[{name: '', position: '', [points_i]}]
	Input: List of All players on roster, Lineup Rules
	Position, Weekly Points, Max Points Possible

	{QB: 1, RB: 3,...}
	Output: All unique lineups?
	[Lineup A, Lineup B], [200,130], [["mahomes", "kelce"],["justin jefferson","josh allen"]]
	"""
	"""
	import itertools

	for comb in itertools.combinations([1, 2, 3, 4], 3):
    	print(comb)

    for comb in itertools.combinations(["jettas", "davante", "cooper", "tyreek"], 3 (wrs in lineup):
    	print(comb)
    	add comb to lineup. do this for each position based on rules
    	for flex, add if flex eligible and not present in lineup
	"""
	qbs, rbs, wrs, tes = positional_sorter(rostered_players)
	






def positional_sorter(rostered_players):
	#add players to positional list
	qbs = []
	rbs = []
	wrs = []
	tes = []
	flex = []
	kicker = []
	for player in rostered_players:
		if player["position"] == "QB":
			qbs.append(player["name"])
		if player["position"] == "RB":
			rbs.append(player["name"])
		if player["position"] == "WR":
			wrs.append(player["name"])
		if player["position"] == "TE":
			tes.append(player["name"])
	return qbs, rbs, wrs, tes


print(hedge_algorithm(player_list, player_dict, max_values, 6))
