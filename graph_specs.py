import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

def node_vocab():

    First_ChkPt = "Basic_Vocabulary"
    Base1 = "language"
    Base2 = "axioms"
    Base3 = "basic_inference"

    set_1_q = "Pre_Engineering_Examples"

    Second_ChkPt = "Logic_Proofs"

    venn = "Venn_Diagrams"
    iff = "IfThen_IFF"
    xor = "XNOR_XOR"
    ind = "Induction"
    conv = "Convergence"

    tt = "Truth_Tables"
    symb_op = "Symbols_and_Operators"
    te = "Tautology_and_Equivalences"
    roi = "Rules_of_Inference"
    ror = "Rules_of_Replacement"
    rod = "Rules_of_Deduction"
    roc = "Rules_of_Conditionals"

    pred = "Predicate"
    quant = "Quantifiers"
    sat = "SAT_UNSAT_Equivalences"
    fal = "Fallacy_Logic"
    indL = "Inductive_Logic"

    tgt = "Engineering_Examples"
    return [First_ChkPt, Base1, Base2, Base3, set_1_q, Second_ChkPt, 
    venn, iff, xor, ind, conv, tt, symb_op, te, roi, ror, rod, roc, 
    pred, quant, sat, fal, indL, tgt]

def rel(vocab, details = True):

    G = nx.DiGraph()
    G.add_nodes_from(vocab)

    # Adding the edge definitions
    G.add_edges_from([(vocab[0],vocab[1]), (vocab[1],vocab[2]), (vocab[2],vocab[3])])
    G.add_edges_from([(vocab[3],vocab[4])])
    G.add_edges_from([(vocab[3],vocab[5])])
    G.add_edges_from([(vocab[5],vocab[6]), (vocab[5],vocab[7]), (vocab[5],vocab[8])])

    G.add_edges_from([(vocab[6],vocab[23]), (vocab[7],vocab[23]), (vocab[8],vocab[23]), 
        (vocab[9],vocab[23]), (vocab[10],vocab[23])])

    G.add_edges_from([(vocab[5],vocab[11]), (vocab[11],vocab[12]), (vocab[12],vocab[13])])
    G.add_edges_from([(vocab[13],vocab[14]), (vocab[13],vocab[15]), (vocab[13],vocab[16]), 
        (vocab[13],vocab[17])])
    G.add_edges_from([(vocab[14],vocab[23]), (vocab[15],vocab[23]), (vocab[16],vocab[23]), 
        (vocab[17],vocab[23])])

    G.add_edges_from([(vocab[5],vocab[18]), (vocab[18],vocab[19]), (vocab[19],vocab[20]), 
        (vocab[20],vocab[23])])

    G.add_edges_from([(vocab[5],vocab[21]), (vocab[5],vocab[22]), (vocab[21],vocab[23]),
        (vocab[22],vocab[23])])

    if details == True:
        nx.draw(G,pos=nx.spring_layout(G), node_size = 50, with_labels = True, font_size = 8)
        print nx.info(G)
        plt.show()
    return G


if __name__ == '__main__':
    vocab = node_vocab()
    graph = rel(vocab)