class Converter:

    def c_to_f(self, celsius_value):
        f = (celsius_value * 9 / 5) + 32
        print(f"{celsius_value}c is equal to {f} f")

    def f_to_C(self, fahrenheit_value):
        c = (fahrenheit_value - 32) * 5 / 9
        print(f"{fahrenheit_value}f is equal to {c} c")


a = Converter()
a.c_to_f(10)
a.f_to_C(20)
