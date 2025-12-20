# Content from Lec3.pdf

## Page 1

LECTURE #3
By: Aqib Rehman


---

## Page 2

OUTLINE
Intro to Forms
Create React App
Single Page Apps
Nesting Components
Props
Outputting Lists
Stateless Components


---

## Page 3

INTRO TO FORMS


---

## Page 4




### Images found on this page:

![page_4_img_1.jpeg](Lec3_images/page_4_img_1.jpeg)


---

## Page 5




### Images found on this page:

![page_5_img_1.jpeg](Lec3_images/page_5_img_1.jpeg)


---

## Page 6




### Images found on this page:

![page_6_img_1.jpeg](Lec3_images/page_6_img_1.jpeg)


---

## Page 7




### Images found on this page:

![page_7_img_1.jpeg](Lec3_images/page_7_img_1.jpeg)


---

## Page 8

When click on submit page will be refresh default event 
of form submit


### Images found on this page:

![page_8_img_1.jpeg](Lec3_images/page_8_img_1.jpeg)


---

## Page 9




### Images found on this page:

![page_9_img_1.jpeg](Lec3_images/page_9_img_1.jpeg)


---

## Page 10

Only trigger when button will be clicked not on Enter pressed


### Images found on this page:

![page_10_img_1.jpeg](Lec3_images/page_10_img_1.jpeg)


---

## Page 11




### Images found on this page:

![page_11_img_1.jpeg](Lec3_images/page_11_img_1.jpeg)


---

## Page 12

Now page will not be refreshed


### Images found on this page:

![page_12_img_1.jpeg](Lec3_images/page_12_img_1.jpeg)


---

## Page 13




### Images found on this page:

![page_13_img_1.jpeg](Lec3_images/page_13_img_1.jpeg)


---

## Page 14




### Images found on this page:

![page_14_img_1.jpeg](Lec3_images/page_14_img_1.jpeg)


---

## Page 15

CREATE REACT APP


---

## Page 16




### Images found on this page:

![page_16_img_1.jpeg](Lec3_images/page_16_img_1.jpeg)


---

## Page 17




### Images found on this page:

![page_17_img_1.jpeg](Lec3_images/page_17_img_1.jpeg)


---

## Page 18




### Images found on this page:

![page_18_img_1.jpeg](Lec3_images/page_18_img_1.jpeg)


---

## Page 19

CREATING APP WITH COMMAND


### Images found on this page:

![page_19_img_1.jpeg](Lec3_images/page_19_img_1.jpeg)


---

## Page 20




### Images found on this page:

![page_20_img_1.jpeg](Lec3_images/page_20_img_1.jpeg)


---

## Page 21




### Images found on this page:

![page_21_img_1.jpeg](Lec3_images/page_21_img_1.jpeg)


---

## Page 22




### Images found on this page:

![page_22_img_1.jpeg](Lec3_images/page_22_img_1.jpeg)


---

## Page 23




### Images found on this page:

![page_23_img_1.jpeg](Lec3_images/page_23_img_1.jpeg)


---

## Page 24

Basically this index.html is our one page app. All the components will be injected 
dynamically in this root div


### Images found on this page:

![page_24_img_1.jpeg](Lec3_images/page_24_img_1.jpeg)


---

## Page 25

First component React created for us with name App.
Its same which we saw earlier like a class based component with render method having a jsx 
template code, returning a div.


### Images found on this page:

![page_25_img_1.jpeg](Lec3_images/page_25_img_1.jpeg)


---

## Page 26

At the end we are exporting that component so that we can render it to the DOM.


### Images found on this page:

![page_26_img_1.jpeg](Lec3_images/page_26_img_1.jpeg)


---

## Page 27

Importing that component in index.js and rendering it to the root element of index.html
So basically here we are inject our component with ReactDOM.render method


### Images found on this page:

![page_27_img_1.jpeg](Lec3_images/page_27_img_1.jpeg)


---

## Page 28

How to run this app


---

## Page 29

Firstly with cd command will go into the directory
Then will start a local server


### Images found on this page:

