import joblib
from typing import List, Dict, Any
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s'
    )


def load_model(model_path: str = 'model.pkl'):
    """
    Load the trained machine learning model from the specified path.

    Parameters:
    - model_path (str): Path to the serialized model file.

    Returns:
    - model: The loaded machine learning model.
    """
    try:
        model = joblib.load(model_path)
        logging.info(f"Model loaded successfully from {model_path}")
        return model
    except FileNotFoundError:
        logging.error(f"Model file not found at path: {model_path}")
        raise FileNotFoundError(f"Model file not found at path: {model_path}")
    except Exception as e:
        logging.error(f"An error occurred while loading the model: {e}")
        raise RuntimeError(f"An error occurred while loading the model: {e}")


def validate_input(
        features: Dict[str, Any], expected_features: List[str]
        ) -> List[Any]:
    """
    Validate and extract feature values from the input dictionary.

    Parameters:
    - features (Dict[str, Any]):
    Dictionary containing feature names and their corresponding values.
    - expected_features (List[str]):
    List of feature names expected by the model.

    Returns:
    - List[Any]: List of feature values ordered as per expected_features.
    """
    if not isinstance(features, dict):
        logging.error("Input features should be a dictionary.")
        raise ValueError("Input features should be a dictionary.")

    missing_features = [feature 
                        for feature in expected_features 
                        if feature not in features]
    if missing_features:
        logging.error(f"Missing features: {missing_features}")
        raise ValueError(f"Missing features: {missing_features}")

    # Extract feature values in the correct order
    try:
        feature_values = [features[feature] for feature in expected_features]
        logging.info(f"Validated input features: {feature_values}")
    except Exception as e:
        logging.error(f"Error extracting feature values: {e}")
        raise ValueError(f"Error extracting feature values: {e}")

    return feature_values


def format_prediction(prediction: Any) -> Dict[str, Any]:
    """
    Format the prediction result into a dictionary.

    Parameters:
    - prediction (Any): The raw prediction output from the model.

    Returns:
    - Dict[str, Any]: Dictionary containing the prediction.
    """
    try:
        result = {'prediction': int(prediction)}
        logging.info(f"Formatted prediction: {result}")
        return result
    except Exception as e:
        logging.error(f"Error formatting prediction: {e}")
        raise ValueError(f"Error formatting prediction: {e}")


def handle_exception(e: Exception) -> Dict[str, Any]:
    """
    Format exception messages for API responses.

    Parameters:
    - e (Exception): The exception that was raised.

    Returns:
    - Dict[str, Any]: Dictionary containing the error message.
    """
    logging.error(f"Exception occurred: {e}")
    return {'error': str(e)}
