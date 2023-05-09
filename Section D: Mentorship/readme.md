1. Alright so first off, let's consider the specific mention of the showDialog method we're trying to use and weigh that up against our purpose for it. We would like to use our pop-up frame to provide the user with an oppertunity to provide us with some input data right? For this purpose, we're not currently using the correct method. While you're almost on the money, the correct method we are looking for would be the "showInputDialog(component, object)" method.

### **Analysis:**

Assess the main error to the code and share with the student what the overall solution would be that we would implement. I try to do this in order to immediately put the student's mind at ease, that we have a solution to implement and that no problem is insurmountable. We can in detail explain this solution, in this case the correct method, and make sure before we continue our student understands what we will be implementing, also spend time on why this is correct over the student's original implementation and point out where it went wrong originally.

2. Now before we use it, let's break down what we have so far, and why this method will be our choice of use. The name of the method as it aptly states is to tell us it's creating a input dialog for our user. When we look at the arguments for this method, it takes a component, and an object.

3. The component, is our frame or our box that we want to contain both our message displayed to the use and our input box from. So in this case, we need to create that frame before we can pass it along to our method. Let's make sure we have that first by creating a JFrame, we can simply call it frame to keep it our naming conventions simplistic and easy to understand.

4. Next, we have a look at our second argument, the object. This would be our message that we display to the user to explain to them what input we are waiting on. This could be anything related to our task such as "Please input XxX here:"

### **Analysis:**
We break down our implementation into smaller, byte-size bricks of info to not come across to overwhelming to someone new to programming. Explain each part from method to argument. Make sure our conversation is interactive and not one-sided, that our student understands the solution before implementing it. As in step 2, we explain the second argument and ensure our student understands what is required, what needs to be present for our solution to function and why this is the case. Offer options if applicable to make the student feel like they are ultimately in control of their code and that our guidance will merely teach instead of instructing them what to do. Step 2 to 4 will be the crucial part and probably where we will spend most of our time to ensure our student understands what is happening and can converse over it to show a level of understanding required before proceeding.

5. Now that we have both our arguments set up and we have our correct method at hand let's implement that and see how it runs.
6. Lastly, we need to make sure that our program closes out once we have successfully ran it, so be sure to include an implementation of System.exit(status) once we're finished else our program might not close on the user. In the event of a successful operation our exit status code will always be 0 implying no error or issues found.

### **Analysis:** 

Help the student to implement this solution once they show an apt level of understanding and create an environment of success and progress as you go along. Provide some additional info to a successful program as to show our student that we take a genuine and avid interest in their ultimate success.

7. That's all there is to it! Brilliant work!

### **Analysis:**

At all times, be congratulatory when there is success to be had and be encouraging and patient when the student is having a tough time. Once the solution is reached, be the person they can feel is truly in their corner as they continue through the course. After all we all had to start somewhere!
