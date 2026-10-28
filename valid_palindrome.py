def isPalindrome(s: str) -> bool:
    # Brute force: read twice, forward and in reverse, compare values

    # Optimized: read from each end at the same time comparing alphanumeric characters
    lp = 0
    rp = len(s) - 1

    # Succeed on if the indices overlap, midpoint doesn't work due to other characters not counting
    while lp < rp:
        if s[lp].casefold() == s[rp].casefold():
            lp += 1
            rp -= 1
        elif not s[lp].isalnum():
            lp += 1
        elif not s[rp].isalnum():
            rp -= 1
        else:
            return False
    
    return True

print(isPalindrome("Was it a car or a cat I saw?"))