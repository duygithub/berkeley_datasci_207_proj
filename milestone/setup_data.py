# Install dependencies as needed:
# pip install kagglehub[pandas-datasets]
import kagglehub
from kagglehub import KaggleDatasetAdapter

def init_data_set():
    # Set the path to the file you'd like to load
    file_path = "loan.csv"
    
    # Load the latest version
    df = kagglehub.load_dataset(
      KaggleDatasetAdapter.PANDAS,
      "adarshsng/lending-club-loan-data-csv",
      file_path,
      # Provide any additional arguments like 
      # sql_query or pandas_kwargs. See the 
      # documenation for more information:
      # https://github.com/Kaggle/kagglehub/blob/main/README.md#kaggledatasetadapterpandas
    )
    
    print("First 5 records:", df.head())
