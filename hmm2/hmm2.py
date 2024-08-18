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

def viterbi_algorithm(em_sequence, tr_matrix, em_matrix, i_prob_matrix):

    N = len(tr_matrix[0])
    T = len(em_sequence)

    # Create empty matrices for Delta and Delta_idx
    delta = [[0] * N for _ in range(T)]
    delta_idx = [[0] * N for _ in range(T)]

    # t = 0 (base case)
    for i in range(N):
        delta[0][i] = em_matrix[i][em_sequence[0]] * i_prob_matrix[0][i]

    # t > 0 (recursion)
    for t in range(1,T):
        for i in range(N):
            max_prob = 0
            max_idx = 0
            for j in range(N):
                prob = tr_matrix[j][i] * delta[t-1][j] * em_matrix[i][em_sequence[t]]
                if (prob > max_prob):
                    max_prob = prob
                    max_idx = j
            delta[t][i] = max_prob
            delta_idx[t][i] = max_idx

    # Backtracking to find most probable final state
    m_prob_seq = [0] * T
    max_final_prob = 0
    for i in range(N):
        if (delta[T-1][i] > max_final_prob):
            max_final_prob = delta[T-1][i]
            m_prob_seq[T-1] = i

    # Backtracking to find most probable sequence of states
    for t in reversed(range(T-1)):
        m_prob_seq[t] = delta_idx[t+1][m_prob_seq[t+1]]

    return m_prob_seq

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

    most_probable_seq = viterbi_algorithm(em_sequence, tr_matrix, em_matrix, i_prob_matrix)

    print(" ".join(map(str, most_probable_seq)))

if __name__ == "__main__":
    main()
