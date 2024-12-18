from solutions.CHK import checkout_solution


class TestSuperstore():
    def test_without_discount(self):
        assert checkout_solution.checkout(["C", "C", "D"]) == 55
    
    def test_with_discount_whole_numbers(self):
        assert checkout_solution.checkout(["A", "A", "A", "B", "B"]) == 175

