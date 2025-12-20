# Chapter: Express.js - Web Application Framework

Express is a minimal and flexible Node.js web application framework that provides a robust set of features for web and mobile applications. It is "unopinionated," meaning it gives developers freedom in how they structure their apps.

---

## 1. Getting Started
### Setup
1. Create a directory: `mkdir myapp`
2. Initialize npm: `npm init`
3. Install Express: `npm install express`

### Hello World Example
```javascript
const express = require('express');
const app = express();
const port = 3000;

app.get('/', (req, res) => {
  res.send('Hello World!');
});

app.listen(port, () => {
  console.log(`Server running on port ${port}`);
});
```

---

## 2. Modules and Asynchrony
- **Modules**: Use `module.exports` to share code across files and `require()` to import it.
- **Async Programming**: Node is single-threaded and non-blocking. Use asynchronous APIs (callbacks, Promises) to avoid blocking the event loop.
- **Error-First Callbacks**: A convention where the first argument of a callback is the error object.

---

## 3. Middleware
Middleware functions are the backbone of Express. They have access to the request (`req`), response (`res`), and the `next` function in the application’s request-response cycle.

### Types of Middleware
1. **Application-level**: Bound to `app` using `app.use()`.
2. **Router-level**: Bound to `express.Router()`.
3. **Built-in**:
   - `express.static()`: Serves static files (CSS, images).
   - `express.json()`: Parses JSON payloads.
   - `express.urlencoded()`: Parses URL-encoded data from forms.
4. **Error-handling**: Defines four arguments: `(err, req, res, next)`.
5. **Third-party**: Community modules like `morgan` (logging) or `cors`.

---

## 4. Routing
Routing defines how an application responds to a client request to a particular endpoint.
- **Methods**: `app.get()`, `app.post()`, `app.put()`, `app.delete()`, `app.all()`.
- **Route Parameters**: Capture values from the URL using `:`.
  ```javascript
  app.get('/users/:userId', (req, res) => {
    res.send(`User ID: ${req.params.userId}`);
  });
```
- **Chaining**: Use `app.route()` to define multiple methods for a single path.

---

## 5. Templating with EJS
EJS (Embedded JavaScript) is a template engine that lets you generate HTML with plain JavaScript.
- **Setup**: `app.set('view engine', 'ejs');`
- **Syntax**:
  - `<% %>`: Executes logic (loops, conditionals).
  - `<%= %>`: Outputs a value to the page.
- **Rendering**: `res.render('index', { name: 'John' });`

---

## 6. Building a REST API
A REST API uses HTTP methods to perform CRUD operations on resources.
- **Create**: `POST /items`
- **Read**: `GET /items` or `GET /items/:id`
- **Update**: `PUT /items/:id`
- **Delete**: `DELETE /items/:id`

---

## Visual Aids from Slides
*(Refer to extracted images for middleware pipeline diagrams and folder structures)*

![Middleware Pipeline](1.Express JS_images/page_13_img_3.png)
![Route Parameters](2.Express JS-2_images/page_20_img_2.png)
![EJS Template](2.Express JS-2_images/page_37_img_1.png)
