# Imports
from src.config import INPUT_DATA_FILE, OUTPUT_DATA_FILE, OUTPUT_REPORT_FILE
from src.reader import read_csv
from src.validator import validate_required_columns
from src.validator import validate_required_columns, add_validation_columns
from src.reporter import save_processed_data
from src.metrics import calculate_kpis, save_kpis_report

# Functions
def main():
    
    # Usa a função pra ler o arquivo
    df = read_csv(INPUT_DATA_FILE)

    # Usa a função pra validar o arquivo
    validate_required_columns(df)

    # Usa a função pra adicionar colunas de verificação no arquivo
    df = add_validation_columns(df)

    # Usa a função pra salvar o arquivo
    save_processed_data(df, OUTPUT_DATA_FILE)

    # Usa a função pra calcular os KPIs
    kpis = calculate_kpis(df)
    print("\n=== KPIs ===")
    for key, value in kpis.items():
        print(f"{key}: {value}")

    # Usa a função pra salvar os KPIs em um arquivo de txt
    save_kpis_report(kpis, OUTPUT_REPORT_FILE)

    
    



    print (df.head())

if __name__ == "__main__":
    main()