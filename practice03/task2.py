class C32:
    def __init__(self):
        self.state: C32.State = C32.A(self)

    def apply(self) -> int:
        return self.state.apply()

    def turn(self) -> int:
        return self.state.turn()

    def carve(self) -> int:
        return self.state.carve()

    class State:
        def __init__(self, parent):
            self.parent: C32 = parent

        def apply(self) -> int:
            raise RuntimeError

        def turn(self) -> int:
            raise RuntimeError

        def carve(self) -> int:
            raise RuntimeError

    class A(State):
        def apply(self):
            self.parent.state = C32.B(self.parent)
            return 0

    class B(State):
        def apply(self):
            self.parent.state = C32.C(self.parent)
            return 1

    class C(State):
        def apply(self):
            self.parent.state = C32.A(self.parent)
            return 3

        def turn(self):
            self.parent.state = C32.D(self.parent)
            return 2

    class D(State):
        def apply(self):
            self.parent.state = C32.E(self.parent)
            return 4

        def turn(self):
            self.parent.state = C32.A(self.parent)
            return 6

        def carve(self):
            self.parent.state = C32.F(self.parent)
            return 5

    class E(State):
        def turn(self):
            self.parent.state = C32.F(self.parent)
            return 7

    class F(State):
        def turn(self):
            self.parent.state = C32.F(self.parent)
            return 8
