question :
           You are tasked with creating a Rectangle class with the following requirements:

An instance of the Rectangle class requires length:int and width:int to be initialized.
We can iterate over an instance of the Rectangle class 
When an instance of the Rectangle class is iterated over, we first get its length in the format: {'length': <VALUE_OF_LENGTH>} followed by the width {width: <VALUE_OF_WIDTH>}



Simple Explanation:

__iter__ makes the object iterable.

__next__ defines what value to give on each next iteration.

We manually keep an index (_index) to know what to return next.

After both length and width are returned, we raise StopIteration.
