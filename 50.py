primes = []
with open('primes.txt', 'r') as filehandle:
    primes = [int(current_prime.rstrip()) for current_prime in filehandle.readlines()]

def consecutive_prime_sum(limit=1000000):
    limited_primes = list(filter(lambda x: x < limit, primes))
    max_count = 1
    max_start = 0
    for i in range(len(limited_primes)):
        psum = limited_primes[i]
        count = 1
        j = i+1
        while psum < limit and j < len(limited_primes):
            psum += limited_primes[j]
            count += 1
            j += 1
            if count > max_count and psum in limited_primes:
                max_count = count
                max_start = limited_primes[i]
                #print(limited_primes[i:i+max_count], psum)
    start_index = limited_primes.index(max_start)
    ans_list = limited_primes[start_index:start_index+max_count]
    #print(len(ans_list), ans_list, sum(ans_list))
    return(sum(ans_list))
print(consecutive_prime_sum())
