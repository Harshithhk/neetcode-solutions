def checkInclusion(s1, s2):
    if len(s1) > len(s2):
        return False

    count_s1 = {}
    for ch in s1:
        count_s1[ch] = count_s1.get(ch, 0) + 1

    l = 0

    count_s2 = {}
    for r in range(len(s2)):
        count_s2[s2[r]] = count_s2.get(s2[r], 0) + 1

        if (r - l + 1) > len(s1):
            count_s2[s2[l]] -= 1
            if count_s2[s2[l]] == 0:
                del count_s2[s2[l]]

            l += 1

        if (r - l + 1) == len(s1):
            if count_s2 == count_s1:
                return True

    return False


s1 = "ab"
# s2 = "eidbaooo"
s2 = "eidboaoo"

res = checkInclusion(s1=s1, s2=s2)
print(res)
