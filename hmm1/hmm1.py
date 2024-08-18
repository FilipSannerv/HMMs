def multiply_lists(list1, list2):
    res = []
    for num1, num2 in zip(list1, list2):
	       res.append(num1 * num2)
    return res

def get_column(matrix, i):
    return [row[i] for row in matrix]

def dot_product(list1, list2):
    dotproduct = 0
    for list1, list2 in zip(list1, list2):
        dotproduct += list1 * list2

    return dotproduct

def forward_algorithm(V, a, b, initial_distribution, T, J):
    alpha = [[0]*J for _ in range(T)]

    alpha[0] = multiply_lists(initial_distribution[0], get_column(b, V[0]))

    for t in range(1, T):
        for j in range(J):
            alpha[t][j] = dot_product(alpha[t - 1], get_column(a, j)) * b[j][V[t]]

    return alpha

def convert_to_matrix(input_list):
    matrix = []
    rows = int(input_list[0])
    columns = int(input_list[1])
    elements = input_list[2:]
    for i in range(rows):
        row_list = []
        for j in range(columns):
            row_list.append(elements[columns * i + j])
        matrix.append(row_list)
    return matrix

def main():
    # Parse input
    tr = []
    em = []
    i_prob = []
    em_seq = []
    for x in input().split():
        tr.append(float(x))
    for x in input().split():
        em.append(float(x))
    for x in input().split():
        i_prob.append(float(x))
    for x in input().split():
        em_seq.append(int(x))

    tr_matrix = convert_to_matrix(tr)
    em_matrix = convert_to_matrix(em)
    i_prob_matrix = convert_to_matrix(i_prob)
    
    em_sequence = em_seq[1:]
    T = em_seq[0]
    J = len(tr_matrix[0])

    alpha = forward_algorithm(em_sequence, tr_matrix, em_matrix, i_prob_matrix, T, J)
    print(round(sum(alpha[len(alpha)-1]), 6))

if __name__ == "__main__":
    main()
