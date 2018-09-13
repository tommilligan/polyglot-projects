# Cooccurrence

## Problem

Input: `n` lines, each containing a variable number of space separated strings `m >= 0`
Output: a function of signature `get(a: string, b: string): integer` that returns the number of lines both `a` and `b` were found in

Where two of the same token are found in one line, their relationships do not need to be deduplicated.

## Example

```
# Input
Alice Bob
Claire Alice David Bob
Eve Eve Fran

# Output
get(Alice, Bob) -> 2
get(David, Bob) -> 0
get(Alice, Claire) -> 1
get(Eve, Fran) -> 2
get(Eve, Eve) -> 2
```

## Approaches

### Extensible query

Form a lookup of form `{token: [line_id, ...], ...}`. This allows querying of `n` tokens, rather than just 2.

For each line, split into tokens. For each token, get current line ids and append current line id.
Deduplicate all line ids in lookup.

On get, find intersection of line numbers of two keys in lookup.

> ? O(log n) lookup
> O(n) data storage

### Optimised pairs

Form a lookup of hashed token pairs, form `{token_pair: count, ...}. Allows `O(1)` lookup.

For each line, split into tokens. Combine pairwise with every other token in line. For each pair, increment lookup count value.

> O(1) lookup
> ? O(log n) data storage

