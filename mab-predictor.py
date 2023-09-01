from mabwiser.mab import MAB, LearningPolicy, NeighborhoodPolicy
arms = ['Josh Allen', 'Patrick Mahomes', 'Lamar Jackson']
decisions = ['Josh Allen', 'Patrick Mahomes', 'Josh Allen']
rewards = [31.48, 17.3, 27.6]
mab = MAB(arms, LearningPolicy.UCB1(alpha=.25))
mab.fit(decisions, rewards)

"""
Build dictionary of team combos

{
teamId: 1
playerArray: ["ryan", "zhane", ..."name"...]
scoreArray: Weekly scores [100, 99, 120] need function to build
rewards: [0,0,0,1] possibly
}

Dictionary of chosen teams
{
teamIds: [1,45,2]
scoreArray: [140, 102, 99]
}


"""
print(mab.predict())