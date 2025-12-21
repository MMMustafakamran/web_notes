# **Express.js Questions from the Provided Papers**

## **From `mockfinal.txt`**

### **Q1 – Part b (Short Answer – Code Analysis)**
**Question 3:** Identify the error in this route definition.  
```javascript
app.get('/user/:id', (req, res) => {
  const user = findUser(req.query.id);
  res.send(user);
});
```
**Issue:** The route uses a URL parameter `:id`, but the code accesses `req.query.id` (query string) instead of `req.params.id`. This will cause `findUser(req.query.id)` to likely return `undefined` or fail.

---

### **Q2 – Part b (Application Development – Express API)**
**Question:** Write an Express POST route `/register`.  
- It receives `username` and `password` in the request body.  
- If `password` length is less than 8, return status 400 with a JSON error message.  
- Otherwise, return status 201 with a success message.

**Solution Outline:**
```javascript
app.post('/register', (req, res) => {
    const { username, password } = req.body;
    if (!password || password.length < 8) {
        return res.status(400).json({ error: "Password must be at least 8 characters" });
    }
    res.status(201).json({ message: "User registered successfully" });
});
```

---

### **Q2 – Part c (Full-Stack Integration – MongoDB with Mongoose)**
**Question:** Assume you have a MongoDB collection `Tasks`. Write the Node/Express code to:  
1. Connect to MongoDB using Mongoose.  
2. Define a Schema for `Task` (title: String, completed: Boolean).  
3. Create a GET route `/tasks` that returns only the tasks where `completed` is `false`.

**Solution Outline:**
```javascript
const mongoose = require('mongoose');
mongoose.connect('mongodb://localhost:27017/taskdb', { useNewUrlParser: true, useUnifiedTopology: true });

const taskSchema = new mongoose.Schema({
    title: String,
    completed: Boolean
});
const Task = mongoose.model('Task', taskSchema);

app.get('/tasks', async (req, res) => {
    try {
        const incompleteTasks = await Task.find({ completed: false });
        res.json(incompleteTasks);
    } catch (err) {
        res.status(500).json({ error: err.message });
    }
});
```

---

### **Q3 – Part b (Advanced Concepts – Express Routing & Regex)**
**Question:** Explain what types of URLs will match the following Express routes and what parameters will be captured:  

1. `app.get('/item/:name([a-zA-Z]+)', ...)`  
   - Matches `/item/Apple`, `/item/Book`  
   - Does **not** match `/item/123` or `/item/Book123`  
   - Captures `req.params.name`

2. `app.get('/files/*.*', ...)`  
   - Matches `/files/document.pdf`, `/files/image.jpg`  
   - Captures wildcard segments for filename and extension

3. `app.get('/post/:id?', ...)`  
   - Matches `/post/123` and `/post`  
   - `:id` is optional

4. `app.get('/user(name)?', ...)`  
   - Matches `/user` and `/username`  
   - `(name)` is optional

5. `app.put('/api/v1/update/:id', ...)`  
   - Matches PUT requests like `/api/v1/update/100`  
   - Captures `req.params.id`

6. `app.get(/.*test$/, ...)`  
   - Matches any URL ending with `test` (e.g., `/mytest`, `/api/test`)  
   - Uses regex pattern

7. `app.use('/admin', checkAuth, adminRouter)`  
   - All routes under `/admin` will first pass through `checkAuth` middleware  
   - Then route to `adminRouter`

---

## **From `final-2024.txt`**

### **Q1 – Part b (Short Answer – Code Analysis)**
**Question 4:** What will be the output of the following Express.js script when a GET request is made to `/about`?  
```javascript
app.use((req, res, next) => {
    console.log('t1');
    next();
});
app.get('/about1', (req, res) => { console.log('about1'); });
app.use(function(req, res, next){ console.log('t2'); });
app.post('/about1', (req, res) => { console.log('about2'); });
app.post('/about', (req, res) => { console.log('about3'); });
app.get('/about', (req, res) => { console.log('about4'); });
```
**Output:**  
```
t1
t2
```
**Explanation:**  
- `t1` logs from the first middleware (matches all routes).  
- The GET `/about` route is defined, but there’s a middleware `app.use(...)` after `/about1` that runs **before** reaching `/about` and does **not** call `next()`, so execution stops at `t2`.

