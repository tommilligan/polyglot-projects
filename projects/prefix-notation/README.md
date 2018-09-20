# prefix-notation

## Problem

Given a line of prefix notation:

- produce a function that can be called
- find the maximum output value considering integer inputs

Input: two lines

- first line containing space separated prefix notation
  - `+ 1 2`
  - `+ 6 * - 4 + 2 3 8`
  - valid operands are `+ - * /`, where `/` denotes integer division (floored)
  - valid numbers are positive integers, i.e. matching the regex `\d+`
  - valid variable names match the regex `[_a-zA-Z]+`
- second line containing JSON serialised variable ranges
  - `{}`
  - `{"x": [0, 3]}`
  - keys of the object are variable names as defined above
  - value is an array of length 2 describing the integer range, e.g. `[0, 3]` describes the possible values `0, 1, 2`

Output: a single line containing the maximum value of the function

## Example

```
# Input
* + 2 x y
{"x":[0,2],"y":[2,4]}

# Output
9
```

## Approach

- split prefix notation into tokens
- classify tokens as numbers, operators, or variables
- form a function that can be called with variables
  - could evalueate initial expression every time
  - could form a closure to precompute expression
- for each combination of variables, brute force for maximum value
