# Imports
from src.config import INPUT_DATA_FILE
from src.reader import read_csv
from src.validator import validate_required_columns
from src.validator import validate_required_columns, add_validation_columns

# Functions
def main():
    
    # Usa a função pra ler o arquivo
    df = read_csv(INPUT_DATA_FILE)
    # Usa a função pra validar o arquivo
    validate_required_columns(df)
    # Usa a função pra adicionar colunas de verificação no arquivo
    df = add_validation_columns(df)
    
    



    print (df.head())

if __name__ == "__main__":
    main()