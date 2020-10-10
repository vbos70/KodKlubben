====================
Club_2: Python Intro
====================

Compute big numbers
===================

Use the *Mu Editor* and *Python* to compute very big numbers.

1. Open the *Mu Editor* from the Raspberry menu.

2. Select *Python mode*.

3. Start Python.

4. Type: `1+1` and press the Enter key.

5. Python computes 1+1 and shows the answer (2).

6. Type a very big number, like `1000000000000000000` and press the Enter key.

7. Python "computes" the number and shows the answer (same number as you typed).

8. Add 2 very big numbers.

9. Add 3 very big numbers.

10. Add 10 very big numbers.

Compute Lists
=============

1. Type `[1,2,3]` in Python and press Enter.

2. [1,2,3] is a list of the elements 1, 2, and 3. Each element has its
   own *location* in the list.

3. Make a longer list: `[1,2,3,4,5,6,7]`

4. Make a list from two lists: `[1,2,3] + [4,5,6,7]`

5. Make 3 copies of a list: `[1,2,3] * 3`

6. Get the first element from a list: `[1,2,3][0]`

       Python answers with `1`, the first element in the list.  The
       `[0]` in `[1,2,3][0]` takes the element at location 0 from
       `[1,2,3]`.  Element locations start from 0. So, the first
       element's location is 0, the second element's location is 1,
       and the third element's location is 2.

7. Get the second element from the list `[1,2,3]`.

       Since locations in lists are numbered from 0, the second
       element is at location 1: `[1,2,3][1]`

8. Try to compute: `[1,2,3][3]`

       This is an error. The list has 3 elements. The `[..][3]` means:
       take the element at location 3 from the list `[..]`. Since
       locations start at 0, this is asking for the fourth
       element. There is no fourth element in `[1,2,3]`.

9. Add all elements in a list: `sum([1,2,3,4])`. Python shows the answer 6.

10. Add the elements in a very long list. For example,
    `sum([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])`

11. We can make really long lists as follows:

        `[1,2,3]` * 1000000

    This is a list of 1000000 copies of `[1,2,3]`: a list with 3000000
    elements! Can you add the elements of this list?

        `sum([1,2,3] * 1000000)`
    
