#Link: https://py.checkio.org/en/mission/most-wanted-letter/
#concise solution learned from others
def checkio(text: str):
    import string
    text = text.lower();
    return max(string.ascii_lowercase, key = text.count);
