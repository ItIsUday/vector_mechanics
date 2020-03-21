from operations import *
from vector import Vector

if __name__ == '__main__':
    all_vectors = list(Vector(*map(float, input().split())) for _ in range(int(input())))
    resultant_vector = get_resultant(all_vectors)
    print(resultant_vector)
