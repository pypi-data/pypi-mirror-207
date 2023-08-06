from prettytable import PrettyTable


class Units(object):

    UNIT_DIGITAL = 15
    UNIT_STR = ["V", "C", "Pa", "kPa", "%", "l/h", "bar", "Hz",
        "s", "ms", "min", "kW", "kWh", "J", "kJ", "",
        "m/s", "'", "h", "MWh", "MJ", "GJ", "W", "MW",
        "kJ/h", "MJ/h", "GJ/h", "ml", "l", "m3", "ml/h", "m3/h",
        "Wh", "?", "K", "", "lx", "t/min", "kVar", "kVarh",
        "mbar", "msg/m", "m", "kJ/kg", "g/kg", "ppm", "A", "kVA",
        "kVAh", "ohm"]

    def __init__(self):
        self._units={}
        self._indexByName={}
        for unit in range(len(self.UNIT_STR)):
            name=self.UNIT_STR[unit]
            self._units[unit]=name
            if name:
                self._indexByName[name.lower()]=unit

    def getByName(self, unit):
        try:
            return self._indexByName[unit.lower()]
        except:
            pass

    def getByNumber(self, unit):
        try:
            return self._units[int(unit)]
        except:
            pass

    def get(self, unit):
        unit=self.getByName(unit)
        if unit is None:
            unit=self.getByNumber(unit)
        return unit

    def __len__(self):
        return len(self.UNIT_STR)

    def __getitem__(self, key):
        return self.get(key)

    def __iter__(self):
        return iter(self._units.values())

    def isDigital(self, unit):
        try:
            if int(unit)==self.UNIT_DIGITAL:
                return True
        except:
            pass
        return False

    def digital(self):
        return self.UNIT_DIGITAL

    def none(self):
        return 0xFF

    def table(self, key=None):
        t=PrettyTable()
        t.field_names = ['#', 'unit']
        t.align['#']='l'
        t.align['unit']='l'
        for unit in range(len(self)):
            name=self.UNIT_STR[unit]
            if not key or key.lower() in name.lower():
                t.add_row([unit, name])
        print(t)

    def dump(self):
        for unit in range(len(self)):
            name=self.UNIT_STR[unit]
            print(unit, name)


if __name__=='__main__':
    pass
