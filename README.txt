HOW TO USE?
> go to 'vocabulary.csv' file
	> adjust 'vocab' and 'definition' columns 
		> run program


HOW DOES IT WORK? (for debug)
> data frame 'vocabulary' with 2 columns:
	> vocabulary column ('vocab')
	> definition column ('definition')
> Shuffe() to create list of term; in random order
> Normal() to create list of term; in same order as in data frame

> convert list to iterator
> create 'vocab' variable to store current vocabular, which is displayed on the interface
	> 'vocab' is a list aswell to make it manipulateble in functions

> 'Next' button:
	> use Update() iterate through iterator and update 'vocab' list with new iterator value
> 'Check' button:
	> checks 'vocab' value with definition value in same row in data frame as 'vocab'
		> look at Check2()
		> Check() is only for writing True/False message
		
> Show()
	> changes label to 'string'

> counter:
	> 'coutner' is list with one value
	> Counter() increases that value when called; updates 'counter'
	> configures in label

> history:
	> using Text widget
	> 'Next'-Button inserts string with current 'vocab' and 'definition' to Text widget
