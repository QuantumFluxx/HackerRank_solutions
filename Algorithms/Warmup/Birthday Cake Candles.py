# Problem: https://www.hackerrank.com/challenges/birthday-cake-candles/problem
# Score: 10

def birthdayCakeCandles(ar):
    tallest_candle = ar[0]

    for x in ar[1:]:
        if x > tallest_candle:
            tallest_candle = x
    
    return sum([1 for x in ar if x == tallest_candle])