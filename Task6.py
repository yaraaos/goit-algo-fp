items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

def greedy_algorithm(items, budget):
    sorted_items = sorted(items.items(), key=lambda x: x[1]['calories']/x[1]['cost'], reverse=True)
    selected_items = []
    total_calories = 0
    total_cost = 0

    for item, data in sorted_items:
        if total_cost + data['cost'] <= budget:
            selected_items.append(item)
            total_cost += data['cost']
            total_calories += data['calories']

    return selected_items, total_calories

def dynamic_programming(items, budget):
    n = len(items)
    dp = [[0] * (budget + 1) for _ in range(n + 1)]
    item_list = list(items.items())

    for i in range(1, n + 1):
        item_name, item_data = item_list[i - 1]
        for w in range(1, budget + 1):
            if item_data['cost'] <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - item_data['cost']] + item_data['calories'])
            else:
                dp[i][w] = dp[i - 1][w]

    result = []
    w = budget
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            result.append(item_list[i - 1][0])
            w -= item_list[i - 1][1]['cost']

    return result, dp[n][budget]

budget = 100
print(greedy_algorithm(items, budget))
print(dynamic_programming(items, budget))
