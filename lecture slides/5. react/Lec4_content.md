# Content from Lec4.pdf

## Page 1

LECTURE #4
By: Aqib Rehman


---

## Page 2

OUTLINE
Conditional Output
Forms Revisited
Functions as Props


---

## Page 3

CONDITIONAL OUTPUT


---

## Page 4




### Images found on this page:

![page_4_img_1.jpeg](Lec4_images/page_4_img_1.jpeg)


---

## Page 5




### Images found on this page:

![page_5_img_1.png](Lec4_images/page_5_img_1.png)


---

## Page 6




### Images found on this page:

![page_6_img_1.jpeg](Lec4_images/page_6_img_1.jpeg)


---

## Page 7




### Images found on this page:

![page_7_img_1.jpeg](Lec4_images/page_7_img_1.jpeg)


---

## Page 8




### Images found on this page:

![page_8_img_1.jpeg](Lec4_images/page_8_img_1.jpeg)


---

## Page 9




### Images found on this page:

![page_9_img_1.jpeg](Lec4_images/page_9_img_1.jpeg)


---

## Page 10




### Images found on this page:

![page_10_img_1.jpeg](Lec4_images/page_10_img_1.jpeg)


---

## Page 11




### Images found on this page:

![page_11_img_1.jpeg](Lec4_images/page_11_img_1.jpeg)


---

## Page 12

FORMS REVISITED


---

## Page 13

What we have already


### Images found on this page:

![page_13_img_1.jpeg](Lec4_images/page_13_img_1.jpeg)


---

## Page 14

WHAT WE GONNA DO
A form in which user can add new ninja of his/her choice.
Programmatically how?
What if by some method we update the ninjas list which we have defined in state of 
App comp.
This list passes as props to Ninjas comp, where it is iterate and show on the screen.
So when list will be updated the updated one will be sent to Ninjas component and 
that will be shown to the user.
So lets create a form with 3 fields for name, age, belt and add button.


---

## Page 15

Create a new component with name AddNinja


---

## Page 16




### Images found on this page:

![page_16_img_1.jpeg](Lec4_images/page_16_img_1.jpeg)


---

## Page 17

What will be type of this comp container or stateless?


---

## Page 18

As we want to store user input values locally in the state so container comp will be 
used


---

## Page 19

htmlFor in jsx template not for


### Images found on this page:

![page_19_img_1.jpeg](Lec4_images/page_19_img_1.jpeg)


---

## Page 20

Define state


### Images found on this page:

![page_20_img_1.jpeg](Lec4_images/page_20_img_1.jpeg)


---

## Page 21

Need 3 functions for each field. 
Right?
No


---

## Page 22




### Images found on this page:

![page_22_img_1.jpeg](Lec4_images/page_22_img_1.jpeg)


---

## Page 23

Calling handleChange func


### Images found on this page:

![page_23_img_1.jpeg](Lec4_images/page_23_img_1.jpeg)


---

## Page 24

hanldeSubmit func


### Images found on this page:

![page_24_img_1.jpeg](Lec4_images/page_24_img_1.jpeg)


---

## Page 25

Adding AddNinja comp in the root comp


### Images found on this page:

![page_25_img_1.jpeg](Lec4_images/page_25_img_1.jpeg)


---

## Page 26




### Images found on this page:

![page_26_img_1.jpeg](Lec4_images/page_26_img_1.jpeg)


---

## Page 27




### Images found on this page:

![page_27_img_1.png](Lec4_images/page_27_img_1.png)


---

## Page 28




### Images found on this page:

![page_28_img_1.png](Lec4_images/page_28_img_1.png)


---

## Page 29

Now what we need:
We need to add the stuff which we got in the last slide from the user to the nijas list 
which we mentioned in the start.
But how?


---

## Page 30

FUNCTIONS AS PROPS


---

## Page 31




### Images found on this page:

![page_31_img_1.jpeg](Lec4_images/page_31_img_1.jpeg)


---

## Page 32




### Images found on this page:

![page_32_img_1.jpeg](Lec4_images/page_32_img_1.jpeg)


---

## Page 33

Calling a func and passing a ninja obj through state


### Images found on this page:

![page_33_img_1.jpeg](Lec4_images/page_33_img_1.jpeg)


---

## Page 34




### Images found on this page:

![page_34_img_1.jpeg](Lec4_images/page_34_img_1.jpeg)


---

## Page 35




### Images found on this page:

![page_35_img_1.png](Lec4_images/page_35_img_1.png)


---

## Page 36

Adding id in ninja obj as we are not interested to take it from user


### Images found on this page:

![page_36_img_1.jpeg](Lec4_images/page_36_img_1.jpeg)


---

## Page 37

Not do this already updating array what of setState


### Images found on this page:

![page_37_img_1.jpeg](Lec4_images/page_37_img_1.jpeg)


---

## Page 38

Do not alter the state without setState


---

## Page 39

Generate a copy


### Images found on this page:

![page_39_img_1.jpeg](Lec4_images/page_39_img_1.jpeg)


---

## Page 40

<!DOCTYPE html>
<html>
<body>
<script>
const numbers = [1, 2, 3, 4, 5, 6];
const [one, two, ...rest] = numbers;
document.write("<p>" + one + "</p>");
document.write("<p>" + two + "</p>");
document.write("<p>" + rest + "</p>");
</script>
</body>
</html>


---

## Page 41




### Images found on this page:

![page_41_img_1.jpeg](Lec4_images/page_41_img_1.jpeg)


---

## Page 42




### Images found on this page:

![page_42_img_1.png](Lec4_images/page_42_img_1.png)


---

## Page 43

Add delete Ninja functionality in current code


---
