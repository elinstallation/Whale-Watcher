import kagglehub

kagglehub.login()

path = kagglehub.dataset_download("asadullahcreative/us-stock-market-historical-ohlcv-dataset")

print("Path:", path)