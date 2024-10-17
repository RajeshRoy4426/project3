import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Sample dataset (assuming you already have a CSV file loaded as `df`)
df = pd.read_csv('synthetic_data.csv')  # Replace with your actual dataset

# Function to display different plot types
def plot_choice(choice):
    if choice == 1:
        # Histogram: Distribution of Salary
        # 2D Histogram (Age vs Salary)
        plt.figure(figsize=(10, 6))
        plt.hist2d(df['Salary'], df['Age'], bins=30, cmap='Blues')
        plt.colorbar(label='Counts')
        plt.xlabel('Age')
        plt.ylabel('Salary')
        plt.title('2D Histogram: Salary vs Age')
        plt.show()

    elif choice == 2:
        # Bar Plot: Average Salary by Department
        plt.figure(figsize=(10, 6))
        avg_salary = df.groupby('Department')['Salary'].mean().reset_index()
        sns.barplot(data=avg_salary, x='Department', y='Salary', palette='viridis')
        plt.title('Average Salary by Department')
        plt.xlabel('Department')
        plt.ylabel('Average Salary')
        plt.tight_layout()
        plt.show()

    elif choice == 3:
        # Scatter Plot: Salary vs Years of Experience
        plt.figure(figsize=(10, 6))
        sns.scatterplot(data=df, x='Years_of_Experience', y='Salary', hue='Department', palette='coolwarm')
        plt.title('Salary vs Years of Experience')
        plt.xlabel('Years of Experience')
        plt.ylabel('Salary')
        plt.tight_layout()
        plt.show()

    elif choice == 4:
        # Heatmap: Correlation Matrix
        correlation_matrix = df[['Age', 'Salary', 'Years_of_Experience']].corr()
        plt.figure(figsize=(8, 6))
        sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
        plt.title('Correlation Matrix of Numeric Variables')
        plt.tight_layout()
        plt.show()

    elif choice == 5:
        # Box Plot: Salary distribution by Education Level
        plt.figure(figsize=(10, 6))
        sns.boxplot(data=df, x='Education_Level', y='Salary', palette='Set3')
        plt.title('Salary Distribution by Education Level')
        plt.xlabel('Education Level')
        plt.ylabel('Salary')
        plt.tight_layout()
        plt.show()

    else:
        print("Invalid choice, please choose a number between 1 and 5.")

# Main interactive prompt
def main():
    print("Please choose a plot type to visualize:")
    print("1. Histogram: Distribution of Salary")
    print("2. Bar Plot: Average Salary by Department")
    print("3. Scatter Plot: Salary vs Years of Experience")
    print("4. Heatmap: Correlation Matrix")
    print("5. Box Plot: Salary Distribution by Education Level")

    choice = int(input("Enter the number of the plot you want to see: "))
    plot_choice(choice)

if __name__ == "__main__":
    main()
