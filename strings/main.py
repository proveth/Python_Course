# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line
# Assignment STRINGS

# Part 1 

# Players who scored
scoring_player_name_1 = "Ruud Gullit"
scoring_player_name_2 = "Marco van Basten"

# Minute of scoring
goal_0 = 32
goal_1 = 54

scorers = scoring_player_name_1 + " "+ str(goal_0) + ", " + scoring_player_name_2 +" "+ str(goal_1)

report = f"{scoring_player_name_1} scored in the {goal_0}nd minute\n{scoring_player_name_2} scored in the {goal_1}th minute"

# Print variables
print(scorers)
print(report)

# Part 2
player = "Marco van Basten"
first_name = player[:player.find(" ")]
last_name_len = len(player[player.find(" ")+1:])
name_short = player[:1]+". "+ player[player.find(" ")+1:]
chant = ((first_name +"! ") * (len(first_name)-1)) + f"{first_name }!"

# Check if last char is not space
good_chant = chant[-1] != " "

# Print variables
print(player)
print(first_name)
print(last_name_len)
print(name_short)
print(chant)
print(good_chant)

