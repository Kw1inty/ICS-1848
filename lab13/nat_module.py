class Nat:
    def __init__(self, value):
        self.Value = value
        self.Divs = []
        self.CalcDivs()

    def CalcDivs(self):
        self.Divs = []
        for i in range(1, self.Value + 1):
            if self.Value % i == 0:
                self.Divs.append(i)

    def DisplayValue(self):
        print(self.Value)

    def SetValue(self, value):
        self.Value = value
        self.CalcDivs()

    def DisplayDivs(self):
        print(*self.Divs)
