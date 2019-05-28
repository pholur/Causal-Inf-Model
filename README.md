# Causal Inferencing in Education (for Proofs and Logic in Engineering)

Provided a well-modelled graph for a causal network in the learning process, our intention is to use this expert system and diagnose the cause for a student's failure in learning proofs based on observed diagnostic data. This graph can be seen in graph.html. The learning uses Bayesian approaches in weighting nodes of the graph. It is important to note that we DO NOT generate the causal graph in this example. Therefore the graph is given below. The weights of yellow nodes are found by the diagnostic test and the weight of the green nodes are computed using Bayesian inferencing. The edges are subject to an expert system defined in infer.py.

![](https://github.com/pholur/Causal_Inf_Model/blob/master/knowledge_graph.png)

## Instructions to Run the Software

Please ensure that the path to the /assessments folder is correctly set in the files: infer.py, toCSV.py, and Corev2.html according to your specifications. Also make sure that the images are routed to the correct path in Corev2.html. To run:
* Execute: >> python server.py
* Go To: localhost:5000 to find all the files on the (now local) server - enter Corev2.html
* Answer the quiz as many times as users would like. The data is stored in the assessments/ dir.
* A visual representation of the graph can be found in graph.html.
* Then from the SRC folder, execute: >> python toCSV.py
* Lastly, execute: >> python infer.py

The last command is a scoring and infering tool that will solve for the deductions. NOTE: Please edit the number_of_entries variable in infer.py to match the number of users who took the test. A sample output is provided below.

![](https://github.com/pholur/Causal_Inf_Model/blob/master/sample_op.png)


## Future Work

* Version 3.0 and up to contain more support for expanding the feature map.
* Requires dynamic building of causal map based on the observational data alone to allow for confounding variables.
* Expanding the angle of questioning to subjective questions to ensure the unbiased assessment of potential.
* Get more precision in inference by expanding the graph but not at the cost of poorer diagnostic data.

For further clarification, contact: pholur@g.ucla.edu

