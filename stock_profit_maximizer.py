price = [5,4,3,12,4,1]
min_price = price[0]
buy_day = sell_day = 1
temp_profit = max_profit = 0
loss=max(price)-min(price)
if buy_day<sell_day:
    for i in range(1, len(price)):
        if min_price < price[i]:
            temp_profit = price[i] - min_price
        else:
            if i != len(price) - 1:
                min_price = price[i]
                buy_day = i + 1
    
        if max_profit < temp_profit:
            max_profit = temp_profit
            sell_day = i + 1

if temp_profit <= 0:
    print("You should not buy this stock")
    print("Maximum loss will be:", loss)
else:
    print(f"Buy on day
