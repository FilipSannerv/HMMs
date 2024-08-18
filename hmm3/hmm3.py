import math
# -------------- Helper functions -----------------------

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

def initilize_matrix(A, B):
    matrix = []
    for i in range(A):
        row_list = []
        for j in range(B):
            row_list.append(float(0))
        matrix.append(row_list)
    return matrix

def initilize_matrix3(A, B, C):
    matrix = []
    for i in range(A):
        matrix.append([])
        for j in range(B):
            matrix[i].append([])
            for k in range(C):
                matrix[i][j].append(0)
    return matrix

def print_solution(matrix):
    solution = ""
    for row in matrix:
        for col in row:
            solution += str(round(col, 6)) + " "

    print(str(len(matrix)) + " " + str(len(matrix[0])) + " " + solution)

# -----------------------------------------------------

def relearn_estimates(em_sequence, tr_matrix, em_matrix, i_prob_matrix, T, N, M):
    global _tr_matrix, _em_matrix, _i_prob_matrix, global_gamma, global_gamma_di, global_tr_matrix , global_em_matrix

    #re-estimate i_prob
    for i in range(N):
        i_prob_matrix[0][i] = global_gamma[0][i]

    #re-estimate tr_matrix
    for i in range(N):
        for j in range(N):
            numerator = float(0)
            denominator = float(0)
            for t in range(T-1):
                numerator += global_gamma_di[t][i][j]
                denominator += global_gamma[t][i]
            global_tr_matrix[i][j] = numerator / denominator
            #print(global_tr_matrix[i][j])

    #re-estimate em_matrix
    for i in range(N):
        for j in range(M):
            numerator = float(0)
            denominator = float(0)
            for t in range(T-1):
                if(em_sequence[t] == j):
                    numerator += global_gamma[t][i]
                denominator += global_gamma[t][i]
            global_em_matrix[i][j] = numerator / denominator
            #print(global_em_matrix[i][j])

    for i in range(len(i_prob_matrix)):
        _i_prob_matrix[0][i] = global_gamma[0][i]

    _tr_matrix = global_tr_matrix
    _em_matrix = global_em_matrix


def calculate_gamma_and_digamma(em_sequence, tr_matrix, em_matrix, T, N):
    global _tr_matrix, _em_matrix, _em_sequence, global_beta, global_alpha, global_gamma, global_gamma_di, global_tr_matrix

    for t in range(T-1):
        denominator = float(0)
        for i in range(N):
            for j in range(N):
                denominator += global_alpha[t][i] * global_beta[t+1][j] * _tr_matrix[i][j] * _em_matrix[j][_em_sequence[t+1]]
                #print(denominator)

        for i in range(N):
            global_gamma[t][i] = float(0)
            for j in range(N):
                global_gamma_di[t][i][j] = (global_alpha[t][i] * _tr_matrix[i][j] * _em_matrix[j][_em_sequence[t+1]] * global_beta[t + 1][j]) / denominator
                #print(global_gamma_di[t][i][j])
                global_gamma[t][i] += global_gamma_di[t][i][j]
                #print(global_gamma[t][i])


def beta_pass(em_sequence, tr_matrix, em_matrix, i_prob_matrix, T, N):
    beta = initilize_matrix(T,N)

    for i in range(N):
        beta[T-1][i] = c[T-1]
        #print(beta[T-1][i])

    for t in reversed(range(T-1)):
        for i in range(0,N):
            beta[t][i] = float(0)
            for j in range(0,N):
                beta[t][i] += (tr_matrix[i][j] * em_matrix[j][em_sequence[t+1]] * beta[t+1][j])
                #print(beta[t][i])
            #Scale Beta[t][i]
            beta[t][i] *= c[t]

    #print(beta[0][1])
    return beta


def alpha_pass(em_sequence, tr_matrix, em_matrix, i_prob_matrix, T, N):

    alpha = initilize_matrix(T,N)
    c[0] = float(0)

    #Calculate alpha[0][i] (initilization)
    for i in range(N):
        alpha[0][i] = em_matrix[i][em_sequence[0]] * i_prob_matrix[0][i]
        #print(alpha[0][i])
        c[0] += alpha[0][i]

    #Scale alpha[0][i] (initilization)
    c[0] = float(1) / c[0]
    for i in range(N):
        alpha[0][i] *= c[0]

    #Calculate alpha[t][i]
    for t in range(1,T):
        c[t] = float(0)
        for i in range(N):
            alpha[t][i] = float(0)
            for j in range(N):
                alpha[t][i] += (alpha[t-1][j] * tr_matrix[j][i])
                #print(alpha[t][i])
            alpha[t][i] *= em_matrix[i][em_sequence[t]]
            c[t] += alpha[t][i]
        #Scale alpha[t][i]
        c[t] = float(1) / c[t]
        for i in range(N):
            alpha[t][i] *= c[t]

    #print(alpha[0][1])
    return alpha


# Initialization ------------------
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

_tr_matrix = convert_to_matrix(tr)
_em_matrix = convert_to_matrix(em)
_i_prob_matrix = convert_to_matrix(i_prob)
_em_sequence = em_seq[1:]

T = em_seq[0]
N = len(_tr_matrix[0])
M = len(_em_matrix[0])

iterations = 250
current_i = 0
log_prob_temp = float(-10000000)

global_beta = initilize_matrix(T,N)
global_alpha = initilize_matrix(T,N)
global_gamma = initilize_matrix(T, N)
global_gamma_di = initilize_matrix3(T, N, N)
global_tr_matrix = initilize_matrix(N,N)
global_em_matrix = initilize_matrix(N,M)
c = [0] * T
# -----------------------------

# Iterate ---------------------
while current_i < iterations:
    global_alpha = alpha_pass(_em_sequence, _tr_matrix, _em_matrix, _i_prob_matrix, T, N)
    #print(global_alpa[0][1])
    global_beta = beta_pass(_em_sequence, _tr_matrix, _em_matrix, _i_prob_matrix, T, N)
    #print(global_beta[0][1])
    calculate_gamma_and_digamma(_em_sequence, _tr_matrix, _em_matrix, T, N)
    relearn_estimates(_em_sequence, _tr_matrix, _em_matrix, _i_prob_matrix, T, N, M)

    log_prob = float(0)
    for i in range(T):
        log_prob += math.log(c[i], 10)
        #print(log_prob)
    log_prob = -log_prob

    current_i += 1
    #print(current_i)

    if (log_prob > log_prob_temp):
        log_prob_temp = log_prob
    else:
        #print("lolp")
        break
# -----------------------------

print_solution(_tr_matrix)
print_solution(_em_matrix)
