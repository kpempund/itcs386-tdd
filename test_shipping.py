import pytest
from shipping import shipping_fee


# Rule 1 is broken at zero: every nonpositive weight must raise ValueError.
@pytest.mark.parametrize("weight_kg", [-1, -0.01, 0])
def test_nonpositive_weight_is_rejected(weight_kg):
    with pytest.raises(ValueError):
        shipping_fee(weight_kg)


# Rule 2 is broken at 1 kg: the upper boundary still costs 40 baht.
# Rule 4 is broken for fractional extra kilograms: round up, not down.
@pytest.mark.parametrize("weight_kg, expected", [
    (0.01, 40), (0.5, 40), (0.999, 40), (1, 40),   # Rule 2
    (1.001, 60), (3, 60), (4.999, 60), (5, 60),    # Rule 3
    (5.001, 70), (5.2, 70), (6, 70),               # Rule 4, first kg
    (6.001, 80), (6.5, 80), (7, 80), (10.2, 120), # Rule 4, later kg
])
def test_shipping_fee_by_weight(weight_kg, expected):
    assert shipping_fee(weight_kg) == expected
