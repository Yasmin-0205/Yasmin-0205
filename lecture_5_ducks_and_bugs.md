* Ducks and Bugs 

What is a bug? 

- A bug is a mistake in a program that causes it to behave unexpectedly or incorrectly 
- They can arise from a variety of sources, including misunderstandings of a problem domain, incorrect assumptions and simple human error 
- They can lead to a range of issues, from minor glitches to major system failure 



Errors in Programming: 
- Syntax errors - When the program does not follow the rules of the language, and fails to compile or run 
- Logic (semantic) errors - When the program runs, but does not do what you intended 

 

2 Ways bugs manifest themselves? 
- The program appears to run correctly, but produces incorrect results in some situations 
- The program fails (crashes) in some situations 
 

Paired Programming 
- Programming in pairs, where 2 Devs (developers), use one keyboard, mouse (etc.) and program together. 
- Usually one "programs out loud". 

This is a part of "Extreme Programming" , or XP. It is essentially a continuous code review. 
This is an expensive but very productive approach to tackling tricky code 


 

More than one way to achieve the fix! 
- A properly engineered, long term, effective fix 
- A quick and dirty hack that will solve the problem short-term 
- This choice can lead to Technical Debt 

 
 

Debugging 
- Dry running -execute the code "by hand" and examine the results 
- This is to assume that we know in what situations the code fails 
- It can be done "all in the head" or with the aid of a printout 
 

Debugger -This is a tool (usually within  an IDE) that will allow us to stop a program at a certain point, and then run it "a line at a time" 

This shows how the values in the variables change 


 

Pepper it With Prints- Add print statements in the program to examine the data at various points 

This is quick and easy, and can be very effective. 

The downside of this, is that we have to remember to remove the print statements afterwards. 



Build in Debugging- Add a constant value (DEBUG, say) that can be set as a Boolean 

If set to true, execute suitably positioned print statements 

Easy to code, but it can make the program much bigger than it needs to be 


Logging- Code the program so that it logs what it is doing to some file 

Examining the log file can often show the cause of the problem 

 

Walk Away 

Ask a friend (A toy duck) 