from time import perf_counter_ns


def nb_succ_sup(T):
    res = 0
    for i in range(len(T)-1):
        if T[i] > T[i+1]:
            res += 1
    
    return res

print(nb_succ_sup([1, 8, 2]))
print(nb_succ_sup([3, 5, 3, 6, 2]))

T = [3, 5, 3, 6, 2]
print("test debut de tableau")
t1 = perf_counter_ns()
T.insert(0, 1)
t2 = perf_counter_ns()
print("tableau : " + str(T) + "\ntemps : " +str(t2-t1))

T = [3, 5, 3, 6, 2]
print("test fin de tableau")
t1 = perf_counter_ns()
T.append(1)
t2 = perf_counter_ns()
print("tableau : " + str(T) + "\ntemps : " +str(t2-t1))

t_moy1 = 0
for i in range(100):
    T = [3, 5, 3, 6, 2]
    t1 = perf_counter_ns()
    T.insert(0, 1)
    t2 = perf_counter_ns()
    t_moy1 += t2 - t1
t_moy1 = t_moy1 / 100
print("temps insertion moy: " + str(t_moy1))

t_moy2 = 0
for i in range(100):
    T = [3, 5, 3, 6, 2]
    t1 = perf_counter_ns()
    T.insert(0, 1)
    t2 = perf_counter_ns()
    t_moy2 += t2 - t1
t_moy2 = t_moy2 / 100
print("temps append moy: " + str(t_moy2))
    