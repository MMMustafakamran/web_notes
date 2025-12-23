# Chapter: JavaScript - The Language of the Web

JavaScript is a versatile, high-level language used for both client-side and server-side development. This chapter covers everything from basic syntax to advanced ES6 features and DOM manipulation.

---

## 1. JavaScript Fundamentals

### Variables

- **`var`**: Function-scoped, can be redeclared and hoisted.
- **`let`**: Block-scoped, cannot be redeclared, not hoisted (preferred).
- **`const`**: Block-scoped, constant value (cannot be reassigned).

### Data Types

- **Primitive**: `String`, `Number`, `Boolean`, `Undefined`, `Null`, `Symbol`, `BigInt`.
- **Complex**: `Object`, `Array`, `Function`.
- _Note:_ `typeof null` returns `"object"` (a known bug).

### Operators

- **Assignment**: `=`, `+=`, `-=`, etc.
- **Comparison**: `==` (equal value), `===` (equal value and type), `!=`, `!==`.
- **Logical**: `&&` (AND), `||` (OR), `!` (NOT).

### Control Structures

- **Conditionals**: `if`, `else if`, `else`, `switch`.
- **Loops**:
  - `for`: Classic iterator.
  - `for...in`: Iterates over object keys.
  - `for...of`: Iterates over iterable values (like array elements).
  - `while` & `do...while`.

---

## 2. Strings and Arrays

### String Methods

Common methods: `concat()`, `charAt()`, `replace()`, `toLowerCase()`, `toUpperCase()`, `trim()`, `split()`.

### Advanced Array Methods (ES6+)

- **Manipulation**: `push()`, `pop()`, `shift()`, `unshift()`, `slice()`, `concat()`, `flat()`.
- **Functional**:
  - `map()`: Creates a new array by transforming every element.
  - `filter()`: Creates a new array with elements that pass a test.
  - `find()`: Returns the first element that passes a test.
  - `forEach()`: Executes a function for each element (returns undefined).
- **Ordering**: `sort()` (alphabetical), `reverse()`.

---

## 3. Functions

### Definitions

1. **Declaration**: `function name() { ... }` (Hoisted)
2. **Expression**: `const name = function() { ... }` (Anonymous or named)
3. **Arrow Function**: `const name = () => { ... }` (Shorter syntax, no `this` binding)

### Parameters and Arguments

- **Default Parameters**: `function greet(name = "Guest") { ... }`
- **Arguments Object**: Array-like object containing all arguments passed to a function.
- **Rest Parameters**: `function sum(...nums) { ... }` (Collects remaining arguments into an array).

---

## 4. Object-Oriented JavaScript (Classes)

Classes are syntactical sugar over prototypes.

```javascript
class Rectangle {
  constructor(height, width) {
    this.height = height;
    this.width = width;
  }
  // Getter
  get area() {
    return this.height * this.width;
  }
  // Setter
  set side(val) {
    this.height = val;
    this.width = val;
  }
}
const square = new Rectangle(10, 10);
```

---

## 5. The Document Object Model (DOM)

The DOM is a programming interface for HTML documents. It represents the page as a tree of objects.

### Selecting Elements

- `document.getElementById('id')`
- `document.querySelector('.selector')`
- `document.querySelectorAll('.selector')`

### Manipulating Elements

- **Content**: `element.innerHTML`, `element.textContent`, `element.value` (for inputs).
- **Attributes**: `getAttribute()`, `setAttribute()`, `removeAttribute()`, `hasAttribute()`.
- **Styles**: `element.style.color = 'red';` (uses camelCase for CSS properties).
- **Creation**: `document.createElement('div')`, `parent.appendChild(child)`.

### Event Handling

Events allow code to respond to user actions.

```javascript
const btn = document.querySelector("#myBtn");
btn.addEventListener("click", (event) => {
  console.log("Button clicked!", event.target);
});
```

---

## Visual Aids from Slides

_(Refer to extracted images in the folder for syntax diagrams and DOM tree visualizations)_

![JS Ecosystem](Lecture 1 - Introduction to JavaScript, Control Structure, String_images/page_2_img_1.jpeg)
![Iteration Methods](Lecture 2 - JS arrays_images/page_19_img_1.jpeg)
![Function Types](Lecture 3 - JavaScript Functions and Classes_images/page_20_img_2.png)
