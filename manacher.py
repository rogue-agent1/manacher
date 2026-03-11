#!/usr/bin/env python3
"""Manacher's algorithm — find all palindromic substrings in O(n)."""
import sys

def manacher(s):
    # Transform: abc -> ^#a#b#c#$
    t = "^#" + "#".join(s) + "#$"
    n = len(t); p = [0] * n; c = r = 0
    for i in range(1, n - 1):
        mirror = 2 * c - i
        if i < r: p[i] = min(r - i, p[mirror])
        while t[i + p[i] + 1] == t[i - p[i] - 1]: p[i] += 1
        if i + p[i] > r: c = i; r = i + p[i]
    return p

def longest_palindrome(s):
    p = manacher(s)
    max_len = max(p); center = p.index(max_len)
    start = (center - max_len) // 2
    return s[start:start + max_len]

def all_palindromes(s, min_len=2):
    p = manacher(s)
    result = set()
    for i in range(2, len(p) - 2):
        if p[i] > 0:
            center = (i - 2) / 2
            radius = p[i]
            for r in range(1, radius + 1):
                start = int(center - (r - 1) / 2)
                length = r if i % 2 == 0 else r
                sub = s[start:start + r] if i % 2 == 0 else s[int(center - r//2):int(center + r//2 + 1)]
            if p[i] >= min_len:
                start = (i - 2 - p[i]) // 2
                result.add(s[start:start + p[i]])
    return result

if __name__ == "__main__":
    s = sys.argv[1] if len(sys.argv) > 1 else "abacabacaba"
    lp = longest_palindrome(s)
    print(f"String: {s}")
    print(f"Longest palindrome: '{lp}' (length {len(lp)})")
