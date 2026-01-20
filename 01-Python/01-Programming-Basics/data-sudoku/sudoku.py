# pylint: disable=missing-docstring
import numpy as np


# pylint: disable=missing-docstring

def sudoku_validator(grid):
    """
    Returns True if the Sudoku grid is valid, False otherwise.
    A valid Sudoku must have numbers 1-9 exactly once per row, column, and 3x3 block.
    """
    S = set(range(1, 10))  # Ensemble {1,2,3,4,5,6,7,8,9}

    # Vérifier les lignes
    for r in range(9):
        if set(grid[r]) != S:
            return False

    # Vérifier les colonnes
    for c in range(9):
        col = [grid[r][c] for r in range(9)]
        if set(col) != S:
            return False

    # Vérifier les 9 sous-blocs 3x3
    for sr in (0, 3, 6):          # start row du bloc
        for sc in (0, 3, 6):      # start col du bloc
            block = [grid[r][c]
                     for r in range(sr, sr + 3)
                     for c in range(sc, sc + 3)]
            if set(block) != S:
                return False

    # Si tout est bon :
    return True
