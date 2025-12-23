Here are the **solutions** to all the React-related questions from both exam files:

---

### **From `sessional2_2024.txt`:**

#### **Question 1**

**i. Difference between Real DOM and Virtual DOM**  
**Real DOM** is the actual browser DOM tree. Updating it is slow because it causes reflow and repaint.  
**Virtual DOM** is a lightweight copy in memory. When state changes, React updates the Virtual DOM first, compares it with the previous version (diffing), then updates only the changed parts in the Real DOM. This improves performance.

**ii. Events in React**  
Common events: `onClick`, `onChange`, `onSubmit`, `onMouseEnter`, `onKeyDown`, etc.  
**Creating an event in React:**

```javascript
function Button() {
  // Step 1: Create an event handler function
  const handleClick = () => alert("Clicked!");
  // Step 2: Attach the event handler to a JSX element
  return <button onClick={handleClick}>Click</button>;
}
```

**iii. Keys props**  
Keys help React identify which items changed, were added, or removed in a list.  
**Necessity:** Yes, keys are necessary when rendering lists to maintain component state correctly and improve performance. Without keys, React may re-render more than needed.

**iv. Types of components in React**

1. **Functional Component:**

```javascript
function Greeting(props) {
  return <h1>Hello, {props.name}</h1>;
}
```

2. **Class Component:**

```javascript
class Greeting extends React.Component {
  render() {
    return <h1>Hello, {this.props.name}</h1>;
  }
}
```

**v. Code output:**

```
array 2: b,e,w,P,r,o,g,r,a,m,m,i,n,g
array 2 updated: web,b,e,w,P,r,o,g,r,a,m,m,i,n,g
array 1: length=17 val=e,w,P,r,o,g,r,a,m,m,i,n,g
array 2: length=18 get=P,r,o,g,r,a,m,m,i,n,g
```

**Why:**

- `arr1.reverse()` mutates `arr1` and returns reference to same array.
- `arr2.push(arr3)` pushes entire array as one element.
- `arr2.unshift("web")` adds "web" at start.
- `arr1.slice(2)` starts from index 2.
- `arr2.slice(-1)` gets last element (which is the `arr3` array).

**vi. Code output:**

```
undefined
NaN
```

**Why:**

- `foo()` logs `undefined` due to variable hoisting (`var x` is hoisted inside function).
- `mult(2, 3)` returns `NaN` because `c` is `undefined`, so `2 * 3 * undefined = NaN`.

---

#### **Question 2**

**ii. React app without create-react-app**

```html
<!-- Full HTML with React in script -->
<script type="text/babel">
  class App extends React.Component {
    state = { inputNo: 0, isEven: "even" };

    handleClick = () => {
      const v = document.getElementById("req").value;
      const isEven = v % 2 === 0 ? "even" : "odd";
      this.setState({ inputNo: v, isEven });
    };

    render() {
      return (
        <div>
          <h1>Input No. {this.state.inputNo}</h1>
          <h1>Result: {this.state.isEven}</h1>
          <input type="number" id="req" />
          <button onClick={this.handleClick}>Check it</button>
        </div>
      );
    }
  }

  ReactDOM.render(<App />, document.getElementById("app"));
</script>
```

---

#### **Question 3**

**Command to create React app:**

```
npx create-react-app quizgame
```

**Directory structure:**

```
quizgame/
├── node_modules/
├── public/
│   ├── index.html
│   └── ...
├── src/
│   ├── App.js
│   ├── index.js
│   └── ...
├── package.json
└── ...
```

**Command to run:**

```
npm start
```

**index.html:**

```html
<!DOCTYPE html>
<html>
  <head>
    ...
  </head>
  <body>
    <div id="root"></div>
  </body>
</html>
```

**index.js:**

```javascript
import React from "react";
import ReactDOM from "react-dom/client";
import App from "./App";

const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(<App />);
```

**QuizGame Component:**

