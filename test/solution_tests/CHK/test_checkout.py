from solutions.CHK import checkout_solution


class TestSuperstore():
    def test_without_discount(self):
        assert checkout_solution.checkout(["C", "C", "D"]) == 55
    
    def test_with_discount_whole_discounts(self):
        assert checkout_solution.checkout(["A", "A", "A", "B", "B"]) == 175

    def test_with_discount_fraction_discounts(self):
        assert checkout_solution.checkout(["A", "A", "A", "A", "B", "B", "C"]) == 245

    def test_with_invalid_char(self):
        assert checkout_solution.checkout(["A", "A", "a", "A", "B", "B", "C"]) == -1