**Problem:**
There are B Bears in incline village and T Trashcans. The bears have a property of mischievousness and the trashcans a property of smelliness. The product of a bear's misc to a trashcan's smell is the property dmg that the city incurs. For all bears, B, to trashcans T, determine the optimal pairing such that the propery damage is minimal.

**Input:**
You are given two unordered arrays that store integers for the Bears' misc and a another array fpr the Trashcans' smell. 


**Solution:** 
1. We are given two unordered arrays, one b_misc and the other t_smell.  We can sort them using a list method to sort in ascending order.
2. Create a variable called min_pdmg to store the minimal property damage from B bears to T trashcans. Create another idx variable starting at the length of B-1 bears.
3. Iterate from the B-1 index of the b_misc array and multiply that value with the starting value at array index 0 of the t_smell array. 
4. Add the product of the two values to the existing min_pdmg value and store that new value back to the min_pdmg variable.
5. Continue iterating until idx 0 index of the b_misc array.
6. Print the minimum property dmg that could occur.