from kivy.app import App
from kivy.uix.label import Label


class MortgageCalculatorApp(App):
    def build(self):
        return Label(text="Hello, MortgageCalculator", halign="center")


MortgageCalculatorApp().run()