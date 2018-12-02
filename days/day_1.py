class FrequencyTracker:
    def __init__(self):
        pass

    @staticmethod
    def read(file_name):
        with open(file_name, newline='') as f:
            return f.read()

    @staticmethod
    def calculate(values):
        return eval(values)

    @staticmethod
    def repeat(values):
        all_freq = set()
        x = 0
        while True:
            for line in values.split("\n"):
                num = int(line[1:])
                x += (num if line[0] == "+" else -num)
                if x in all_freq:
                    return x
                all_freq.add(x)
