s = 'zrlgqrinvqphypqhsi'

highest = 0
high_seq = []


for i in range(len(s) - 1):

    tmp_seq = []

    count = 1
    cur = 0
    next = 1

    lett = s[i + cur]
    lett_j = s[i + next]

    tmp_seq.append(s[i + cur])

    while ord(lett.lower()) <= ord(lett_j.lower()):

        if (i + next) < len(s):

            lett = s[i + cur]
            lett_j = s[i + next]

            if ord(lett.lower()) <= ord(lett_j.lower()):
                tmp_seq.append(s[i + next])
                count += 1

            cur += 1
            next += 1

        else:
            break

    if count > highest:
        highest = count
        high_seq = tmp_seq

print("Longest substring in alphabetical order is:", ''.join(high_seq))
