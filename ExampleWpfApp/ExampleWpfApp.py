import wpf

from System.Windows import Application, Window


class MyWindow(Window):
    def __init__(self):
        wpf.LoadComponent(self, 'ExampleWpfApp.xaml')
        self.greetButton.Click += self.greet

    def greet(self, sender, event):
        name = self.nameTextBox.Text
        greeting = "Hello {name}".format(name=name)
        self.outputTextBlock.Text = greeting
    

if __name__ == '__main__':
    Application().Run(MyWindow())
