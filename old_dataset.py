from math import sqrt

def floatTryParse(value):
    try:
        val = float(value)
        return val, True
    except ValueError:
        return None, False

class Dataset:

    def __init__(self, file_name):
        self.name = file_name.split(".")[0]
        self.features = self.parse_features(file_name)
        self.features_name = self.features.pop(0)
        self.select_features()
        self.model_features_count = len(self.model_features[0]["features"])
        self.standardize_model_features()
        print(self.model_features[0])
        # print(self.model_targets[0])
        quit()
        # print(self.model_features_count)
        # self.
        # print(self.features_name, sep="\n")
        # print(self.features[0], sep="\n")

    def __str__(self):
        return "[{}]: size: {}".format(self.name, len(self.features))
    
    def parse_features(self, file_name):
        fd = open(file_name, "r")
        lines = fd.read().split("\n")
        return [x.split(",")[1:] for x in lines if len(x) > 0]
    
    def standardize_model_features(self):
        for mf in self.model_features:
            for fi, f in enumerate(mf["features"]):
                fstat = self.features_stats[fi]
                mf["features"][fi] = (f - fstat["Mean"]) / fstat["Std"]

    def select_features(self):
        # hogwarts house 0 (target)
        # astronomy 6
        # herbology 7
        # defense against the drak art 8
        # ancient runes 11
        # (charms) 16
        target = 0
        selected_features = [6, 7, 8, 11]
        features_mean = [[0, 0] for i in range(len(self.features[0]))]
        # print(self.features[0])
        self.model_features = []
        for feature in self.features:
            new_mf = {"features": [], "target": ""}
            for i, f in enumerate(feature):
                if i in selected_features:
                    fval, success = floatTryParse(f)
                    if success == True:
                        features_mean[i][0] += fval
                        features_mean[i][1] += 1
                    new_mf["features"].append(fval)
                elif i == target:
                    new_mf["target"] = f
            self.model_features.append(new_mf)
            
            
        # self.model_features = [[f for i, f in enumerate(feature) if i in selected_features] ]

        # print(self.features_name[11])
        self.features_stats = [{"Mean": (f[0] / f[1]), "Std": 0, "Initial_count": f[1]} for f in features_mean if f != [0, 0]]
        v = [0] * len(self.features_stats)
        for mf in self.model_features:
            for i, f in enumerate(mf["features"]):
                if f == None:
                    mf["features"][i] = self.features_stats[i]["Mean"]
                else:
                    v[i] += (f - self.features_stats[i]["Mean"]) ** 2
        for i, s in enumerate(self.features_stats):
            s["Std"] = sqrt(v[i] / s["Initial_count"])
        # for mf in self.model_features:
        #     if None in mf["features"]:
        #         quit()
        print (self.features_stats)
        print(self.model_features[0])
        # return model_features