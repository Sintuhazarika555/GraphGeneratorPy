import numpy as np
import pandas as pn
import matplotlib.pyplot as plt
import seaborn as sns

# functions to call the graph functions
def graph1():
    print("You have selected Line Plot.")
    print("you now need to enter the x and y values for the line plot.")
    x=list(map(int,input("Enter the x values separated by space: ").split()))
    y=list(map(int,input("Enter the y values separated by space: ").split()))
    plt.plot(x, y)
    plt.title("Line Plot")
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.grid(True)
    plt.show()

def graph2():
    print("You have selected Bar Chart.")
    print("You now need to enter the categories and their corresponding values.")
    n = int(input("Enter number of categories: "))
    categories = []
    values = []
    for i in range(n):
        category = input(f"Enter name for category #{i+1}: ")
        value = float(input(f"Enter value for '{category}': "))
        categories.append(category)
        values.append(value)
    plt.figure(figsize=(8, 5))
    plt.bar(categories, values, color='red')
    plt.title("User Input Bar Chart")
    plt.xlabel("Categories")
    plt.ylabel("Values")
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()

def graph3():
    print("You have selected Horizontal Bar Chart.")
    print("You now need to enter the categories and their corresponding values.")
    n = int(input("Enter number of categories: "))
    categories = []
    values = []
    for i in range(n):
        category = input(f"Enter name for category #{i+1}: ")
        value = float(input(f"Enter value for '{category}': "))
        categories.append(category)
        values.append(value)
    plt.figure(figsize=(8, 5))
    plt.barh(categories, values, color='red')
    plt.title("User Input Horizontal Bar Chart")
    plt.xlabel("Categories")
    plt.ylabel("Values")
    plt.grid(axis='x', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()

def graph4():
    print("You have selected Histogram.")
    print("You now need to enter numeric data for the histogram.")
    data_input = input("Enter numeric data separated by spaces: ")
    data = list(map(float, data_input.split()))
    bins = int(input("Enter number of bins for the histogram: "))
    plt.figure(figsize=(8, 5))
    plt.hist(data, bins=bins, color='red', edgecolor='black')
    plt.title("Histogram of User Input Data")
    plt.xlabel("Value")
    plt.ylabel("Frequency")
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()

def graph5():
    print("You have selected Scatter Plot.")
    print("You now need to enter the x and y values for the scatter plot.")
    x = list(map(float, input("Enter the x values separated by space: ").split()))
    y = list(map(float, input("Enter the y values separated by space: ").split()))
    plt.scatter(x, y)
    plt.title("Scatter Plot")
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.grid(True)
    plt.show()

def graph6():
    print("You have selected Pie Chart.")
    print("You now need to enter the labels and their corresponding sizes.")
    n = int(input("Enter number of categories: "))
    labels = []
    sizes = []
    for i in range(n):
        label = input(f"Enter name for category #{i+1}: ")
        size = float(input(f"Enter size for '{label}': "))
        labels.append(label)
        sizes.append(size)
    plt.figure(figsize=(8, 8))
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
    plt.title("Pie Chart of User Input Data")
    plt.axis('equal')  
    plt.show()

def graph7():
    print("You have selected Box Plot.")
    print("You now need to enter numeric data for the box plot.")
    data_input = input("Enter numeric data separated by spaces: ")
    data = list(map(float, data_input.split()))
    plt.figure(figsize=(8, 5))
    sns.boxplot(data=data, color='black')
    plt.title("Box Plot of User Input Data")
    plt.xlabel("Data")
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()

def graph8():
    print("You have selected Violin Plot.")
    print("You now need to enter numeric data for the violin plot.")
    data_input = input("Enter numeric data separated by spaces: ")
    data = list(map(float, data_input.split()))
    plt.figure(figsize=(8, 5))
    sns.violinplot(data=data, color='purple')
    plt.title("Violin Plot of User Input Data")
    plt.xlabel("Data")
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()

def graph9():
    print("You have selected Error Bar Plot.")
    print("You now need to enter the x values, y values, and error values.")
    x = list(map(float, input("Enter the x values separated by space: ").split()))
    y = list(map(float, input("Enter the y values separated by space: ").split()))
    error = list(map(float, input("Enter the error values separated by space: ").split()))
    plt.errorbar(x, y, yerr=error, fmt='-o', color='green', ecolor='red', capsize=5)
    plt.title("Error Bar Plot")
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.grid(True)
    plt.show()

def graph10():
    print("You have selected Contour Plot.")
    print("You now need to enter the range for x and y values.")
    print("Enter a function f(x, y), e.g., x**2 + y**2 or np.sin(np.sqrt(x**2 + y**2))")
    func_input = input("f(x, y) = ")
    x = np.linspace(-5, 5, 100)
    y = np.linspace(-5, 5, 100)
    X, Y = np.meshgrid(x, y)
    try:
        Z = eval(func_input, {"x": X, "y": Y, "np": np})
    except Exception as e:
        print("Error in function:", e)
        exit()
    plt.figure(figsize=(8, 6))
    contour = plt.contour(X, Y, Z, levels=20, cmap='viridis')
    plt.colorbar(contour)
    plt.title(f"Contour Plot of: {func_input}")
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def graph11():
    print("You have selected 3D Surface Plot.")
    print("Select : (1) f(x,y) , (2)f(x,y,z)")
    sel= int(input("Enter your choice: "))
    if sel == 1:
            print("Enter a function f(x, y), e.g., np.sin(np.sqrt(x**2 + y**2)) or x**2 - y**2")
            func_input = input("f(x, y) = ")
            x = np.linspace(-5, 5, 100)
            y = np.linspace(-5, 5, 100)
            X, Y = np.meshgrid(x, y)
            try:
                F = eval(func_input, {"x": X, "y": Y, "np": np})
            except Exception as e:
                print("Error in function:", e)
                exit()
            fig = plt.figure(figsize=(10, 7))
            ax = fig.add_subplot(111, projection='3d')
            surf = ax.plot_surface(X, Y, F, cmap='viridis', edgecolor='none')
            ax.set_title(f"3D Surface Plot of: {func_input}")
            ax.set_xlabel('X axis')
            ax.set_ylabel('Y axis')
            ax.set_zlabel('Z axis')
            fig.colorbar(surf, ax=ax, shrink=0.5, aspect=10)
            plt.tight_layout()
            plt.show()
    else:
        print("Enter a function f(x, y, z), e.g., np.sin(np.sqrt(x**2 + y**2 + z**2)) or x**2 - y**2 + z**2")
        func_input = input("f(x, y, z) = ")
        x = np.linspace(-5, 5, 100)
        y = np.linspace(-5, 5, 100)
        z = np.linspace(-5, 5, 100)
        X, Y, Z = np.meshgrid(x, y, z)
        try:
            F = eval(func_input, {"x": X, "y": Y, "z": Z, "np": np})
        except Exception as e:
            print("Error in function:", e)
            exit()
        fig = plt.figure(figsize=(10, 7))
        ax = fig.add_subplot(111, projection='3d')
        surf = ax.plot_surface(X[:, :, 0], Y[:, :, 0], F[:, :, 0], cmap='viridis', edgecolor='none')
        ax.set_title(f"3D Surface Plot of: {func_input}")
        ax.set_xlabel('X axis')
        ax.set_ylabel('Y axis')
        ax.set_zlabel('Z axis')
        fig.colorbar(surf, ax=ax, shrink=0.5, aspect=10)
        plt.tight_layout()
        plt.show()

def graph12():
    print("You have selected Polar Plot.")
    print("You now need to enter the theta values and corresponding radius values.")
    theta = np.linspace(0, 2 * np.pi, 100)
    r = np.abs(np.sin(theta))  
    plt.polar(theta, r, color='blue')
    plt.title("Polar Plot")
    plt.grid(True)
    plt.show()

def graph13():
    print("You have selected Heatmap.")
    print("You now need to enter the dimensions for the heatmap data.")
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))
    print(f"Enter the {rows} rows, with {cols} space-separated numbers each:")
    data = []
    for i in range(rows):
        while True:
            row_input = input(f"Row {i+1}: ").strip()
            row_values = row_input.split()
            if len(row_values) == cols:
                try:
                    row = list(map(float, row_values))
                    data.append(row)
                    break
                except ValueError:
                    print("Invalid numbers. Please enter floats or ints.")
            else:
                print(f"Please enter exactly {cols} values.")
    matrix = np.array(data)
    plt.figure(figsize=(8, 6))
    plt.imshow(matrix, cmap='viridis', interpolation='nearest')
    plt.colorbar(label='Value')
    plt.title("Heatmap of User Input Matrix")
    plt.xlabel("Columns")
    plt.ylabel("Rows")
    plt.tight_layout()
    plt.show()

