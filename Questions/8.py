"""
Ask number of games played in tournament. Ask the user number of games won and number of gam,es loss.
 Calculate number of tie and total points. (1 win = 4,points 1 tie = 2 points).
"""


games_played = int(input("Enter games_played = "))
games_won = int(input("Enter games_won = "))
games_lost = int(input("Enter games_lost = "))

games_tie = games_played-games_won-games_lost
print(f"games_ties = {games_tie}") 

Total_points = (games_won * 4) + (games_lost * 2)
print(Total_points)
 