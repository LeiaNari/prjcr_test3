import matplotlib.pyplot as plt
import numpy
import seaborn as sns

data = sns.load_dataset("iris")
print(data['petal_length'].mean())
print(data['petal_length'].median())
print(data['petal_length'].mode())

print("Dataset Information:")
print(data.info())
print("\nSummary Statistics:")
print(data.describe())
print("\nFirst Few Rows of the Dataset:")
print(data.head())

plt.hist(data['petal_length'], bins=20, color='skyblue', edgecolor='black')
plt.title('Distribution of Petal Length')
plt.xlabel('Petal Length')
plt.ylabel('Frequency')
plt.show()

plt.scatter(data['sepal_length'], data['sepal_width'], c=data['species'], cmap='viridis')
plt.title('Relationship between Sepal Length and Sepal Width')
plt.xlabel('Sepal Length')
plt.ylabel('Sepal Width')
plt.colorbar(label='Species')
plt.show()