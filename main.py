from stock import Stock

symbols = ["MSFT", "GOOGL", "AAPL", "META", "IMB", "EGY", "USA", "TESLA"]
threads = []

for symbol in symbols:
    t = Stock(symbol)
    t.start()
    threads.append(t)

for t in threads:
    t.join()
    print(t)
