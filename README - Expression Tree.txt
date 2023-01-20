
PROJECT DESCRIPTION AND GUIDELINES PROVIDED ON ASSIGNMENT INSTRUCTIONS

For this assignment you will read from stdin the file expression.in and create an expression tree. The ex-
pression will be a valid infix expression with the all the necessary parentheses so that there is no ambiguity
in the order of the expression. You will evaluate the expression and print the result. You will also write the
prefix and postfix versions of the same expression without any parentheses.

In an expression tree the nodes are either operators or operands.

1. The operators will be in the set [’+’, ’-’, ’*’, ’/’, ’//’, ’%’, ’**’].
2. The operands will be either integers or floating point numbers.
3. All the operand nodes will be leaves of the expression tree.
4. All the operator nodes will have exactly two children.

The function create tree() will take as input parameter an infix expression with parentheses as a String
and create an Expression Tree from it. Assume that the expression string is valid and there are spaces
between the operators, operands, and the parentheses.

You will take the expression string and break it into tokens. There are four different kinds of tokens -
left parenthesis, right parenthesis, operator, and operand. When we read a left parenthesis we are starting a
new expression and when we read a right parenthesis we are ending an expression. Here is the algorithm
that you will use. Start with an empty node that is going to be your root node. Call it the current node. Then
start parsing the expression.

1. If the current token is a left parenthesis add a new node as the left child of the current node. Push
current node on the stack and make current node equal to the left child.

2. If the current token is an operator set the current node’s data value to the operator. Push current node
on the stack. Add a new node as the right child of the current node and make the current node equal
to the right child.

3. If the current token is an operand, set the current node’s data value to the operand and make the current
node equal to the parent by popping the stack.

4. If the current token is a right parenthesis make the current node equal to the parent node by popping
the stack if it is not empty.

Input:

Suppose the input file was the following:

( ( 8 + 3 ) ∗ ( 7 − 2 ) )

Output:

For the input expression, this is what your program will output:

( ( 8 + 3 ) ∗( 7 −2 ) ) = 55.0

Prefix Expression: ∗ + 8 3 − 7 2

Postfix Expression: 8 3 + 7 2 − ∗
