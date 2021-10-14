import matplotlib.pyplot as plt
import numpy as np
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.



def print_hi(name, umur):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    print(f'Umur saya {umur}')

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm', '21')
    x = np.array([5, 6, 7])
    y = np.array([99, 86, 10])
    plt.scatter(x, y)
    plt.show()
