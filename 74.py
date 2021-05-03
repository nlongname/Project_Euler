import math

def factorial_chains(limit=1000000, length=60):
    lengths = {}
    answers = []
    for n in range(limit):
        if n % 10000 == 0:
            print(n)
        if n not in lengths:
            terms = []
            next_term = n
            while next_term not in terms:
                terms.append(next_term)
                next_term = sum(lambda x: math.factorial(int(x)), str(next_term))))
            cycle = terms[terms.index(next_term):]
            for t in cycle:
                lengths[t] = len(cycle)
                if len(cycle) == length and t < limit:
                    answers.append(t)
            if n not in lengths:
                lengths[n] = len(terms)
                if len(terms) == length:
                    answers.append(n)
    return(len(answers), lengths)

(a, l) = factorial_chains()
print(a)
