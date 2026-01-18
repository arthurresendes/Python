import pandas as pd

def main():
    sequencia = pd.date_range('20250101' , periods=31)
    print(sequencia)

if __name__ == "__main__":
    main()
