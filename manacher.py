#!/usr/bin/env python3
"""Manacher algorithm for longest palindromic substring."""
import sys

def manacher(s):
    t = "#" + "#".join(s) + "#"
    n = len(t)
    p = [0]*n
    c = r = 0
    for i in range(n):
        mirror = 2*c - i
        if i < r:
            p[i] = min(r - i, p[mirror])
        while i + p[i] + 1 < n and i - p[i] - 1 >= 0 and t[i+p[i]+1] == t[i-p[i]-1]:
            p[i] += 1
        if i + p[i] > r:
            c, r = i, i + p[i]
    max_len = max(p)
    center = p.index(max_len)
    start = (center - max_len) // 2
    return s[start:start+max_len]

def all_palindromes(s, min_len=2):
    t = "#" + "#".join(s) + "#"
    n = len(t)
    p = [0]*n
    c = r = 0
    for i in range(n):
        mirror = 2*c - i
        if i < r: p[i] = min(r - i, p[mirror])
        while i+p[i]+1 < n and i-p[i]-1 >= 0 and t[i+p[i]+1] == t[i-p[i]-1]:
            p[i] += 1
        if i + p[i] > r: c, r = i, i + p[i]
    result = set()
    for i in range(n):
        if p[i] >= min_len:
            start = (i - p[i]) // 2
            length = p[i]
            result.add(s[start:start+length])
    return result

def test():
    assert manacher("babad") in ("bab", "aba")
    assert manacher("cbbd") == "bb"
    assert manacher("racecar") == "racecar"
    assert manacher("a") == "a"
    pals = all_palindromes("abacaba")
    assert "abacaba" in pals
    assert "aba" in pals
    print("  manacher: ALL TESTS PASSED")

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "test": test()
    else:
        s = sys.argv[2] if len(sys.argv) > 2 else "abaxyzzyxf"
        print(f"Longest palindrome in '{s}': {manacher(s)}")
