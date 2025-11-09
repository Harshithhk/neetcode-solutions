def characterReplacement(s: str, k: int) -> int:
    l = 0
    r = 1
    jmp_count = 0
    max_sub_len = 1
    jmp_point = 0
    while r < len(s):
        if s[r] == s[l]:
            r += 1
        else:
            if jmp_count == 0:
                jmp_point = r
            while jmp_count <= k:
                jmp_count += 1
                r += 1
                if jmp_count == k:
                    max_sub_len = max(max_sub_len, r - l + 1)
                    l = jmp_point
                    jmp_count = 0

    return max_sub_len


s = "ABAB"
characterReplacement(s, 2)
