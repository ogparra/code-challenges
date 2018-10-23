// Author: Oscar Parra
// Date: 10/18/18

var b_misc = [0, 1, 2, 3];
var t_smell = [0, 1, 2, 3, 4, 5, 6, 7, 8];

var min_pdmg = 0;
var idx = b_misc.length-1;
while( idx >= 0 ){
	b_val = b_misc[idx];
	t_val = t_smell[b_misc.length - (idx + 1)];
	min_pdmg = min_pdmg + (b_val * t_val);
	idx--;
}
console.log(min_pdmg);