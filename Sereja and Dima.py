# Read the number of cards
n = int(input())

# Read the list of card values
cards = list(map(int, input().split()))

# Initialize pointers for the left and right ends of the row
left = 0
right = n - 1

# Initialize scores for Sereja and Dima
sereja_score = 0
dima_score = 0

# Simulate the game
turn = 0  # 0 for Sereja's turn, 1 for Dima's turn
while left <= right:
    if cards[left] > cards[right]:
        chosen_card = cards[left]
        left += 1
    else:
        chosen_card = cards[right]
        right -= 1

    # Add the chosen card to the current player's score
    if turn == 0:
        sereja_score += chosen_card
    else:
        dima_score += chosen_card

    # Switch turns
    turn = 1 - turn

# Print the final scores
print(sereja_score, dima_score)