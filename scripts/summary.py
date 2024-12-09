import pandas as pd

# Load your dataset
# Replace 'your_file.csv' with your dataset file path or create a DataFrame manually
data = pd.read_csv('../data') 

# Display summary statistics for numeric columns
statistics = data.describe().T

# Adding additional statistics
statistics['median'] = data.median()
statistics['std_dev'] = data.std()
statistics['variance'] = data.var()
statistics['skewness'] = data.skew()
statistics['kurtosis'] = data.kurt()

# Display the summary statistics
print(statistics)