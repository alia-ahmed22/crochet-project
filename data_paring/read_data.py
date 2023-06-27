from pprint import *
import matplotlib.pyplot as plt
from scipy.signal import lfilter


def read_data(filepath):
    a = []
    g = []

    with open(filepath) as f:
        my_data = f.read().splitlines()

    for d in range(len(my_data)):
        if "ACCEL" in my_data[d] and d != len(my_data) - 1:
            x, y, z = my_data[d + 1].split("\t")
            a.append((x, y, z))
        elif "GYRO" in my_data[d] and d != len(my_data) - 1:
            x, y, z = my_data[d + 1].split("\t")
            z = z[3:]
            g.append((x, y, z))

    return a, g


def plot_xyz(title, num, x, y, z):
    plt.figure(num)
    plt.title(title)
    plt.plot(range(len(x)), x, c='r', linewidth=1)
    plt.plot(range(len(y)), y, c='g', linewidth=1)
    plt.plot(range(len(z)), z, c='b', linewidth=1)
    plt.show()


def plot_magnitude(title, num, x, y, z):
    plt.figure(num)
    plt.title(title)
    mag = []
    for i in range(len(x)):
        mag.append(np.sqrt(x[i]**2 + y[i]**2 + z[i]**2))
    plt.plot(range(len(mag)), mag, c='r', linewidth=2)
    plt.show()


def plot_axis(title, num, d):
    plt.figure(num)
    plt.title(title)
    plt.scatter(range(len(d)), d)
    plt.show()


def main():
    accel, gyro = read_data("../test_data/eightish_single.txt")
    print("Acceleration\n")
    pprint(accel)
    print("Gyroscope:\n")
    pprint(gyro)

    accel_x = [float(x[0]) for x in accel]
    accel_y = [float(x[1]) for x in accel]
    accel_z = [float(x[2]) for x in accel]
    gyro_x = [float(x[0]) for x in gyro]
    gyro_y = [float(x[1]) for x in gyro]
    gyro_z = [float(x[2]) for x in gyro]

    plot_xyz("Acceleration XYZ", 1, accel_x, accel_y, accel_z)
    #plot_xyz("Gyroscope", 1, gyro_x, gyro_y, gyro_z)

    #plot_magnitude("Acceleration Magnitude", 2, accel_x, accel_y, accel_z)
    #plot_axis("gyro x", 1, accel_x)
    #plot_axis("gyro y", 2, accel_y)
    #plot_axis("gyro_z", 3, accel_z)

main()
