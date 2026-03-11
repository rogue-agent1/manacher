#!/usr/bin/env python3
"""Manacher's algorithm — find all palindromic substrings in O(n).

One file. Zero deps. Does one thing well.

Returns the longest palindromic substring and all palindrome radii.
"""
import sys

def manacher(s):
    """Returns array P where P[i] = radius of palindrome centered at i in transformed string."""
    t = "#" + "#".join(s) + "#"
    n = len(t)
    p = [0] * n
    c = r = 0
    for i in range(n):
        mirror = 2 * c - i
        if i < r:
            p[i] = min(r - i, p[mirror])
        while i + p[i] + 1 < n and i - p[i] - 1 >= 0 and t[i + p[i] + 1] == t[i - p[i] - 1]:
            p[i] += 1
        if i + p[i] > r:
            c, r = i, i + p[i]
    return p, t

def longest_palindrome(s):
    if not s: return ""
    p, t = manacher(s)
    max_len = max(p)
    center = p.index(max_len)
    start = (center - max_len) // 2
    return s[start:start + max_len]

def all_palindromes(s, min_len=2):
    """Return all distinct palindromic substrings of length >= min_len."""
    p, t = manacher(s)
    pals = set()
    for i in range(len(t)):
        for r in range(1, p[i] + 1):
            sub = t[i - r:i + r + 1].replace("#", "")
            if len(sub) >= min_len:
                pals.add(sub)
    return sorted(pals, key=lambda x: (-len(x), x))

def count_palindromic_substrings(s):
    p, _ = manacher(s)
    return sum((r + 1) // 2 for r in p)

def main():
    for s in ["babad", "cbbd", "abaaba", "racecar", "abacdfgdcaba"]:
        lp = longest_palindrome(s)
        count = count_palindromic_substrings(s)
        pals = all_palindromes(s)
        print(f"'{s}' → longest: '{lp}', count: {count}, all(≥2): {pals[:5]}{'...' if len(pals)>5 else ''}")

if __name__ == "__main__":
    main()
