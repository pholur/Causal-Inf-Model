from infer import *
import matplotlib.pyplot as plt
import numpy as np

responses = np.loadtxt(open("/Users/pavan/Desktop/Research/Masters_Project/SRC/assessments/assess1_LP.csv", "rb"), delimiter=",", skiprows=1)
# Models individual students performance improvements from time-to-time

inference = ["Vocabulary", "Semantics", 
"Inference", "Digital Logic", 
"Word Problems", "Basic Probability", 
"Probability in Engineering"]

def ret_dict_studs():
    # Creates a one-to-many map to record the progress per student in the class over time intervals.
    # There are 7 nodes with important values and the 8th is time
    student_rec = {}

    for i in range(0,number_of_entries):
        user = [int(i) for i in responses[i][0:]]
        user_ans = user[2:]
        user_sc = score_per_concept(user_ans)
        val = process_cause(user_sc)
        val_r = []

        for i in val: # some precision issues could lead to > 1 probs
            if i <= 1.000:
                val_r.append(i)
            else:
                val_r.append(1.000)

        val = val_r
        val.append(user[1])
        print val
        student_rec.setdefault(user[0], []).append(val)
    return student_rec

def plot_kid(l, key):
    plt.style.use('seaborn-darkgrid')
    palette = plt.get_cmap('Set1')

    ln = np.array(l)
    for i in range(0,7):
        plt.plot(ln[:,7],ln[:,i], label = inference[i])
    plt.title("User " + str(key) + "\'s Concept Learning Progress")
    plt.ylabel("Proficiency in Concept")
    plt.xlabel("Time through Diagnostic Test in system hrs")
    plt.legend(loc=2, ncol=2)
    plt.savefig("results/" + str(key) + ".pdf", bbox_inches='tight')
    plt.show()

if __name__ == '__main__':
    st_rec = ret_dict_studs()
    for key in st_rec:
        plot_kid(st_rec[key], key)
