Final Exam weightage : 40 %

List of Topics Weeks Contact Hours CLO(s)
Introduction to Web Development
Front-end vs Back-end Development 0.5 1.5 1,2,7,12
HTML, HTML5 1 3 1,2,3,5,8
CSS, CSS3 1 3
Bootstrap 1 3
JavaScript fundamentals, ES6
(ECMAScript 6) 2 6 1,2,3,5,8
DOM 1 3
Introduction to React
Asynchronous JavaScript 3 9 1,2,3,5
Introduction to Express, FETCH, AXIOS 2 6 1,2,3,5,8
MongoDB 1.5 4.5 5,12,6
Introduction to Node 1.5 4.5 1,2,3,5
Advance topics- Serverless 0.5 1.5 1,2,3,4, 5,12
Deployment and Web Programming
practices and Demos 1 3 1,6,7,9,10,11
Total







exam pattern 
Based on the syllabus and past exam questions you provided, here’s a breakdown of the **most important topics to focus on for CS-4032 Web Programming**:

---

## **1. HTML & CSS (Basics and Styling)**

* **HTML**:

  * Tags: `<h1>`–`<h6>`, `<ol>`, `<ul>`, `<li>`, `<div>`, `<span>`, `<a>`, `<form>`, `<input>`, `<button>`
  * Attributes: `id`, `class`, `style`, `name`
  * Forms and input handling basics
* **CSS**:

  * Selectors: `#id`, `.class`, element selectors
  * Properties: `background-color`, `font-size`, `font-family`, `color`
  * Bootstrap basics: `.container`, `.container-fluid`, responsive grid (`rows` and `columns`)

> **Focus:** MCQs frequently test syntax, selectors, and Bootstrap classes.

---

## **2. JavaScript & ES6**

* Variables: `var`, `let`, `const`
* Data types: `Number`, `String`, `Array`, `Object`
* Arrays: `push()`, `pop()`, `unshift()`, `map()`, `filter()`
* Functions:

  * Regular and arrow functions
  * Scope of `this` in arrow vs normal functions (important for React handlers)
* Error handling: `try...catch`
* `console.count()` and debugging basics
* DOM manipulation and event handling

> **Focus:** Functional JS, array methods, `this` behavior in callbacks.

---

## **3. React**

* **Components**:

  * Class-based and functional
  * Stateful vs stateless
* **State & Props**:

  * Passing data from parent to child using props
  * `this.setState` for updating state in class components
* **Event handlers**:

  * Arrow functions needed for correct `this` binding
* **List rendering**:

  * Using `map()`, `key` attribute importance
* **React Lifecycle**:

  * `componentDidMount` for API calls
* **React + Redux (if included)**:

  * Store, Actions, Reducers, Dispatch, Connect
* **Creating apps**:

  * `npx create-react-app my-app`

> **Focus:** State management, event handling, rendering lists, connecting to Redux.

---

## **4. Node.js & Express**

* Creating a server: `express()`, `app.listen()`
* Routes: `app.get()`, `app.post()`, `app.all()`
* Middleware:

  * `app.use()`
  * Request logging, error-handling middleware
* Sending responses:

  * `res.send()`, `res.json()`
* Fetching data from routes using client-side Axios/Fetch
* Express Templates (EJS):

  * Rendering dynamic data with `res.render()`
  * Using `<%= %>` syntax for dynamic content
* Route parameters:

  * `/:param`, regex-like paths (`?`, `+`, `*`)
* Bonus: Error handling in Express routes

> **Focus:** Middleware flow, route handling, sending JSON, URL params, templates.

---

## **5. MongoDB & Mongoose**

* CRUD operations:

  * `find()`, `insertOne()`, `updateOne()`, `deleteOne()`
* Connecting Node.js app to MongoDB:

  * `mongoose.connect()`
* Defining schema and models:

  * `new mongoose.Schema({})`
  * `mongoose.model()`
* Fetching data to send via Express routes

> **Focus:** Integration with Express, retrieving data for API endpoints.

---

## **6. Asynchronous JS**

* Promises, async/await
* Event loop, non-blocking behavior
* Fetching API data using Axios or Fetch
* Error handling in async operations

> **Focus:** componentDidMount, API calls in React, Express async routes.

---

## **7. Exam Patterns**

* MCQs: HTML, CSS, JS basics, React, Node, MongoDB syntax
* Practical/Code output:

  * React: `setState`, event handling
  * Express: middleware and route outputs
  * Node + MongoDB: fetch data and render
* Short practical:

  * Show list data, manipulate state
  * Use EJS template for dynamic content

---

### ✅ **Priority Topics**

| Priority  | Topics                                                                                                  |
| --------- | ------------------------------------------------------------------------------------------------------- |
| Very High | React (state, props, lifecycle, event handlers), Express middleware & routes, MongoDB CRUD, async/await |
| High      | JavaScript basics (arrays, functions, `this`, error handling), Node.js server basics                    |
| Medium    | HTML/CSS fundamentals, Bootstrap, Express templates (EJS)                                               |
| Low       | Advanced Redux details, serverless concepts, deployment demos                                           |

---
