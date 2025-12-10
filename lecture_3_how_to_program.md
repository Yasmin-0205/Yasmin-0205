* Computer and Instructions 

- Python is a high-level interpreted, general-purpose programming language 
- It is good for rapid development where experimentation is key 
- It is bad however, if a program needs to run very quickly, or if it needs to be very memory efficient 
- Python is strictly a "program" script and can also be known as a scripting language 




As a result of abstraction, languages like python mean we do not need to worry too much about how the computer works 

Arithmetic operations are carried out in the CPU 

There is a small amount of memory in the CPU, in registers, with much more outside 

 

A python statement to create a named value is something like: 

  >>> spam = 42
  - The value is identified as an integer
  - The value 42 (in denary) is stored in the memory, an an addrss, using some memory suitable for an integer
  - The name spam is created, and associated with the address in a lookup table
  Now if the value spam is used
  - The name is located in the lookup table
  - The value is retrieved from memory, using the address in the lookup table
  - The value is used



* Data Restrictions 

The value of an integer is limited by the number of bits used to store one 

The size if floating-point numbers is likewise limited, as is the precision of the number 

The length of a string is limited by the amount of memory available 


 Performance Issues 

The length of a string is limited by the amount of memory available 

In the CPU: 

ALU - Arithmetic Logic Unit 

PCU - Program Control Unit 

Registers - Small amounts of memory in the CPU 

Cache - Small amounts of memory in the CPU, for frequently used data 

 

 

The program is stored in the memory, along with the data 

The PC keeps track of the address of the next instruction to be executed 

The instructions will be encoded as binary values and the operations will roughly correspond to the operations of the ALU 


* Errors in Programming 

Syntax errors:  When the program does not follow the rules of the language, and fails to compile or run 

Log (Semantic) errors:  When the program runs, but does not do what its intended to do 
