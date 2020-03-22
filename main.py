"""THIS PROGRAM CALCULATES RESULTANT AND MOMENT OF NON-CONCURRENT FORCES"""

import shutil

from vector import Vector

if __name__ == '__main__':
    columns = shutil.get_terminal_size().columns
    print("VECTOR MECHANICS\n\n".center(columns))

    num = int(input('Enter the number of vectors: '))
    print('Enter details of each vector in the particular order')
    print('Magnitude | Inclination from x-axis | Horizontal distance | Vertical distance\n')
    all_vectors = list(Vector(*map(float, input().split())) for _ in range(num))

    resultant_vector = sum(all_vectors)
    print('\nThe resultant,', resultant_vector)
    print('The moment is,', resultant_vector.moment())
    print('Y intercept is,', resultant_vector.y_intercept())
    print('X intercept is,', resultant_vector.x_intercept())
