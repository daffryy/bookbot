def wc(string):
    return len(string.split())

def charcount(string):
    count = {}
    for i in string:
        if (i.isalpha()):
            if not i.lower() in count:
                count[i.lower()] = 1
                continue
            count[i.lower()] += 1
    return count

def cmp(d):
    return d["num"]

def ordered(dictionary):
    chars = []
    for i in dictionary:
        tmp = {}
        tmp["char"] = i
        tmp["num"] = dictionary[i]
        chars.append(tmp)
    chars.sort(reverse=True, key=cmp)
    return chars
