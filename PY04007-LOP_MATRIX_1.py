class Matrix:
    def __init__(self, n, m, mt):
        self.n = n
        self.m = m
        self.mt = mt

    def transpose(self):
        transposed = [[self.mt[i][j] for i in range(self.n)] for j in range(self.m)]
        return Matrix(self.m, self.n, transposed)

    def multiply(self, other):
        result = []
        for i in range(self.n):
            row = []
            for j in range(other.m):
                s = 0
                for k in range(self.m):
                    s += self.mt[i][k] * other.mt[k][j]
                row.append(s)
            result.append(row)
        return Matrix(self.n, other.m, result)

    def print_matrix(self):
        for row in self.mt:
            print(' '.join(str(x) for x in row))


for i in range(int(input())):
    n, m = map(int, input().split())
    matrix_data = [list(map(int, input().split())) for _ in range(n)]
    a = Matrix(n, m, matrix_data)
    a_T = a.transpose()
    result = a.multiply(a_T)
    result.print_matrix()
