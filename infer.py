# this can be better done recursively. If the knowledge map
# is small enough, we can also just do it iteratively down
# the adjacency matrix with a prescribed direction.

# from is rows and to is cols
adj_matrix = [
[-1, -1, -1, -1, -1, -1, -1, +1, -1, -1, -1, -1, -1, -1],
[-1, -1, -1, -1, -1, -1, -1, -1, +0.5, -1, -1, -1, -1, -1],
[-1, -1, -1, -1, -1, -1, -1, -1, -1, +0.5, -1, -1, -1, -1],
[-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, +0.5, -1, -1, -1],
[-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, +0.5, -1, -1],
[-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, +1, -1],
[-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, +0.5],
[-1, -1, -1, -1, -1, -1, -1, -1, +0.5, -1, -1, -1, -1, -1],
[-1, -1, -1, -1, -1, -1, -1, -1, -1, +0.5, -1, -1, -1, -1],
[-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, +0.5, +0.4, -1, +0.2],
[-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, +0.1, -1, -1],
[-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
[-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 0.3],
[-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]]

import numpy as np
number_of_entries = 2
corr_ans = [1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 
0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 0, 1, 0, 0, 0, 1, 1, 0, 
1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 1, 0, 0]

# P voc, sem, inf, dig l, word l, prob, prob l
pred = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

#voc = (0:5)
#sem = [5:10]
#inf = [10:15]
#dig_l = [15:25]
#word_l = [25:35]
#prob = [40:50]
#prob_l = [35:40,50:60]

def process_cause(user_sc):
    A = map(list, zip(*adj_matrix))
    l = []
    for i in range(7,14): # limit the area of searching for cause due to property of graph
        sumt = 0.0
        tri = -1.0
        for j in range(0,len(A[i])):
            if A[i][j] != -1:
                if j >= 7:
                    sumt = sumt + A[i][j]*user_sc[j-7]
                else:
                    tri = A[i][j]
        l.append((user_sc[i-7] - sumt)/tri)
    #print l
    return l


def ret_val(user_ans, i,j):
    return sum(abs(np.subtract(user_ans[i:j],corr_ans[i:j])))

def score_per_concept(user_ans):
    l = []
    #for vocab
    value = ret_val(user_ans, 0, 5)
    length = 5.0
    l.append(1 - value/length)

    #for semantics
    value = ret_val(user_ans, 5,10)
    length = 5.0
    l.append(1 - value/length)

    #for inference
    value = ret_val(user_ans, 10,15)
    length = 5.0
    l.append(1 - value/length)

    #for digital logic
    value = ret_val(user_ans, 15,25)
    length = 10.0
    l.append(1 - value/length)

    #for word problems
    value = ret_val(user_ans, 25,35)
    length = 10.0
    l.append(1 - value / length)

    #for prob
    value = ret_val(user_ans, 40,50)
    length = 10.0
    l.append(1 - value / length)

    #for prob logic
    value = ret_val(user_ans, 35,40) + ret_val(user_ans, 50, 60)
    length = 15.0
    l.append(1 - value / length)

    return l

inference = ["Vocabulary", "Semantics", "Inference", "Digital Logic", 
"Word Problems", "Probability", "Probability Logic"]

if __name__ == '__main__':  
    responses = np.loadtxt(open("/Users/pavan/Desktop/assessments/assess1_LP.csv", "rb"), delimiter=",", skiprows=1)
    for i in range(0,number_of_entries):
        user = [int(i) for i in responses[i][0:]]
        user_ans = user[2:]
        user_net = 60 - ret_val(user_ans, 0, 60)
        user_sc = score_per_concept(user_ans)
        val = process_cause(user_sc)

        indic = np.argsort(val)
        print
        print "Net score of user " + str(user[0]) + " is: " + str(int(user_net)) + "/60" 
        if user_net < 55:
            print "The user has some ways to improve to be better at logic!"
            print 'The user would do well to practise on ' + '\033[1m' + inference[indic[0]] + ' and ' + inference[indic[1]] + '.' + '\033[0m'

        if user_net >= 52:
            print "The user is reasonably good at logic!"
        print