# ---
# title: Prisoners and Cards Problem
# tags: [CodingChallenges, Python, Logic, PigeonholePrinciple]
# created: '2023-11-19'
# ---

# ## Problem Description

# Five prisoners are standing in a line, each given a card from a shuffled deck of 52 standard playing cards. The first prisoner can see everyone's cards except his own, and the last prisoner can only see his own card. If the last prisoner can correctly guess his card, all prisoners are set free. The prisoners can have a meeting before the cards are distributed. What should be their strategy?

# ## Constraints

# - The deck of cards is standard with 52 cards, 13 of each suit: Club, Spade, Heart, Diamond.
# - Each card is represented as a string with the suit followed by the card's number (e.g., 'Club1', 'Spade13').

# ## Solution

# The solution strategy is based on the pigeonhole principle and the prisoners' ability to communicate through the arrangement of their cards.

# Here's the Python code for this problem:

# ```python
import random
import itertools

def extract_number(card):
  return int(''.join(filter(str.isdigit, card)))

def extract_suit(card):
  return ''.join(filter(str.isalpha, card))

def solution():
  p1_card = p2_card = p3_card = p4_card = p5_card = '' # prisoner's card
  
  # Create a sorted deck of cards that can be numbered from 0 to 52.
  deck = [suit + str(number) for number in range(1, 14) for suit in ['Club', 'Spade', 'Heart', 'Diamond']]
  
  # Randomly draw 5 cards.
  drawn_cards = random.sample(deck, 5)
  original_cards = drawn_cards[:]

  # Find two cards with the same suit.
  suit_dict = {}
  for i, card in enumerate(drawn_cards):
    suit = extract_suit(card)
    suit_dict.setdefault(suit, []).append(i)

  for val in suit_dict.values():
    if len(val) >= 2:
      card_A = drawn_cards[val[0]]
      card_B = drawn_cards[val[1]]
      drawn_cards.remove(card_A)
      drawn_cards.remove(card_B)
      break

  # Ensure minimum distance between cards A and B is always <= 6.
  num_diff = abs(extract_number(card_A) - extract_number(card_B))
  sorted_cards = sorted([card_A, card_B], key=extract_number)
  if num_diff >= 7:
    num_diff = 13 - num_diff
    p1_card = sorted_cards[1]
  else:
    p1_card = sorted_cards[0]

  # Determine the order of prisoner's 2, 3, 4 cards according to the distance between cards A and B.
  perms = list(itertools.permutations([1, 2, 3]))
  order = perms[num_diff - 1]
  sorted_nums = sorted([deck.index(x) for x in drawn_cards])
  p2_card, p3_card, p4_card = [deck[sorted_nums[order[i] - 1]] for i in range(3)]
      
  # The suit of prisoner 5's card is the same as that of prisoner 1, and the number is obtained as described.
  candidate_num = extract_number(p1_card) + (perms.index(order) + 1)
  p5_card = extract_suit(p1_card) + str(candidate_num if 0 < candidate_num <= 13 else abs(13 - candidate_num))

  final_result = [p1_card, p2_card, p3_card, p4_card, p5_card]
  
  return [[original_cards, final_result], set(final_result) == set(original_cards)]

print(solution())
