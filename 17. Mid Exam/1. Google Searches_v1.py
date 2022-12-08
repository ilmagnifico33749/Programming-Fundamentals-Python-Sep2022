income_per_search = float(input())
number_of_users = int(input())

total_money_earned = 0

for user in range(1, number_of_users + 1):
    searches_of_user = int(input())
    money_earned = income_per_search * searches_of_user
    if user != 0 and user % 3 == 0:
        money_earned = money_earned * 3

    if searches_of_user <= 1:
        money_earned = 0

    elif searches_of_user > 5:
        money_earned = money_earned * 2

    total_money_earned += money_earned

print(f"Total money earned: {total_money_earned:.2f}")
