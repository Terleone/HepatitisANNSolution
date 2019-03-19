class Sample:
    """Class representing a single hepatitis data sample."""
    def __init__(self, classification, age, sex, steroid, antivirals, fatigue, malaise, anorexia,
                 liver_big, liver_firm, spleen_palpable, spiders, ascites, varices, bilirubin,
                 alk_phosphate, sgot, albumin, protime, histology):
        self.classification = classification
        self.age = age
        self.sex = sex
        self.steroid = steroid
        self.antivirals = antivirals
        self.fatigue = fatigue
        self.malaise = malaise
        self.anorexia = anorexia
        self.liver_big = liver_big
        self.liver_firm = liver_firm
        self.spleen_palpable = spleen_palpable
        self.spiders = spiders
        self.ascites = ascites
        self.varices = varices
        self.bilirubin = bilirubin
        self.alk_phosphate = alk_phosphate
        self.sgot = sgot
        self.albumin = albumin
        self.protime = protime
        self.histology = histology
        return

