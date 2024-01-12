#!/usr/bin/python3

def canUnlockAll(boxes):
    """
    Check if all boxes can be unlocked.

    Args:
    boxes (list of lists): Each inner list contains the keys in a box.

    Returns:
    bool: True if all boxes can be unlocked, False otherwise.
    """
    n = len(boxes)
    unlocked = [False] * n
    unlocked[0] = True
    stack = [0]

    while stack:
        current_box = stack.pop()
        for key in boxes[current_box]:
            if key < n and not unlocked[key]:
                unlocked[key] = True
                stack.append(key)

    return all(unlocked)
