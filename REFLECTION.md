# Part B: Reflection

## 1. How many tests and lines of code did I write?

I wrote 9 test functions in Part A, but the final file has 8 because I
removed `test_multiplication_by_two` in A3. The new multiplication test
already checked that case. `kitchen.py` has 37 lines of code without blank
lines, or 54 lines with blank lines included. The final ratio is 8 tests
to 37 lines of code, which is about 1 test for every 4.63 lines. All 43
test cases pass: 35 from Part 0 and 8 from Part A.

## 2. When did the tests stay red the longest?

The tests stayed red the longest in A7, when I added quantities with different
units. It took about 13 seconds between the first red commit and the green
commit, including the time spent running commands and pushing to GitHub.
I had to store conversion rates, pass the converter into the reduce methods,
and convert both quantities before adding them. The result of `201 g` helped
me see the mistake: the code added `200 + 1` without converting the ounce
to `28 g` first.

## 3. When did I use the three ways to get to green?

In A1, I used Fake It by setting the answer to 600 so the first test passed.
In A2, I used Triangulate by adding a second test that expected 400, which
forced me to replace 600 with `amount * multiplier`. In A3, I used Obvious
Implementation by returning a new Quantity with the multiplied amount.
I think these choices worked well: Fake It helped me check that the first
test worked, Triangulate led to the correct formula, and the A3 change was
simple enough to write directly.

## 4. What is still on my test list?

I finished every required item through A7 and added a test to check the
direction of conversion. The remaining items are multiplying a Sum, which
belongs to optional A8, and using quantities in sets or as dictionary keys,
which needs hashing. If I extended the program, I would implement Sum
multiplication next because it is already on the original test list.
For now, I would remove hashing from the list of planned features because
it is only a possible future need, but keep the note as A4 requested.

## 5. Would I have included Quantity.reduce in a plan made before coding?

I might not have included `Quantity.reduce` if I had planned the whole
system on paper first. I might have put all the conversion code in Converter
instead. After adding Sum, I saw why both Quantity and Sum needed a reduce
method: Converter could call the same method on either object. Passing the
converter into these methods also kept each converter's rates separate.

## 6. How were writing tests after and before the code different?

In Part 0, the code was already given, so I wrote tests to check its rules
and practice using pytest. The shipping tests helped me find bugs at the
weight boundaries. In Part A, I wrote each new test before adding the code
to make it pass, so the failures showed me what to change next.
The multiplication test led me to return a new quantity, the equality test
made comparisons easier, and the unit and mixed-addition tests guided the
conversion design. Part 0 mainly helped me check existing code, while
Part A helped me decide how to build the code.
