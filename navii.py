from functools import reduce
import pandas as pd
import pprint


class Classifier:

    def __init__(self, filename=None, class_attr=None):
        self.data = pd.read_csv(filename, sep=',', header=0)
        self.class_attr = class_attr
        self.priori = {}
        self.cp = {}
        self.hypothesis = None

    """
    probability(class) =
    count(class value)
    -------------------
    total number of samples
    """
    def calculate_priori(self):
        class_values = set(self.data[self.class_attr])
        class_data = list(self.data[self.class_attr])

        for value in class_values:
            self.priori[value] = class_data.count(value) / float(len(class_data))

        print("Prior Probabilities:")
        pprint.pprint(self.priori)

    """
    Conditional Probability:
    P(attribute=value | class)
    """
    def get_cp(self, attr, attr_value, class_value):
        data_attr = list(self.data[attr])
        class_data = list(self.data[self.class_attr])

        count = 0
        class_count = class_data.count(class_value)

        for i in range(len(data_attr)):
            if data_attr[i] == attr_value and class_data[i] == class_value:
                count += 1

        # Laplace smoothing
        return (count + 1) / float(class_count + len(set(data_attr)))

    """
    Calculate conditional probabilities for given hypothesis
    """
    def calculate_conditional_probabilities(self, hypothesis):
        self.cp = {}

        for class_value in self.priori:
            self.cp[class_value] = {}
            for attr in hypothesis:
                self.cp[class_value][attr] = self.get_cp(
                    attr, hypothesis[attr], class_value
                )

        print("\nConditional Probabilities:")
        pprint.pprint(self.cp)

    """
    Final classification
    """
    def classify(self):
        print("\nClassification Result:")
        for class_value in self.cp:
            probability = reduce(
                lambda x, y: x * y,
                self.cp[class_value].values()
            ) * self.priori[class_value]

            print(f"{class_value} ==> {probability:.6f}")


# ---------------- DRIVER CODE ----------------
if __name__ == "__main__":

    c = Classifier(
        filename=r"F:\AI LAB EXPTS\weather_data.csv",
        class_attr="Play"
    )

    c.calculate_priori()

    # Test hypothesis
    c.hypothesis = {
        "Outlook": "Rainy",
        "Temp": "Mild",
        "Humidity": "Normal",
        "Windy": "t"
    }

    c.calculate_conditional_probabilities(c.hypothesis)
    c.classify()