![page_29_img_1.jpeg](Lec3_images/page_29_img_1.jpeg)


---

## Page 30

It will shows the ip address where that app is running


### Images found on this page:

![page_30_img_1.jpeg](Lec3_images/page_30_img_1.jpeg)


---

## Page 31

It will also be opened in browser automatically


### Images found on this page:

![page_31_img_1.jpeg](Lec3_images/page_31_img_1.jpeg)


---

## Page 32

All the text on the browser is coming from here: App component


### Images found on this page:

![page_32_img_1.jpeg](Lec3_images/page_32_img_1.jpeg)


---

## Page 33

Lets delete the css file. We do not going to show that default text on browser like 
its logo


### Images found on this page:

![page_33_img_1.jpeg](Lec3_images/page_33_img_1.jpeg)


---

## Page 34

Also delete the reference of the previous css file


### Images found on this page:

![page_34_img_1.jpeg](Lec3_images/page_34_img_1.jpeg)


---

## Page 35

Also delete the test file. No need at this time


### Images found on this page:

![page_35_img_1.jpeg](Lec3_images/page_35_img_1.jpeg)


---

## Page 36

So now basically we have 
App.js file which is our component.
Index.css which is a global css file of our project we can also add more css in this file.
Index.js file where we render the component to the DOM.
Logo.svg delete this logo too we have no further need.
registerServiceWorker.js file which manage cache for best user experience leave it…


### Images found on this page:

![page_36_img_1.png](Lec3_images/page_36_img_1.png)


---

## Page 37

Delete the import logo line we have no more this logo and also delete the image tag where we 
are putting logo.


### Images found on this page:

![page_37_img_1.jpeg](Lec3_images/page_37_img_1.jpeg)


---

## Page 38

Now in the browser we will have:
Simple Right?


### Images found on this page:

![page_38_img_1.jpeg](Lec3_images/page_38_img_1.jpeg)


---

## Page 39

Delete the rest too


### Images found on this page:

![page_39_img_1.jpeg](Lec3_images/page_39_img_1.jpeg)


---

## Page 40

Add simple template


### Images found on this page:

![page_40_img_1.jpeg](Lec3_images/page_40_img_1.jpeg)


---

## Page 41

When you hit Ctrl +S key it will automatically updated on the browser


### Images found on this page:

![page_41_img_1.jpeg](Lec3_images/page_41_img_1.jpeg)


---

## Page 42

SINGLE PAGE APPS


---

## Page 43




### Images found on this page:

![page_43_img_1.jpeg](Lec3_images/page_43_img_1.jpeg)


---

## Page 44




### Images found on this page:

![page_44_img_1.jpeg](Lec3_images/page_44_img_1.jpeg)


---

## Page 45




### Images found on this page:

![page_45_img_1.jpeg](Lec3_images/page_45_img_1.jpeg)


---

## Page 46




### Images found on this page:

![page_46_img_1.jpeg](Lec3_images/page_46_img_1.jpeg)


---

## Page 47




### Images found on this page:

![page_47_img_1.jpeg](Lec3_images/page_47_img_1.jpeg)


---

## Page 48

NESTING COMPONENTS


---

## Page 49

In React root component is App.js we can nesting more components in it


---

## Page 50




### Images found on this page:

![page_50_img_1.jpeg](Lec3_images/page_50_img_1.jpeg)


---

## Page 51

Creating another component with name Ninjas in src directory


### Images found on this page:

![page_51_img_1.jpeg](Lec3_images/page_51_img_1.jpeg)


---

## Page 52

Injecting component


### Images found on this page:

![page_52_img_1.jpeg](Lec3_images/page_52_img_1.jpeg)


---

## Page 53




### Images found on this page:

![page_53_img_1.png](Lec3_images/page_53_img_1.png)


---

## Page 54

PROPS


---

## Page 55

Passing data to component (Parent to child)


### Images found on this page:

![page_55_img_1.jpeg](Lec3_images/page_55_img_1.jpeg)


---

## Page 56




### Images found on this page:

![page_56_img_1.jpeg](Lec3_images/page_56_img_1.jpeg)


