class Sample:
    """Class representing a single hepatitis data sample."""
    labels = ["age", "sex", "steroid", "antivirals",
              "fatigue", "malaise", "anorexia", "liver_big", "liver_firm",
              "spleen_palpable", "spiders", "ascites", "varices", "bilirubin",
              "alk_phosphate", "sgot", "alubim", "protime", "histology"]

    def __init__(self, classification, attributes):
        self.classification = classification
        self.attributes = attributes
        return
