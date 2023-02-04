# 𝐏𝐚𝐥𝐢𝐧𝐝𝐫𝐨𝐦𝐞-𝐧𝐮𝐦𝐛𝐞𝐫
𝐏𝐚𝐥𝐢𝐧𝐝𝐫𝐨𝐦𝐞 𝐧𝐮𝐦𝐛𝐞𝐫

𝐏𝐫𝐨𝐛𝐥𝐞𝐦 𝐃𝐞𝐬𝐜𝐫𝐢𝐩𝐭𝐢𝐨𝐧:

The program takes a number and checks whether it is a palindrome or not.


Program Explanation:

1} User must first enter the value of the integer and store it in a variable.

2} The value of the integer is then stored in another temporary variable.

3} The for loop is used and the last digit of the number is obtained by using the modulus operator.

4} The last digit is then stored at the one’s place, second last at the ten’s place and so on.

5} The last digit is then removed by truly dividing the number with 10.

6} This loop terminates when the value of the number is 0.

7} The reverse of the number is then compared with the integer value stored in the temporary variable.

8} If both are equal, the number is a palindrome.

9} If both aren’t equal, the number isn’t a palindrome.

10} The final result is then printed.

Example 1:

Enter a number:121

reverse= 121

it is a Palindrome number

Example 2:

Enter a number:984

reverse= 489

it is not a Palindrome number

Example 3:

Enter a number:737

reverse= 737

it is a Palindrome number

Example 4:

Enter a number:845

reverse= 548

it is not a Palindrome number
