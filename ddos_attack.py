import math
import random
from collections import Counter
from datetime import datetime

# Function to calculate entropy
def calculate_entropy(data):
    data_size = len(data)
    counter = Counter(data)
    entropy = 0.0

    for count in counter.values():
        probability = count / data_size
        entropy -= probability * math.log2(probability)

    return entropy

# Function to detect DDoS attacks and generate a report
def detect_ddos_attack(data, threshold):
    entropy = calculate_entropy(data)
    attack_detected = entropy > threshold

    report = f"======= DDoS Attack Detection Report =======\n"
    report += f"Timestamp: {datetime.now()}\n"
    report += f"Data Length: {len(data)}\n"
    report += f"Entropy: {entropy}\n"
    report += f"Threshold: {threshold}\n"
    report += f"Attack Detected: {'Yes' if attack_detected else 'No'}\n"

    if attack_detected:
        report += f"Warning: DDoS attack detected!\n"
        # Add additional actions to take when an attack is detected

    return report

# Predefined threshold for DDoS detection
ddos_threshold = 4.5

# List to store packet data and their labels
packet_data = []
labels = []

# Function to send packet and update packet_data list
def send_packet():
    packet = random.randint(0, 255)
    packet_data.append(packet)
    labels.append(0)  # Label 0 indicates normal traffic

# Function to generate DDoS packets and update packet_data list
def generate_ddos_packet():
    packet = random.randint(256, 511)
    packet_data.append(packet)
    labels.append(1)  # Label 1 indicates DDoS traffic

# Generate and send normal packets
for _ in range(1000):  # Adjust the number of packets as needed
    send_packet()

# Generate and send DDoS packets
for _ in range(200):  # Adjust the number of DDoS packets as needed
    generate_ddos_packet()

# Combine the normal and DDoS packets
combined_data = list(zip(packet_data, labels))
random.shuffle(combined_data)
packet_data, labels = zip(*combined_data)

# Split the data into training and testing sets
train_data = list(packet_data[:800])
train_labels = list(labels[:800])
test_data = list(packet_data[800:])
test_labels = list(labels[800:])

# Train the DDoS detection algorithm
train_entropies = [calculate_entropy([data]) for data in train_data]
train_ddos_detected = [1 if entropy > ddos_threshold else 0 for entropy in train_entropies]

# Test the DDoS detection algorithm
test_entropies = [calculate_entropy([data]) for data in test_data]
test_ddos_detected = [1 if entropy > ddos_threshold else 0 for entropy in test_entropies]

# Calculate accuracy
train_accuracy = sum(train_ddos_detected[i] == train_labels[i] for i in range(len(train_labels))) / len(train_labels)
test_accuracy = sum(test_ddos_detected[i] == test_labels[i] for i in range(len(test_labels))) / len(test_labels)

print("Training Accuracy:", train_accuracy)
print("Testing Accuracy:", test_accuracy)

# Generate report for test data
report = detect_ddos_attack(test_data, ddos_threshold)
print(report)
