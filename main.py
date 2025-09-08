import pandas as pd
from matplotlib import pyplot as plt

def main():
    print("Hello from main function!")
    print("Creating a df...")
    df = pd.DataFrame({'idx': [1, 2, 3, 4, 5], 'y': [1, 1, 10, 20, 60]})
    print("Plotting the df")
    df.plot()
    plt.show()


if __name__ == "__main__":
    main()
