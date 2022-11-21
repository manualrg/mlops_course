import pickle
import numpy as np
from pydantic import BaseModel
# https://docs.python.org/3/reference/import.html 5.7
from src.models.custom_models import ANDModel
from pathlib import Path


# Represents a particular wine (or datapoint)


class Features(BaseModel):
    x1: int
    x2: int


def load_clf():
    path_model = Path(__file__).parent.parent / "models"
    model_name = 'model.pkl'
    filename_model = path_model / model_name
    print(f"Loading model from path: {path_model}")

    # Load classifier from pickle file
    with open(filename_model, "rb") as file:
        global clf
        # https://stackoverflow.com/questions/50465106/attributeerror-when-reading-a-pickle-file/50472787#50472787
        clf = pickle.load(file)
        assert isinstance(clf, ANDModel), "Please, clf must be a ANDModel"


def home():
    return "Congratulations! Your API is working as expected. Now head over to http://localhost:80/docs"


def predict(input: Features):
    data_point = np.array(
        [
            [input.x1, input.x2]
        ]
    )

    pred = clf.predict(data_point).tolist()
    pred = pred[0]
    print(pred)
    return {"Prediction": pred}


def main():
    import os
    cwd = os.getcwd()
    print(f'@@@@@@@@@@@@{cwd=}')
    import sys
    print(f'@@@@@@@@@@@@syspath={sys.path}')

    clf = load_clf()
    xs = Features(x1=0, x2=0)
    ps = predict(input=xs)
    print(ps)


if __name__ == "__main__":
    main()
