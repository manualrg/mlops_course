import pandas_datareader.data as pdr
import pandas as pd


def get_data(start_date: str = "2019-07-01", end_date: str = "2019-09-30", ticker: str = "BTC-USD", provider: str = "yahoo"):
    start = pd.Timestamp(start_date)
    end = pd.Timestamp(end_date)
    df = pdr.DataReader(ticker, provider, start, end)
    return df


def write_data(data: pd.DataFrame, path: str, *args, **kwargs):
    data.to_csv(path, *args, **kwargs)


def main():
    btc_df = get_data(
        start_date="2019-07-01",
        end_date="2019-09-30",
        ticker="BTC-USD",
        provider="yahoo"
    )

    print(btc_df.head())


if __name__ == "__main__":
    main()