---

### **Q2 – Part b (Express Server with JSON data)**
**Question:** Create your own web server with Express and save user info in JSON format. Write a route `/getUsers` with GET method.  

**Solution:**
```javascript
const express = require('express');
const app = express();
const PORT = 3001;

const users = [
  { name: "John Doe", email: "john@example.com", age: 30 },
  { name: "Jane Smith", email: "jane@example.com", age: 25 }
];

app.get('/getUsers', (req, res) => {
  res.json(users);
});

app.listen(PORT, () => {
  console.log(`Server is running on http://localhost:${PORT}`);
});
```

---

### **Q2 – Part c (Express with MongoDB)**
**Question:** Instead of sending information from JSON, get the data from MongoDB. Write the code for accessing data from MongoDB and sending to the client.  

**Solution:**
```javascript
const express = require('express');
const mongoose = require('mongoose');
const app = express();
const PORT = 3001;

mongoose.connect('mongodb://localhost:27017/mydatabase', { useNewUrlParser: true, useUnifiedTopology: true });

const userSchema = new mongoose.Schema({
  name: String,
  email: String,
  age: Number
});
const User = mongoose.model('User', userSchema);

app.get('/getUsers', async (req, res) => {
  try {
    const users = await User.find({});
    res.json(users);
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
});

app.listen(PORT, () => {
  console.log(`Server is running on http://localhost:${PORT}`);
});
```

---

### **Q3 – Part a (Express with EJS Templates)**
**Question:** Use templates for showing books data on requesting `/showBooks` route. The book object contains isbn, title, and price.  

**Solution (`app.js`):**
```javascript
const express = require('express');
const app = express();
const port = 3000;

app.set('view engine', 'ejs');

const books = [
    { isbn: '978-3-16-148410-0', title: 'Book One', price: 29.99 },
    { isbn: '978-1-4028-9462-6', title: 'Book Two', price: 39.99 }
];

app.get('/showBooks', (req, res) => {
    res.render('books', { books: books });
});

app.listen(port, () => {
    console.log(`Server is running on http://localhost:${port}`);
});
```

**EJS Template (`views/books.ejs`):**
```html
<!DOCTYPE html>
<html>
<head>
    <title>Books List</title>
</head>
<body>
    <h1>Books List</h1>
    <table border="1">
        <tr>
            <th>ISBN</th>
            <th>Title</th>
            <th>Price</th>
        </tr>
        <% books.forEach(function(book) { %>
            <tr>
                <td><%= book.isbn %></td>
                <td><%= book.title %></td>
                <td><%= book.price %></td>
            </tr>
        <% }); %>
    </table>
</body>
</html>
```

---

### **Q3 – Part b (Express Route Patterns)**
**Question:** Explain the following routes and provide examples of URLs which can be called.  

1. `app.get('/ab?cd', ...)`  
   - Matches: `/acd`, `/abcd`  
   - `b` is optional.

2. `app.get('/ab+cd', ...)`  
   - Matches: `/abcd`, `/abbcd`, `/abbbcd`  
   - `b` can repeat one or more times.

3. `app.get('/ab*cd', ...)`  
   - Matches: `/abcd`, `/abxcd`, `/ab123cd`  
   - `*` matches any characters between `ab` and `cd`.

4. `app.get('/ab(cd)?e', ...)`  
   - Matches: `/abe`, `/abcde`  
   - `(cd)` is optional.

5. `app.get(/.*fly$/, ...)`  
   - Matches: `/butterfly`, `/dragonfly`  
   - Regex: any string ending with `fly`.

6. `app.get('/flights/:from-:to', ...)`  
   - Matches: `/flights/LAX-SFO`  
   - Params: `req.params.from = 'LAX'`, `req.params.to = 'SFO'`.

7. `app.all('/secret', ...)`  
   - Matches **all** HTTP methods (GET, POST, PUT, etc.) to `/secret`.  
   - Example: `GET /secret`, `POST /secret`.