class vscode():
    def compile(self):
        print('compiling by vscode ')
    def execute(self):
        print('excetuting by vscode ')
    def debug(self):
        print('debug by vscode  ')
class pycham():
    def compile(self):
        print('compiling by pycham ')
    def execute(self):
        print('excetuting by pycham  ')
    def debug(self):
        print('debug by pycham ')
class programmer():
    def work(self,ide):
        ide.compile()
        ide.execute()
        ide.debug()
obj1=programmer()
obj2=pycham()
obj1.work(obj2)
