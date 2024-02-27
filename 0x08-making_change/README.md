# Making Change

This project provides a Python implementation for determining the fewest number of coins needed to meet a given total amount. It utilizes dynamic programming to efficiently calculate the minimum number of coins required from a pile of coins with different values.

## Functionality

The `makeChange` function in `0-making_change.py` module takes two parameters:
- `coins`: a list of coin values available.
- `total`: the total amount to be met using the available coins.

The function returns the fewest number of coins needed to meet the total amount. If the total amount is 0 or less, it returns 0. If the total cannot be met by any combination of the available coins, it returns -1.

## Example Usage

```python
from 0-making_change import makeChange

# Example 1
print(makeChange([1, 2, 25], 37))  # Output: 7

# Example 2
print(makeChange([1256, 54, 48, 16, 102], 1453))  # Output: -1
```

## Requirements

- Python version: 3.4.3
- All files are interpreted/compiled on Ubuntu 20.04 LTS.
- Files should end with a new line.
- The first line of all files should be `#!/usr/bin/python3`.
- All files must be executable.
- Editors allowed: vi, vim, emacs.
- PEP 8 style (version 1.7.x) should be followed.
- A `README.md` file is mandatory in the root of the project directory.

## Author
This project is authored by Akram Freij. 

## Contribution
Contributions are welcome. Please fork the repository, make changes, and submit a pull request.

Feel free to reach out with any suggestions, questions, or feedback. 

Happy coding!