import numexpr as ne


class ViewModel:

    def __init__(self, entry, history):
        self.entry = entry
        self.history_lbl = history
        self.history = ""
        self.startValue = "0"
        self.zeroDivisionError = "wtf bro"
        self.operators = ['/', '*', '-', '+']

    def parseButton(self, lbl):
        if self.entry.get() ==  self.zeroDivisionError:
            self.entry.delete(0, "end")
            self.entry.insert("end", self.startValue)
        if lbl in self.operators:
            self.history += self.entry.get() + lbl
            self.history_lbl.config(text=self.history)
            self.entry.delete(0, "end")
            self.entry.insert("end", self.startValue)
        elif lbl == '.' and self.entry.get() == self.startValue:
            self.entry.insert("end", lbl)
        elif lbl == 'x²':
            value = self.entry.get()
            self.entry.delete(0, "end")
            self.entry.insert("end", self.getSqrtValue(value))
        elif lbl == '√':
            value = self.entry.get()
            self.entry.delete(0, "end")
            self.entry.insert("end", self.getRootValue(value))
        elif lbl == '1/x':
            value = self.entry.get()
            self.entry.delete(0, "end")
            self.entry.insert("end", self.getFractionValue(value))
        elif lbl == '%':
            value = self.entry.get()
            self.entry.delete(0, "end")
            self.entry.insert("end", self.getPercentValue(value))
        elif lbl == '=':
            self.history += self.entry.get()
            try:
                eval = ne.evaluate(self.history)
                self.history = ""
                self.history_lbl.config(text=self.history)
                self.entry.delete(0, "end")
                self.entry.insert("end", eval)
            except ZeroDivisionError:
                self.history = ""
                self.history_lbl.config(text=self.history)
                self.entry.delete(0, "end")
                self.entry.insert("end", self.zeroDivisionError)
        elif lbl == '±':
            value = self.entry.get()
            self.entry.delete(0, "end")
            self.entry.insert("end", self.getAbsValue(value))
        elif lbl == '⌫':
            value = self.entry.get()[:-1]
            self.entry.delete(0, "end")
            if len(value) == 0:
                self.entry.insert("end", self.startValue)
            else:
                self.entry.insert("end", value)
        elif lbl == "C":
            self.history = ""
            self.history_lbl.config(text=self.history)
            self.entry.delete(0, "end")
            self.entry.insert("end", self.startValue)
        elif lbl == "CE":
            self.entry.delete(0, "end")
            self.entry.insert("end", self.startValue)
        elif self.entry.get()[0] == self.startValue:
            self.entry.delete(0, "end")
            self.entry.insert("end", lbl)
        else:
            self.entry.insert("end", lbl)

    def getSqrtValue(self, value):
        number = float(value) ** 2
        if number.is_integer():
            return int(number)
        else:
            return number

    def getRootValue(self, value):
        number = float(value) ** 0.5
        if number.is_integer():
            return int(number)
        else:
            return number

    def getFractionValue(self, value):
        try:
            number = 1 / float(value)
        except:
            return self.startValue
        if number.is_integer():
            return int(number)
        else:
            return number

    def getPercentValue(self, value):
        if self.history[:-1] == "":
            return self.startValue
        eval = ne.evaluate(self.history[:-1])
        number = float(value) * eval / 100
        if number.is_integer():
            return int(number)
        else:
            return number

    def getAbsValue(self, value):
        number = -float(value)
        if number.is_integer():
            return int(number)
        else:
            return number
