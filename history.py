import logic
import numpy as np
import math

history = []
results = []

def addToHistory(board, result):
    history.append(board)
    results.append(result)

def getHistory(i):
    return history[i]

def getResult(i):
    return results[i]

    