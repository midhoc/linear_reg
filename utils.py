import csv
import json
import sys

def normalize_data(x):
    mean_x = sum(x) / len(x)  # Calculate mean of x values
    std_x = (sum((xi - mean_x) ** 2 for xi in x) / len(x)) ** 0.5  # Standard deviation
    normalized_x = [(xi - mean_x) / std_x for xi in x]  # Apply normalization
    return normalized_x, mean_x, std_x

def predict(x, teta_0, teta_1, mean_x=0, std_x=1):
    normalized_x = [(xi - mean_x) / std_x for xi in x]  # Normalize input
    return [teta_0 + teta_1 * xi for xi in normalized_x]  # Predict using the learned parameters

def save_O(teta_0, teta_1, mean_x, std_x):
    data = {'teta_0': teta_0, 'teta_1': teta_1, 'mean_x': mean_x, 'std_x': std_x}
    try:
        with open('files/theta_values.json', 'w') as outfile:
            json.dump(data, outfile)
    except:
        print('Can\'t save Theta')
        sys.exit()
    
def load_O():
    try:
        with open('files/theta_values.json') as file:
            data = json.load(file)
    except:
        print('Can\'t load Theta')
        sys.exit()
    return data['teta_0'], data['teta_1'], data['mean_x'], data['std_x']

def read_data():
    x = []
    y = []
    try:
        file = open("files/data.csv", 'r')
    except:
        print('Couldn\'t open the file: files/data.csv')
        sys.exit()
    with file:
        csvreader = csv.reader(file)
        next(csvreader)  # Skip header row
        for row in csvreader:
            x.append(float(row[0]))  # Distance in km
            y.append(float(row[1]))  # Price
    return x, y
