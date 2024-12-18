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
    
    def test_multi_price_model_with_single_application(self):
        assert checkout_solution.checkout(["A", "A", "A", "A", "A", "B", "B", "C"]) == 265
    
    def test_multi_price_model_with_multiple_application(self):
        assert checkout_solution.checkout(["A", "A", "A", "A", "A", "A", "A", "A", "B", "B", "C"]) == 395
    
    def test_multi_price_model_with_multiple_and_free_application(self):
        assert checkout_solution.checkout(["A", "A", "A", "A", "A", "A", "A", "A", "B", "B", "C", "E", "E"]) == 460

    def test_multi_price_model_with_free_self_item(self):
        assert checkout_solution.checkout(["A", "A", "A", "A", "A", "A", "A", "A", "B", "B", "C", "F", "F", "F"]) == 415
    
    def test_multi_price_model_with_free_self_item_unclaimed(self):
        assert checkout_solution.checkout(["A", "A", "A", "A", "A", "A", "A", "A", "B", "B", "C", "F", "F"]) == 415

    def test_long_list(self):
        l = [
            ("I", 35),
            ("H", 10),
            ("G", 20)
        ]
        for i in l:
            assert checkout_solution.checkout(i[0]) == i[1]

    def test_group_offer(self):
        assert checkout_solution.checkout(["A", "A", "A", "X", "Y", "Z"]) == 175

    def test_group_offer_higher_value(self):
        assert checkout_solution.checkout(["A", "A", "A", "X", "Y", "Z", "Z", "Y", "Z", "Z"]) == 237