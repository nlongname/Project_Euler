start = 1504170715041707
current = start
mod = 4503599627370517
coin = start
prev_count = 0
total = 0
count = 1
while coin > 0:
    current += start
    current %= mod
    count += 1
    if current < coin:
        if count > 506:
            change = coin-current
            step = count - prev_count
            while current >= 0:
                coin = current
                total += coin
                print((count, coin))
                current -= change
                count += step
            if current == 0:
                print(f"total is {total}")
                break
            else:
                prev_count = count - step
        else:
            prev_count = count
            coin = current
            total += coin
            print((count, coin))
