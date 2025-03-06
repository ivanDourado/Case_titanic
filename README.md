# Titanic Case Study

## Project Overview

This project analyzes data from the Titanic disaster, focusing on passenger survival based on various factors. The analysis includes statistical computations, data visualizations, and predictive modeling using logistic regression.

## Objectives

- **Embarkation Analysis**: Percentage of passengers who boarded at each port, using grouping and graphical visualization.
- **Class Analysis**: Percentage and count of passengers per class, highlighting distribution by class.
- **Family on Board**: Analysis of siblings/spouses and parents/children on board.
- **Age Analysis**: Number of passengers by age group (decades) with average age distribution.
- **Survival Analysis**: Number and percentage of survivors, divided by class and gender, using data from `train.csv` and `test.csv`.
- **Predictive Model**: Logistic regression model estimating survival probability based on gender, class, and age.

## Dataset

The project utilizes two datasets:

- **Train.csv**: Contains known survival outcomes.
- **Test.csv**: Used for predictions.

## Project Structure

```bash
├── titanic_data_analysis.ipynb  # Jupyter Notebook with analysis
├── titanic_tratamento_tabelas.py  # Data processing script
├── titanic_graficos.py  # Visualization script
├── train.csv  # Training dataset
├── test.csv  # Testing dataset
├── historica.csv  # Processed historical data
├── prevista.csv  # Predicted data
└── README.md  # Project documentation
```

## Prerequisites

To run this project, you need:

- **Python 3.7+**
- **pandas**
- **matplotlib**
- **seaborn**

Install dependencies using:

```bash
pip install pandas matplotlib seaborn
```

## Running the Project

### 1. Data Preprocessing

```python
import pandas as pd
import copy

# Load data
prevista = pd.read_csv('prevista.csv')
historica = pd.read_csv('historica.csv')
prev = copy.deepcopy(prevista)

# Fill missing ages with the mean per gender
prev.loc[prev['Sex'] == 'male', 'Age'] = prev.loc[prev['Sex'] == 'male', 'Age'].fillna(prev[prev['Sex'] == 'male']['Age'].mean())
prev.loc[prev['Sex'] == 'female', 'Age'] = prev.loc[prev['Sex'] == 'female', 'Age'].fillna(prev[prev['Sex'] == 'female']['Age'].mean())
```

### 2. Logistic Regression Model for Survival Prediction

```python
# Create indicator columns for gender and class
prev['isfemale'] = (prev['Sex'] == 'female').astype(int)
prev['isfirst'] = (prev['Pclass'] == 1).astype(int)
prev['issecond'] = (prev['Pclass'] == 2).astype(int)

# Compute survival probability using logistic regression formula
prev['Survived'] = -1.33 + 2.55 * prev['isfemale'] + 1.27 * prev['issecond'] + 2.58 * prev['isfirst'] - 0.04 * prev['Age']
prev['Survived'] = prev['Survived'].apply(lambda x: 2 if x >= 1 else 3)  # 2 = Would Survive, 3 = Would Die
```

### 3. Data Visualization

```python
import matplotlib.pyplot as plt
import seaborn as sns

# Survival by class
sns.countplot(x='Pclass', hue='Survived', data=prev)
plt.title('Survival by Passenger Class')
plt.show()
```

### 4. Run Interactive Menu

You can execute the Titanic menu script:

```bash
python titanic_graficos.py
```

This will display various visualizations for embarkation, class distribution, family presence, age groups, and survival analysis.

## Expected Results

- **Survival probability predictions** for test dataset.
- **Visual insights** into class, age, gender, and family influences on survival.
- **Logistic regression model** estimating survival likelihood.

## Contribution

To contribute:

1. Fork the repository.
2. Clone the project.
3. Create a new branch (`git checkout -b feature-branch`).
4. Commit your changes (`git commit -m 'Add feature'`).
5. Push to your branch (`git push origin feature-branch`).
6. Submit a Pull Request.

## License

This project is open-source and intended for educational purposes.

---

This documentation follows best practices for GitHub README files, ensuring clarity for users and contributors. 🚢
