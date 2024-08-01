"""Порівняння жадібного алгоритму та алгоритму динамічного програмування 
для задачі видачі решти."""

import time

def find_coins_greedy(amount):
    """Жадібний алгоритм для знаходження монет для розмінювання суми amount."""
    # Номінали монет
    coins = [50, 25, 10, 5, 2, 1]
    # Результат, словник для зберігання кількості кожного номіналу
    result = {coin: 0 for coin in coins}

    # Жадібний алгоритм
    for coin in coins:
        while amount >= coin:
            amount -= coin
            result[coin] += 1

    # Повертаємо лише ті номінали, що використовувалися
    return {k: v for k, v in result.items() if v > 0}

def find_min_coins(amount):
    """Алгоритм динамічного програмування для знаходження мінімальної 
    кількості монет для розмінювання суми amount."""
    # Номінали монет
    coins = [50, 25, 10, 5, 2, 1]
    # Створення масиву для зберігання мінімальної кількості монет для кожної суми
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0  # Для суми 0 потрібно 0 монет
    # Масив для відстеження вибраних монет
    coin_count = [{} for _ in range(amount + 1)]

    # Алгоритм динамічного програмування
    for i in range(1, amount + 1):
        for coin in coins:
            if i - coin >= 0 and dp[i - coin] + 1 < dp[i]:
                dp[i] = dp[i - coin] + 1
                coin_count[i] = coin_count[i - coin].copy()
                if coin in coin_count[i]:
                    coin_count[i][coin] += 1
                else:
                    coin_count[i][coin] = 1

    return coin_count[amount]

def compare_algorithms(amount):
    """Порівняння жадібного алгоритму та алгоритму динамічного програмування"""
    start_greedy = time.time()
    greedy_result = find_coins_greedy(amount)
    end_greedy = time.time()
    greedy_time = end_greedy - start_greedy

    start_dp = time.time()
    dp_result = find_min_coins(amount)
    end_dp = time.time()
    dp_time = end_dp - start_dp

    return greedy_result, dp_result, greedy_time, dp_time

if __name__ == "__main__":
    amount = 113
    greedy_result, dp_result, greedy_time, dp_time = compare_algorithms(amount)
    print("Результат жадібного алгоритму:", greedy_result)
    print("Результат алгоритму динамічного програмування:", dp_result)
    print("Час виконання жадібного алгоритму: {:.6f} секунд".format(greedy_time))
    print("Час виконання алгоритму динамічного програмування: {:.6f} секунд".format(dp_time))

    # Велика сума для порівняння
    large_amount = 10000
    greedy_result, dp_result, greedy_time, dp_time = compare_algorithms(large_amount)
    print("\nДля великої суми:", large_amount)
    print("Час виконання жадібного алгоритму: {:.6f} секунд".format(greedy_time))
    print("Час виконання алгоритму динамічного програмування: {:.6f} секунд".format(dp_time))
