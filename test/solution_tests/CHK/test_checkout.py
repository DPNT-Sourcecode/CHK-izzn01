from solutions.CHK import checkout_solution


class TestSuperstore():
    def test_without_discount(self):
        assert checkout_solution.checkout(["C", "C", "D"]) == 55
