import pandas as pd

URL = "https://data.ademe.fr/data-fair/api/v1/datasets/dpe-v2-tertiaire-2/lines?size=10000&format=csv&after=10000%2C965634&header=true"

data = pd.read_csv(URL)

assert len(data) > 0

print(data.shape)

OUTPUT_DATA = "./data/original/dpe-v2-tertiaire.csv"

data.to_csv(OUTPUT_DATA, index=False)
