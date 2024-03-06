from scipy.special import rel_entr

p = [0.20,0.40,0.50]
q = [0.60,0.15,0.05]

KL_PQ = rel_entr(p, q)
print('KL(P||Q): %.3f' % sum(KL_PQ))

#Calculate (Q||P)
KL_QP = rel_entr(q, p)
print('KL(Q||P): %.3f' % sum(KL_QP))