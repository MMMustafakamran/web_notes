# Node.js Questions Extracted from Past Papers

## **From: final-2024.txt**

### Q1: Objectives – MCQs

18. Which command is used to install a package globally in Node.js?

    - a) `npm install -g package-name`
    - b) `npm install package-name`
    - c) `npm install global package-name`
    - d) `npm install -global package-name`

19. What is the default port for a Node.js application?

    - a) `3000` | b) `8080` | c) `80` | d) `5000`

20. How do you create both client and server in Node.js?

    - a) Using the `http` module
    - b) Using the `net` module
    - c) Using the `express` module
    - d) Using the `url` module
    - e) Using the `dns` module

21. How do you create a new Express application?

    - a) `var app = express()`
    - b) `var app = new express()`
    - c) `var app = Express()`
    - d) `var app = new Express()`

22. Which method is used to define a GET route in Express?

    - a) `app.get()` | b) `app.route()` | c) `app.fetch()` | d) `app.retrieve()`

23. How do you start a server in Express?

    - a) `app.listen()` | b) `app.start()` | c) `app.run()` | d) `app.launch()`

24. Which middleware function is used to parse incoming request bodies in Express?

    - a) `body-parser` | b) `json-parser` | c) `urlencoded-parser` | d) `data-parser`

25. How do you connect a MongoDB database to a Node.js application using Mongoose?

    - a) `mongoose.connect()`
    - b) `mongoose.bind()`
    - c) `mongoose.link()`
    - d) `mongoose.attach()`

26. How do you make a JSON response in an Express route?

    - a) `res.json()` | b) `res.send()` | c) `res.return()` | d) `res.end()`

27. Which command is used to initialize a new Node.js project?

    - a) `npm init` | b) `npm start` | c) `npm new` | d) `npm create`

28. How do you define middleware in Express.js?

    - a) `app.use()` | b) `app.middleware()` | c) `app.next()` | d) `app.route()`

29. Which of the following is a built-in middleware function in Express.js?
    - a) `morgan` | b) `cookie-parser` | c) `express.Router` | d) `express.json`

### Q1: Code Analysis & Short Answers

4. What will be the output of the following Express.js script when a GET request is made to `/about`?
   ```javascript
   const express = require("express");
   const app = express();
   const port = 3000;
   app.use((req, res, next) => {
     console.log("t1");
     next();
   });
   app.get("/about1", (req, res) => {
     console.log("about1");
   });
   app.use(function (req, res, next) {
     console.log("t2");
   });
   app.post("/about1", (req, res) => {
     console.log("about2");
   });
   app.post("/about", (req, res) => {
     console.log("about3");
   });
   app.get("/about", (req, res) => {
     console.log("about4");
   });
   app.listen(port, () => {
     console.log(`Server running at http://localhost:${port}/`);
   });
   ```

### Q2: Application Development

**b. Express Server with JSON Data [10 Marks]**  
Consider the question Q2 part a. and instead of third party API create your own web server with express and save the required info in json format and write a route `/getUsers` with get method. You are required to write a server code and just calling and receiving logic on client side.

**c. MongoDB Integration with Express [15 Marks]**  
Consider the Q2 part b. and instead of sending information from json, Get the data from MongoDB. Consider the MongoDB has already contains the collection of users. You are required to write a code of accessing data from MongoDB and sending to the client only.

### Q3: Advanced Concepts & Routing

**a. Express Templating with EJS [15 Marks]**  
In the Express Server topic we have studied about Templates. You are required to use the templates for showing books data on requesting `/showBooks` route. The book object contains isbn, title, and price.

**b. Express Route Patterns [28 Marks]**  
Explain the following routes and provide the examples of urls which can be called on the following routes:

1. `app.get('/ab?cd', ...)`
2. `app.get('/ab+cd', ...)`
3. `app.get('/ab*cd', ...)`
4. `app.get('/ab(cd)?e', ...)`
5. `app.get(/.*fly$/, ...)`
6. `app.get('/flights/:from-:to', ...)`
7. `app.all('/secret', ...)`
