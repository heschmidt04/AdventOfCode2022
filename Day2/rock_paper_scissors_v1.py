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
end_states = {"Y": 3, "X": 0, "Z": 6}# tie, lose, win

total_score = 0 # reset for reuse in part 2
for line in lines:
    # opponents choice is always first
    opponent_option = line[0]
    # the end state of the round mapped to end_states
    end_state = line[2]

    # nine if statements way
    # 1 = rock
    # 2 = paper
    # 3 = scissors
    if opponent_option == "A": # rock
        if end_state == "X":   # require a loss
            player_score = 3   # scissors beaten by rock
        elif end_state == "Y": # require a tie
            player_score = 1   # two rocks collide
        else:
            player_score = 2 # win! paper over rock
    elif opponent_option == "B": # paper
        if end_state == "X":     # require a loss
            player_score = 1     # rock sits on paper
        elif end_state == "Y":   # require a tie
            player_score = 2     # paper and paper
        else:
            player_score = 3     # win! scissors cuts paper
    else: # scissors
        if end_state == "X":   # require a loss
            player_score = 2   #  paper is cut by scissors
        elif end_state == "Y": # require a tie
            player_score = 3   # scissors and scissors
        else:
            player_score = 1   # win! rocks beat scissors

    round_score = end_states[end_state] + player_score

    total_score += round_score

print(total_score)







