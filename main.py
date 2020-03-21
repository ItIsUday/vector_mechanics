from vector import Vector

if __name__ == '__main__':
    all_vectors = list(Vector(*map(float, input().split())) for _ in range(int(input())))

    resultant_vector = sum(all_vectors)
    print(resultant_vector)
    print(resultant_vector.moment())
    print(resultant_vector.y_intercept())
    print(resultant_vector.x_intercept())
   