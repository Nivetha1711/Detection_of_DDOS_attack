# DDOS_attack
A Distributed Denial of Service (DDoS) attack is a malicious attempt to disrupt the normal functioning of a network, service, or website by overwhelming it with a flood of internet traffic!
In the context of DDoS (Distributed Denial of Service) detection,entropy computing refers to the calculation and analysis of entropy values in network traffic to identify anomalous patterns and potential DDoS attacks!

Proposed method:
1. Program Overview:
The program simulates the generation of network packets and implements a DDoS detection algorithm based on entropy calculation. It generates both normal and DDoS packets, combines them, and splits them into training and testing sets. The algorithm calculates the entropy of each packet and determines if it is indicative of DDoS traffic based on a predefined threshold. Finally, it evaluates the accuracy of the algorithm on the training and testing datasets.
2. Entropy Calculation:
The program defines a function named `calculate_entropy` that takes a data sequence as input and calculates the entropy using the formula: entropy = -Σ(p * log2(p)), where p is the probability of each unique element in the data. It uses a frequency distribution to calculate the probabilities and then calculates the entropy accordingly.
3. DDoS Threshold:
The program sets a predefined threshold (`ddos_threshold`) for DDoS detection. If the entropy of a packet exceeds this threshold, it is classified as DDoS traffic; otherwise, it is considered normal traffic.
4. Packet Generation and Labeling:
The program generates packets using the `send_packet` function for normal traffic and `generate_ddos_packet` function for DDoS traffic. Each packet is assigned a label (0 for normal traffic, 1 for DDoS traffic) and stored in the `packet_data` list along with its corresponding label in the `labels` list.
5. Data Splitting:
The program splits the combined packet data and labels into training and testing sets. The first 800 packets are used for training, while the remaining 200 packets are used for testing. The `train_data`, `train_labels`, `test_data`, and `test_labels` lists store the respective split datasets.
6. DDoS Detection:
The program trains the DDoS detection algorithm using the training data. It calculates the entropy for each packet in the training set and compares it with the predefined DDoS threshold. If the entropy exceeds the threshold, the packet is classified as DDoS traffic (assigned a value of 1 in `train_ddos_detected`); otherwise, it is classified as normal traffic (assigned a value of 0).
7. Accuracy Evaluation:
The program tests the trained DDoS detection algorithm using the testing data. It calculates the entropy for each packet in the testing set and determines if it exceeds the DDoS threshold. The results are stored in the `test_ddos_detected` list. The program then compares the detected labels with the actual labels in the testing set to calculate the accuracy of the algorithm.
8. Results and Reporting:
The program prints the training and testing accuracies on the console using the calculated accuracy values. The training accuracy is the percentage of correctly classified packets in the training set, while the testing accuracy represents the percentage of correctly classified packets in the testing set.

