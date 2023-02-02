import pickle
from pathlib import Path
from summarizer import Summarizer


CURRENT_DIRECTORY = Path(__file__).parent
PACKAGE_DIRECTORY = f"{CURRENT_DIRECTORY}/packages"
MODEL_MAP = {
    "bert_summarizer": "Summarizer"
}


def create_pkl(model="bert_summarizer"):
    """Generate pickle file from corresponding mapped model

    Args:
        model (str, optional): _description_. Defaults to "bert_summarizer".
    """
    pkl_loc = f"{PACKAGE_DIRECTORY}/{model}.pkl"
    print(f"Trying to create {pkl_loc}")
    model_instance = eval(MODEL_MAP[model])()
    pickle.dump(model_instance, open(pkl_loc, 'wb'))
    print("Created")
