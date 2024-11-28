from utils import *
import matplotlib.pyplot as plt

def plot(x, y, O_0, O_1):
    plt.scatter(x, y)
    plt.plot(x, predict(x, O_0, O_1), 'r', label='Prediction')
    plt.xlabel('Distance (km)')
    plt.ylabel('Price')
    plt.legend()
    plt.show()

def train_model(x, y, learning_rate=1e-2, epochs=5000):
    O_0, O_1 = 0, 0  # Initialize parameters
    m = len(x)  # Number of data points

    for epoch in range(epochs):
        predictions = predict(x, O_0, O_1)  # Predicted values
        error = [pred - yi for pred, yi in zip(predictions, y)]  # Calculate error

        # Update parameters using gradient descent
        O_0 -= learning_rate * sum(error) / m
        O_1 -= learning_rate * sum(e * xi for e, xi in zip(error, x)) / m

        if epoch % 500 == 0:  # Print progress every 500 epochs
            mse = sum((pred - yi) ** 2 for pred, yi in zip(predictions, y)) / m  # MSE
            print(f'Epoch {epoch}: MSE = {mse}')

    return O_0, O_1

def main():
    x, y = read_data()  # Read data from file
    normalized_x, mean_x, std_x = normalize_data(x)  # Normalize input data

    O_0, O_1 = train_model(normalized_x, y)  # Train model
    save_O(O_0, O_1, mean_x, std_x)  # Save model parameters and normalization values

    mse, mape = evaluate_model(normalized_x, y, O_0, O_1)  # Evaluate model
    print(f'MSE: {mse}')
    print(f'MAPE: {mape}%')

    plot(x, y, O_0, O_1)  # Visualize results

def evaluate_model(x, y, teta_0, teta_1):
    predictions = predict(x, teta_0, teta_1)
    mse = sum((pred - yi) ** 2 for pred, yi in zip(predictions, y)) / len(x)  # MSE
    mape = sum(abs(pred - yi) / yi for pred, yi in zip(predictions, y)) / len(x) * 100  # MAPE
    return mse, mape

if __name__ == "__main__":
    main()
