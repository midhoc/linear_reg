from utils import *

def main():
    distance = -1
    while distance < 0:
        try:
             distance = float(input('Enter distance (km): '))
        except:
            distance = -1
    O_0, O_1, mean_x, std_x = load_O()  # Load trained model parameters and normalization values
    print('Estimated price is: {}'.format(predict([distance], O_0, O_1, mean_x, std_x)))

if __name__ == "__main__":
    main()
