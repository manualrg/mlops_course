import numpy as np
import pandas as pd
import pickle
from pathlib import Path
from src.models.custom_models import ANDModel


def main():
    path_model = Path(__file__).parent / "models"
    model_name = 'model.pkl'
    filename_model = path_model / model_name
    Xs = pd.DataFrame([[1, 1], [1, 0], [0, 1], [0, 0]])
    ys = pd.Series([1, 0, 0, 0])

    model = ANDModel().fit(Xs, ys)
    ps = model.predict(Xs)

    for idx, row in Xs.iterrows():
        print(f"input: ({row[0]}, {row[1]}) prediction: {ps[idx]}")

    print(f'Storing model in: {path_model.as_posix()} as {model_name}')
    pickle.dump(model, open(filename_model, "wb"))


if __name__ == "__main__":
    main()
