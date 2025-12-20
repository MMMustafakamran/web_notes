# Content from JavaScript2.pdf

## Page 1

Java Script 
 
 
External JavaScript 
<script src="myScript.js"></script> 
Using innerHTML 
 
<!DOCTYPE html> 
<html> 
<head> 
<script> 
function myFunction() { 
  document.getElementById("demo").innerHTML = "Paragraph changed."; 
} 
</script> 
</head> 
<body> 
<h1>A Web Page</h1> 
<p id="demo">A Paragraph</p> 
<button type="button" onclick="myFunction()">Try it</button> 
</body> 
</html> 
<!DOCTYPE html> 
<html> 
<body> 
 
<h1>My First Web Page</h1> 
<p>My First Paragraph</p> 
 
<p id="demo"></p> 
 
<script> 
document.getElementById("demo").innerHTML = 5 + 6; 
</script> 
 
</body> 
</html>


---

## Page 2

Using document.write() 
<!DOCTYPE html> 
<html> 
<body> 
 
<h1>My First Web Page</h1> 
<p>My first paragraph.</p> 
 
<script> 
document.write(5 + 6); 
</script> 
 
</body> 
</html> 
Using window.alert() 
<!DOCTYPE html> 
<html> 
<body> 
 
<h1>My First Web Page</h1> 
<p>My first paragraph.</p> 
 
<script> 
window.alert(5 + 6); 
</script> 
 
</body> 
</html> 
Using console.log() 
<!DOCTYPE html> 
<html> 
<body> 
 
<script> 
console.log(5 + 6); 
</script> 
 
</body> 
</html>


---

## Page 3

JavaScript Statements 
<!DOCTYPE html> 
<html> 
<body> 
<h2>JavaScript Statements</h2> 
<p>A <b>JavaScript program</b> is a list of <b>statements</b> to be executed by a computer.</p> 
<p id="demo"></p> 
<script> 
var x, y, z;  // Statement 1 
x = 5;    // Statement 2 
y = 6;    // Statement 3 
z = x + y;  // Statement 4 
document.getElementById("demo").innerHTML = 
"The value of z is " + z + ".";   
</script> 
</body> 
</html> 
multiple statements 
<!DOCTYPE html> 
<html> 
<body> 
<h2>JavaScript Statements</h2> 
<p>Multiple statements on one line is allowed.</p> 
<p id="demo1"></p>


---

## Page 4

<script> 
var a, b, c; 
a = 5; b = 6; c = a + b; 
document.getElementById("demo1").innerHTML = c; 
</script> 
</body> 
</html> 
JavaScript Line Length and Line Breaks 
<!DOCTYPE html> 
<html> 
<body> 
<h2>JavaScript Statements</h2> 
<p id="demo"></p> 
<script> 
document.getElementById("demo").innerHTML = 
"Hello Dolly!"; 
</script> 
</body> 
</html> 
JavaScript Comments 
<!DOCTYPE html> 
<html> 
<body> 
<h2>JavaScript Comments are NOT Executed</h2>


---

## Page 5

<p id="demo"></p> 
<script> 
var x; 
x = 5; 
// x = 6; I will not be executed 
document.getElementById("demo").innerHTML = x; 
</script> 
</body> 
</html> 
Concatenation 
<!DOCTYPE html> 
<html> 
<body> 
<h2>JavaScript Expressions</h2> 
<p>Expressions compute to values.</p> 
<p id="demo"></p> 
<script> 
document.getElementById("demo").innerHTML = "John" + " "  +2*3 + " Doe"; 
</script> 
</body> 
</html> 
JavaScript is Case Sensitive 
 
<!DOCTYPE html> 
<html>


---

## Page 6

<body> 
<h2>JavaScript is Case Sensitive</h2> 
<p>Try change lastName to lastname.</p> 
<p id="demo"></p> 
<script> 
var lastname, lastName; 
lastName = "Doe"; 
lastname = "Peterson"; 
document.getElementById("demo").innerHTML = lastName; 
</script> 
</body> 
</html> 
JavaScript Arrays 
<!DOCTYPE html> 
<html> 
<body> 
<h2>JavaScript Arrays</h2> 
<p>Array indexes are zero-based, which means the first item is [0].</p> 
<p id="demo"></p> 
<script> 
var cars = ["Saab","Volvo","BMW"]; 
 
document.getElementById("demo").innerHTML = cars[0]; 
</script> 
</body> 
</html>


---

## Page 7

JavaScript Objects 
 
<!DOCTYPE html> 
<html> 
<body> 
<h2>JavaScript Objects</h2> 
<p id="demo"></p> 
<script> 
var person = { 
  firstName : "John", 
  lastName  : "Doe", 
  age     : 50, 
  eyeColor  : "blue" 
}; 
document.getElementById("demo").innerHTML = 
person.firstName + " is " + person.age + " years old."; 
</script> 
</body> 
</html>


---
