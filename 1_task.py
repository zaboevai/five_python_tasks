import logging


def log(func):
    def surogate(*args):
        log = logging.getLogger('LOG')
        sh = logging.StreamHandler()
        log.addHandler(sh)
        log.setLevel('DEBUG')
        arguments = ', '.join(f"'{str(n)}'" for n in args)
        log.info(f'Входными значениями A и B являются: {arguments}')
        return func(*args)
    return surogate


class Calculator:

    @log
    def Sum(a,b):
        return a + b

    @log
    def Multiply(a,b):
        return a * b

    @log
    def Divide(a,b):
        return a / b

    @log
    def Subtract(a,b):
        return a - b

print(Calculator.Multiply(1,2))