```javascript
import React, { useState, useEffect } from "react";

const QuizGame = () => {
  const [score, setScore] = useState(0);
  const [question, setQuestion] = useState("");
  const [answer, setAnswer] = useState("");
  const [result, setResult] = useState("");
  const operators = ["+", "-", "*", "/", "%"];

  const generateQuestion = () => {
    const op = operators[Math.floor(Math.random() * operators.length)];
    const a = Math.floor(Math.random() * 10) + 1;
    const b = Math.floor(Math.random() * 10) + 1;
    setQuestion(`${a} ${op} ${b}`);
  };

  useEffect(() => generateQuestion(), []);

  const checkAnswer = () => {
    const correct = eval(question);
    if (parseInt(answer) === correct) {
      setScore(score + 1);
      setResult("Correct!");
    } else {
      setScore(score - 1);
      setResult("Wrong!");
    }
    setAnswer("");
    generateQuestion();
  };

  return (
    <div>
      <h1>Math Quiz Game</h1>
      <p>Score: {score}</p>
      <p>Question: {question}</p>
      <input
        type="number"
        value={answer}
        onChange={(e) => setAnswer(e.target.value)}
      />
      <button onClick={checkAnswer}>Submit</button>
      <p>{result}</p>
      {score >= 10 && <h2>You Win!</h2>}
    </div>
  );
};

export default QuizGame;
```

---

### **From `final-2024.txt`:**

#### **MCQ Answers (React-related):**

14. a) `class MyComponent extends React.Component {}`
15. a) Via props
16. a) `this.setState`
17. a) To help identify which items have changed, are added, or removed
18. a) They can be stateful or stateless.
19. a) `npx create-react-app my-app`

---

#### **Q1 Part b Solutions:**

**1. ShowCount Button Error**  
**Error:** `this` is undefined in `foo()` because it's not bound.  
**Fix:** Use arrow function or bind in constructor.

```javascript
foo = (e) => {
  this.setState({ count: this.state.count - 5 });
};
```

**2. Add Item Button Output**  
**Output:** Only "New Item" in list after first click.  
**Why:** `setState({ items: ['New Item'] })` replaces entire array each time.

---

#### **Q2 Solutions:**

**a. React Component Fetching API Data**

```javascript
import React, { useState, useEffect } from "react";
import axios from "axios";

function UserList() {
  const [users, setUsers] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    axios
      .get("https://www.webapi.com/users")
      .then((res) => {
        setUsers(res.data);
        setLoading(false);
      })
      .catch((err) => {
        setError(err);
        setLoading(false);
      });
  }, []);

  if (loading) return <div>Loading...</div>;
  if (error) return <div>Error: {error.message}</div>;

  return (
    <ul>
      {users.map((user) => (
        <li key={user.email}>
          {user.name} - {user.email} - {user.age}
        </li>
      ))}
    </ul>
  );
}
```

**b. Express Server + React Client**  
**Server:**

```javascript
const express = require("express");
const app = express();
app.get("/getUsers", (req, res) => {
  res.json([
    { name: "John", email: "john@test.com", age: 25 },
    { name: "Jane", email: "jane@test.com", age: 30 },
  ]);
});
app.listen(3001);
```

**React Client:**  
Change axios URL to `http://localhost:3001/getUsers`.

**c. MongoDB + Express + React**  
**Server:**

```javascript
const mongoose = require("mongoose");
mongoose.connect("mongodb://localhost:27017/test");
const User = mongoose.model("User", {
  name: String,
  email: String,
  age: Number,
});

app.get("/getUsers", async (req, res) => {
  const users = await User.find();
  res.json(users);
});
```

**React Client:** Same as above.

---

#### **Q3 Solutions:**

**a. Redux Example**  
**Store setup, actions, reducers, connecting components** (as shown in the provided example).

**b. Express Templates for Books**

```javascript
// app.js
app.set("view engine", "ejs");
app.get("/showBooks", (req, res) => {
  const books = [
    { isbn: "123", title: "Book 1", price: 20 },
    { isbn: "456", title: "Book 2", price: 30 },
  ];
  res.render("books", { books });
});
```

**books.ejs:**

```html
<% books.forEach(book => { %>
<div><%= book.title %> - $<%= book.price %></div>
<% }) %>
```

**c. Route Explanations**

1. `/ab?cd` → `acd` or `abcd`
2. `/ab+cd` → `abcd`, `abbcd`, `abbbcd`
3. `/ab*cd` → `abXcd` where X is any string
4. `/ab(cd)?e` → `abe` or `abcde`
5. `/.*fly$/` → `butterfly`, `dragonfly`
6. `/flights/:from-:to` → `flights/LAX-SFO`
7. `app.all('/secret')` → handles all HTTP methods on `/secret`

**Bonus:** 😊 (Smiley face)

---

Let me know if you'd like more detailed explanations for any specific question!
s
