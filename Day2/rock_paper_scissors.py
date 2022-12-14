import pprint
pp = pprint.pprint

file = "day2_input.txt"

# Part 1
with open(file) as f:
    lines = f.readlines()

options = {"A": 0, "X": 0, "B": 1, "Y": 1, "C": 2, "Z": 2}
outcome_options = {0: 3, 1: 0, 2: 6} # tie, lose, win

total_score = 0

for line in lines:
    # opponents choice is always first
    opponent_option = line[0]
    # my choice is always second
    player_option = line[2]

    # my score is always constant whether I win the match
    player_score = options[player_option]
    # outcome of the match score
    opponent_score = options[opponent_option]

    # calculate the outcome from opponent and player
    # modulo 3, based on three states tie, win, lose
    outcome = (opponent_score - player_score) % 3
    # then use the round outcome to look up in outcome_options
    outcome_score = outcome_options[outcome]

    # the round for the player will be always + 1 to counter the index position (1, 2, 3) to give value
    # the outcome_score is the points won for the round (0, 3, 6)
    round_score = (player_score + 1) + outcome_score

    total_score += round_score

print(total_score)

# Part 2
result_outcomes = {"X": 1, "Y": 0, "Z": 2}
result_scores = {"X": 0, "Y": 3, "Z": 6}

total_score = 0  # reset for reuse in part 2
for line in lines:
    # opponents choice is always first
    opponent_option = line[0]
    # the end state of the round mapped to end_states
    result_outcome = line[2]

    player_option = (options[opponent_option] - result_outcomes[result_outcome]) % 3
    round_score = (player_option + 1) + result_scores[result_outcome]
    total_score += round_score

print(total_score)







