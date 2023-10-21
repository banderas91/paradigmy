#Корреляция Пирсона
import math

def mean(X):
    return sum(X) / len(X)

def pearson_correlation(X, Y):
    n = len(X)
    mean_X = mean(X)
    mean_Y = mean(Y)
    
    diffprod = sum((x - mean_X) * (y - mean_Y) for x, y in zip(X, Y))
    xdiff2 = sum((x - mean_X) ** 2 for x in X)
    ydiff2 = sum((y - mean_Y) ** 2 for y in Y)

    return diffprod / math.sqrt(xdiff2 * ydiff2)

# Пример использования:
X = [1, 2, 3, 4, 5]
Y = [2, 3, 4, 5, 6]
print(pearson_correlation(X, Y))
