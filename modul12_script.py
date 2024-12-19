import pandas as pd

file_path = "C:/Users/tito_/PythonChatting/pythonProject/Negara.csv"
data = pd.read_csv(file_path)

mean_values = data[['Luas', 'Populasi']].mean()
std_dev_values = data[['Luas', 'Populasi']].std()

mean_df = pd.DataFrame({
    'Kriteria': ['Luas', 'Populasi'],
    'Mean': mean_values.values
})

std_dev_df = pd.DataFrame({
    'Kriteria': ['Luas', 'Populasi'],
    'Standar Deviasi': std_dev_values.values
})

mean_output_path = "C:/Users/tito_/PythonChatting/pythonProject/NegaraMean.csv"
std_dev_output_path = "C:/Users/tito_/PythonChatting/pythonProject/NegaraStandarDeviasi.csv"
mean_df.to_csv(mean_output_path, index=False)
std_dev_df.to_csv(std_dev_output_path, index=False)

mean_output_path, std_dev_output_path
