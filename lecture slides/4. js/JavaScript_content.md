# Content from JavaScript.pdf

## Page 1

Java Script 
Change HTML Content 
<!DOCTYPE html> 
<html> 
<body> 
<h2>What Can JavaScript Do?</h2> 
<p id="demo">JavaScript can change HTML content.</p> 
<button type="button" 
onclick='document.getElementById("demo").innerHTML = "Hello 
JavaScript!"'>Click Me!</button> 
</body> 
</html> 
<html> 
<body> 
<h2>My First JavaScript</h2> 
<button type="button" 
onclick="document.getElementById('demo').innerHTML = Date()"> 
Click me to display Date and Time.</button> 
<p id="demo"></p> 
</body> 
</html>


---

## Page 2

Change HTML Attributes 
<!DOCTYPE html> 
<html> 
<body> 
<h2>What Can JavaScript Do?</h2> 
<p>JavaScript can change HTML attribute values.</p> 
<p>In this case JavaScript changes the value of the src (source) attribute of 
an image.</p> 
<button 
onclick="document.getElementById('myImage').src='pic_bulbon.gif'">Turn 
on the light</button> 
<img id="myImage" src="pic_bulboff.gif" style="width:100px"> 
<button 
onclick="document.getElementById('myImage').src='pic_bulboff.gif'">Turn 
off the light</button> 
</body> 
</html> 
Change HTML CSS Style 
<!DOCTYPE html> 
<html> 
<body>


---

## Page 3

<h2>What Can JavaScript Do?</h2> 
<p id="demo">JavaScript can change the style of an HTML element.</p> 
<button type="button" 
onclick="document.getElementById('demo').style.fontSize='35px'">Click 
Me!</button> 
</body> 
</html> 
Hide and Show 
<!DOCTYPE html> 
<html> 
<body> 
<img id="myImg" src="pic_bulboff.gif" width="100" height="132"> 
<br> 
<button type="button" onclick="hideElem(  )">Hide image</button> 
<button type="button" onclick="showElem()">Show image</button> 
<script> 
function hideElem() { 
  document.getElementById("myImg").style.visibility = "hidden";  
} 
function showElem() { 
  document.getElementById("myImg").style.visibility = "visible";


---

## Page 4

} 
</script> 
</body> 
</html> 
Difference between visibility and display 
<!DOCTYPE html> 
<html> 
<body> 
<p id="myP1">This is some text.</p> 
<p id="myP2">This is some text.</p> 
<input type="button" onclick="demoDisplay()" value="Hide text with display 
property"> 
<input type="button" onclick="demoVisibility()" value="Hide text with 
visibility property"> 
<script> 
function demoDisplay() { 
  document.getElementById("myP1").style.display = "none"; 
} 
function demoVisibility() { 
  document.getElementById("myP2").style.visibility = "hidden"; 
}


---

## Page 5

</script> 
</body> 
</html> 
Show Element 
<!DOCTYPE html> 
<html> 
<body> 
<h2>What Can JavaScript Do?</h2> 
<p>JavaScript can show hidden HTML elements.</p> 
<p id="demo" style="displa:none">Hello JavaScript!</p> 
<button type="button" 
onclick="document.getElementById('demo').style.display='block'">Click 
Me!</button> 
</body> 
</html> 
External JS 
<script src="myScript.js"></script>


---
