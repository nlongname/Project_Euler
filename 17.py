ones = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
tens = ['', 'ten', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
teens = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']


def nlc(n):
    total = 0
    for i in range(n+1):
        th = h = t = o = a = 0
        th = len(ones[int(i/1000)])
        if th != 0:
            th += len('thousand')
            #print(n)
        h = len(ones[int((i%1000)/100)])
        if h != 0:
            h += len('hundred')
        if i%100 in range(11, 20):
            t = len(teens[i%10])
            o = 0
        else:
            t = len(tens[int((i%100)/10)])
            o = len(ones[i%10])
        if t+o != 0 and h > 0:
            a = 3 #'and'
        total += th+h+t+o+a
        #print(total)
    return(total)

print(nlc(1000))
