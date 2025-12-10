* Modern Error Handling 

The Happy Path 

Code to the happy path: 
- It's well documented 
- It's the most important part 
- It may be the most interesting part 
- It delivers the most value 

 

Off the Path 
- A program should not crash when something unexpected happens 
- Shouldn’t confidently produce incorrect results 

 

The impact of errors; 
- Program will crash 
- Program will display unreliable results 

 

EXAMPLE CODE ERROR: 
class_size = int(input('How many students are there? ')) 


Domain error - The value entered could represent a class size 
Type error - The value entered is actually an integer 