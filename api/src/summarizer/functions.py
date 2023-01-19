# import warnings
from summarizer import Summarizer


# warnings.filterwarnings("ignore")


async def get_summary(text):
    """Generate summary of a text

    Args:
        text (_type_): _description_

    Returns:
        _type_: _description_
    """
    summarizer = Summarizer()
    summary = summarizer(text)
    return summary

