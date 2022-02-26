import myConvexHull as mch
from sklearn import datasets
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os


def printDir():
    print("Current Dataset:")
    directory = os.getcwd()
    directory += f"\\test"
    listdir = os.listdir(directory)
    for i in range(len(listdir)):
        print(f"{i+1}. {listdir[i]}")
    choice = int(input("What do you want to choose?: "))
    if choice < 0 or choice > len(listdir):
        print("\nPlease input the correct number\n")
        return printDir()
    return listdir[choice-1]


def sklearnDataset():
    print("Sklearn Dataset:")
    print("1. Iris")
    print("2. wine")
    print("3. breast cancer")
    choice = int(input("What do you want to choose?: "))
    data = None
    if choice == 1:
        data = datasets.load_iris()
    elif choice == 2:
        data = datasets.load_wine()
    elif choice == 3:
        data = datasets.load_breast_cancer()
    else:
        print("\nPlease input the correct number\n")
        return sklearnDataset()
    return data


def selectedDataset():
    data = printDir()
    data = f"test\\{data}"
    return data


def selectDataset():
    data = None
    check = False
    print("1. Sklearn Dataset")
    print("2. Select dataset manually")
    choice = int(input("What do you want to choose?: "))
    if choice == 1:
        data = sklearnDataset()
        check = True
    elif choice == 2:
        data = selectedDataset()
        check = False
    else:
        print("\nPlease input the correct number\n")
        return selectDataset()
    return data, check


def prompt():
    print("Hi, Welcome to Gare's convex hull visualizer!")
    print("Do you want to try the Sklearn dataset or Select dataset manually?")
    data, check = selectDataset()
    if data == None:
        print("Invalid Dataset, Program exiting")
        exit(0)
    else:
        return data, check


def processSklearn(data):
    colors = ['b', 'r', 'g', 'c', 'm', 'y', 'k']
    df = pd.DataFrame(data.data, columns=data.feature_names)
    df['Target'] = pd.DataFrame(data.target)
    plt.figure(figsize=(10, 6))
    print("Processing sklearn dataset")
    print("\n")
    print(df.head())
    print("\n")
    print("Select 2 columns that you want to plot on x and y axis")
    len_data = len(data.feature_names)
    len_target = len(data.target_names)
    for i in range(len_data):
        print(f"{i+1}. {data.feature_names[i]}")
    choice = input(
        "Input number of two columns with space separated (ex: 1 2): ")
    x_idx = int(choice.split()[0])-1
    y_idx = int(choice.split()[1])-1
    try:
        x, y = data.feature_names[x_idx], data.feature_names[y_idx]
    except:
        print("Invalid input, Program exiting")
        exit(0)
    plt.title(f'{x} vs {y}')
    plt.xlabel(x)
    plt.ylabel(y)
    try:
        for i in range(len_target):
            bucket = df[df['Target'] == i]
            bucket = bucket.iloc[:, [x_idx, y_idx]].values
            tempbucket = bucket.tolist()
            hull = mch.convexHull(tempbucket)
            plt.scatter(bucket[:, 0], bucket[:, 1], label=data.target_names[i])
            for simplex in hull:
                plt.plot(bucket[simplex, 0], bucket[simplex, 1], colors[i])
                plt.legend()
        plt.show()
    except:
        print("Invalid Dataset, Program exiting")
        exit(0)


def processLocal(data):
    colors = ['b', 'r', 'g', 'c', 'm', 'y', 'k']
    df = pd.read_csv(data)
    cols = df.columns
    length_cols = len(cols) - 1
    print("Processing local dataset")
    print("\n")
    print(df.head())
    print("\n")
    plt.figure(figsize=(10, 6))
    print("Select 2 columns that you want to plot on x and y axis")
    for i in range(length_cols):
        print(f"{i+1}. {cols[i]}")
    choice = input(
        "Input number of two columns with space separated (ex: 1 2): ")
    x_idx = int(choice.split()[0])-1
    y_idx = int(choice.split()[1])-1
    try:
        x, y = cols[x_idx], cols[y_idx]
    except:
        print("Invalid input, Program exiting")
        exit(0)
    plt.title(f'{x} vs {y}')
    plt.xlabel(x)
    plt.ylabel(y)
    unique = df.Target.unique()
    try:
        for i in range(len(unique)):
            bucket = df[df['Target'] == unique[i]]
            bucket = bucket.iloc[:, [x_idx, y_idx]].values
            tempbucket = bucket.tolist()
            hull = mch.convexHull(tempbucket)
            plt.scatter(bucket[:, 0], bucket[:, 1], label=unique[i])
            for simplex in hull:
                plt.plot(bucket[simplex, 0], bucket[simplex, 1], colors[i])
                plt.legend()
        plt.show()
    except:
        print("Invalid Dataset, Program exiting")
        exit(0)


def main():
    data, check = prompt()
    # create a DataFrame
    if check:
        processSklearn(data)
        return

    processLocal(data)
    return


if __name__ == "__main__":
    main()
