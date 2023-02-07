import pickle
from pathlib import Path

# TODO Check for implementation of class

CURRENT_DIRECTORY = Path(__file__).parent
PACKAGE_DIRECTORY = f"{CURRENT_DIRECTORY}/packages"
# MODEL_MAP = {
#     "bert_summarizer": "Summarizer"
# }


# def create_pkl(model="bert_summarizer"):
#     """Generate pickle file from corresponding mapped model

#     Args:
#         model (str, optional): _description_. Defaults to "bert_summarizer".
#     """
#     from summarizer import Summarizer
#     model = MODEL_MAP[model]()
#     pickle.dump(model, open(f"{PACKAGE_DIRECTORY}/{model}.pkl"))


def get_model_obj(model="bert_summarizer"):
    """Return model instance from serialised package

    Args:
        model (str, optional): _description_. Defaults to "bert_summarizer".
    """
    model = pickle.load(open(f"{PACKAGE_DIRECTORY}/{model}.pkl", "rb"))
    return(model)




if __name__ == "__main__":
    MODEL = "bert_summarizer"
    TEXT = "Orangutans are not as powerfully built as the gorilla but are larger than the chimpanzee. The adult male is typically twice the size of the female and may attain a height of 1.3 metres (4.3 feet) and a weight of 130 kg (285 pounds) in the wild; females weigh 37 kg (82 pounds) or less. Older males develop wide cheek pads, a unique feature among primates. The typically dark tan or brownish skin is covered with relatively coarse and usually sparse red hair. Adult males and some older adult females may have partially or entirely bare backs, but the hair on a male can be so long as to look like a cape when he moves his arms."
    # create_pkl("bert_summarizer")
    def summarize(text, model="bert_summarizer"):
        summarizer = get_model_obj(model)
        return summarizer(text)
    summary = summarize(TEXT, MODEL)
    print(len(summary), summary)