def graph14():
    print("You have selected Stacked Bar Chart.")
    print("You now need to enter the categories and their corresponding values.")
    n = int(input("Enter number of categories: "))
    labels = []
    A = []
    B = []
    for i in range(n):
        label = input(f"Enter name for category #{i+1}: ")
        a_value = float(input(f"Enter value for '{label}' in group A: "))
        b_value = float(input(f"Enter value for '{label}' in group B: "))
        labels.append(label)
        A.append(a_value)
        B.append(b_value)
    plt.bar(labels, A, label='Group A', color='lightblue')
    plt.bar(labels, B, bottom=A, label='Group B', color='orange')
    plt.title("Stacked Bar Chart")
    plt.xlabel("Categories")
    plt.ylabel("Values")
    plt.legend()
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()
    


# MAIN PART


print("_"*100 +"\n"+" "*40+ "WELCOME TO GRAPH GENERATOR\n" + "_"*100)
print("This program generates various types of graphs using matplotlib and seaborn.\n")
while True:
    print("_"*100 +"\n")
    cont = input("Do you want to generate a graph? (yes/no): ").strip().lower()
    if cont == 'yes':

        print("Available Graphs:\n")
        print("1. Line Plot\n2. Bar Chart\n3. Horizontal Bar Chart\n4. Histogram\n5. Scatter Plot\n6. Pie Chart \n7. Box Plot\n8. Violin Plot\n9. Error Bar Plot\n10. Contour Plot\n11. 3D Surface Plot\n12. Polar Plot\n13. Heatmap\n14. Stacked Bar Chart")
        graph = int(input("\nEnter the number of the graph you want to generate (1-14): "))
        if graph == 1:
            graph1()
        elif graph == 2:
            graph2()
        elif graph == 3:
            graph3()
        elif graph == 4:
            graph4()
        elif graph == 5:
            graph5()
        elif graph == 6:
            graph6()
        elif graph == 7:
            graph7()
        elif graph == 8:
            graph8()
        elif graph == 9:
            graph9()
        elif graph == 10:
            graph10()
        elif graph == 11:
            graph11()
        elif graph == 12:
            graph12()
        elif graph == 13:
            graph13()
        elif graph == 14:
            graph14()
        else:
            print("Invalid input. Please enter a number between 1 and 14.")
    elif cont == 'no':
        print("_"*100 +"\n"+" "*40+ "Thank you for using the Graph Generator!\n" + "_"*100)
        break
    else:
        print("Invalid input. Please enter 'yes' or 'no'.")