---

## Page 57




### Images found on this page:

![page_57_img_1.png](Lec3_images/page_57_img_1.png)


---

## Page 58




### Images found on this page:

![page_58_img_1.jpeg](Lec3_images/page_58_img_1.jpeg)


---

## Page 59




### Images found on this page:

![page_59_img_1.png](Lec3_images/page_59_img_1.png)


---

## Page 60




### Images found on this page:

![page_60_img_1.jpeg](Lec3_images/page_60_img_1.jpeg)


---

## Page 61

Still same output


### Images found on this page:

![page_61_img_1.png](Lec3_images/page_61_img_1.png)


---

## Page 62

Use same component with diff values: dynamic behavior


### Images found on this page:

![page_62_img_1.jpeg](Lec3_images/page_62_img_1.jpeg)


---

## Page 63

What it looks on browser


### Images found on this page:

![page_63_img_1.jpeg](Lec3_images/page_63_img_1.jpeg)


---

## Page 64

OUTPUTTING LISTS


---

## Page 65




### Images found on this page:

![page_65_img_1.jpeg](Lec3_images/page_65_img_1.jpeg)


---

## Page 66




### Images found on this page:

![page_66_img_1.jpeg](Lec3_images/page_66_img_1.jpeg)


---

## Page 67




### Images found on this page:

![page_67_img_1.jpeg](Lec3_images/page_67_img_1.jpeg)


---

## Page 68




### Images found on this page:

![page_68_img_1.jpeg](Lec3_images/page_68_img_1.jpeg)


---

## Page 69




### Images found on this page:

![page_69_img_1.jpeg](Lec3_images/page_69_img_1.jpeg)


---

## Page 70




### Images found on this page:

![page_70_img_1.jpeg](Lec3_images/page_70_img_1.jpeg)


---

## Page 71




### Images found on this page:

![page_71_img_1.png](Lec3_images/page_71_img_1.png)


---

## Page 72




### Images found on this page:

![page_72_img_1.jpeg](Lec3_images/page_72_img_1.jpeg)


---

## Page 73




### Images found on this page:

![page_73_img_1.jpeg](Lec3_images/page_73_img_1.jpeg)


---

## Page 74




### Images found on this page:

![page_74_img_1.png](Lec3_images/page_74_img_1.png)


---

## Page 75

STATELESS COMPONENTS


---

## Page 76

Container components are not concerned with UI or look of app
Container Comp.=Statefull Comp.=Class based Comp.
UI Comp.=Stateless Comp.=Functional Comp.


### Images found on this page:

![page_76_img_1.jpeg](Lec3_images/page_76_img_1.jpeg)


---

## Page 77




### Images found on this page:

![page_77_img_1.jpeg](Lec3_images/page_77_img_1.jpeg)


---

## Page 78




### Images found on this page:

![page_78_img_1.jpeg](Lec3_images/page_78_img_1.jpeg)


---

## Page 79




### Images found on this page:

![page_79_img_1.jpeg](Lec3_images/page_79_img_1.jpeg)


---

## Page 80




### Images found on this page:

![page_80_img_1.jpeg](Lec3_images/page_80_img_1.jpeg)


---

## Page 81




### Images found on this page:

![page_81_img_1.jpeg](Lec3_images/page_81_img_1.jpeg)


---

## Page 82




### Images found on this page:

![page_82_img_1.jpeg](Lec3_images/page_82_img_1.jpeg)


---

## Page 83

Final One


### Images found on this page:

![page_83_img_1.jpeg](Lec3_images/page_83_img_1.jpeg)


---

## Page 84




### Images found on this page:

![page_84_img_1.png](Lec3_images/page_84_img_1.png)


---

## Page 85




### Images found on this page:

![page_85_img_1.jpeg](Lec3_images/page_85_img_1.jpeg)


---

## Page 86

If have many


### Images found on this page:

![page_86_img_1.png](Lec3_images/page_86_img_1.png)


---

## Page 87

Also write this


### Images found on this page:

![page_87_img_1.png](Lec3_images/page_87_img_1.png)


---
