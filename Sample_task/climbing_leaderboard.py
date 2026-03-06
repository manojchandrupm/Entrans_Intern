
def leaderboard(scores, alice):
    unique_scores = sorted(list(set(scores)), reverse=True)
    # print(unique_scores)
    ranking = []
    for a in alice:
        rank = 1
        for s in unique_scores:
            if a<s:
                rank += 1
            else:
                break
        ranking.append(rank)
    return ranking

no_of_score = int(input("Enter the no of player in leaderboard :"))
print("Enter the leaderboard scores in decreasing order :")
scores = []
for i in range(no_of_score):
    scores.append(int(input()))
no_of_game = int(input("Enter the no of game alice played :"))
print("Enter the Alice score in ascending order :")
alice_scores = []
for i in range(no_of_game):
    alice_scores.append(int(input()))

# scores = [100, 90, 90, 80, 75, 60]
# alice_scores = [50, 65, 77, 90]

res = leaderboard(scores, alice_scores)
print(res)