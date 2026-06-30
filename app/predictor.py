import joblib
import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
MODEL_PATH = BASE_DIR / "model" / "pipeline.joblib"

pipeline = joblib.load(MODEL_PATH)


def predict(data):

    column_mapping = {
        "mean_radius": "mean radius",
        "mean_texture": "mean texture",
        "mean_perimeter": "mean perimeter",
        "mean_area": "mean area",
        "mean_smoothness": "mean smoothness",
        "mean_compactness": "mean compactness",
        "mean_concavity": "mean concavity",
        "mean_concave_points": "mean concave points",
        "mean_symmetry": "mean symmetry",
        "mean_fractal_dimension": "mean fractal dimension",
        "radius_error": "radius error",
        "texture_error": "texture error",
        "perimeter_error": "perimeter error",
        "area_error": "area error",
        "smoothness_error": "smoothness error",
        "compactness_error": "compactness error",
        "concavity_error": "concavity error",
        "concave_points_error": "concave points error",
        "symmetry_error": "symmetry error",
        "fractal_dimension_error": "fractal dimension error",
        "worst_radius": "worst radius",
        "worst_texture": "worst texture",
        "worst_perimeter": "worst perimeter",
        "worst_area": "worst area",
        "worst_smoothness": "worst smoothness",
        "worst_compactness": "worst compactness",
        "worst_concavity": "worst concavity",
        "worst_concave_points": "worst concave points",
        "worst_symmetry": "worst symmetry",
        "worst_fractal_dimension": "worst fractal dimension"
    }

    model_input = {
        column_mapping[key]: value
        for key, value in data.items()
    }

    df = pd.DataFrame([model_input])

    prediction = pipeline.predict(df)

    return int(prediction[0])