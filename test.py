

class A():
    param_1 = 1

    def returning_param(self):
        return self.param_1


class Mixin:
    param_2 = 2

    def list(self):
        return self.returning_param()


class View(A, Mixin):
    def get(self):
        print(self.list())


print(View().get())
