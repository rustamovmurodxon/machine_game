def calculate_scores():
    print("O'yinchi 1 harakatlarini kiriting (masalan: share, steal):")
    L1 = input().strip().split(", ")
    print("O'yinchi 2 harakatlarini kiriting (masalan: share, steal):")
    L2 = input().strip().split(", ")

    player1_score = 3  
    player2_score = 3

   
    for action1, action2 in zip(L1, L2):
        if action1 == "share" and action2 == "share":
            player1_score += 2
            player2_score += 2
        elif action1 == "share" and action2 == "steal":
            player1_score += 0
            player2_score += 3
        elif action1 == "steal" and action2 == "share":
            player1_score += 3
            player2_score += 0
        elif action1 == "steal" and action2 == "steal":
            player1_score += 1
            player2_score += 1

    print("Natija: [", player1_score, ",", player2_score, "]")

calculate_scores()
