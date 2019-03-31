class Sample:
    """Class representing a single hepatitis data sample."""
    labels = ["age", "sex", "steroid", "antivirals", "fatigue",
              "malaise", "anorexia", "liver_big", "liver_firm", "spleen_palpable",
              "spiders", "ascites", "varices", "bilirubin", "alk_phosphate",
              "sgot", "alubim", "protime", "histology"]
    ranked_labels = ["bilirubin", "alubim", "spiders", "histology", "malaise",
                     "ascites",	"fatigue", "age", "varices", "protime"]

    def __init__(self, classification, attributes):
        self.classification = classification
        self.attributes = attributes
        return

    def convert_to_ranked(self):
        self.attributes = \
            [self.attributes[13], self.attributes[16], self.attributes[10], self.attributes[18], self.attributes[5],
             self.attributes[11], self.attributes[4], self.attributes[0], self.attributes[12], self.attributes[17]]
        return

    def question_mark_to_min_int(self):
        for i in range(len(self.attributes)):
            if self.attributes[i] == '?':
                self.attributes[i] = float('-inf')
        return
