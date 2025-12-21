# 📘 Node.js & Express Exam Notes

---

## 🔹 **Core Node.js Concepts**

### **What is Node.js?**
- JavaScript runtime built on **V8 engine**.
- **Asynchronous, event-driven**, single-threaded.
- Uses **event loop** for non-blocking I/O.
- Good for I/O-intensive apps, not for CPU-intensive tasks.
- Full-stack JS (MEAN/MERN stacks).

### **Global Objects**
Available without import:
- `__dirname`, `__filename`
- `require()`, `exports`, `module`
- `console`, `setTimeout`, `process`

### **Event Loop Example**
```javascript
console.log("1");
setTimeout(() => console.log("2"), 1000);
console.log("3");
// Output: 1, 3, 2
```
- `setTimeout` is async → goes to callback queue.

### **Utility Modules**
- `path`: handle file paths.
- `os`: OS info (type, memory).
- `dns`: domain name resolution.
- `net`: TCP server/client.
- `domain`: error handling.

---

## 📦 **NPM & Package Management**

### **Key Commands**
| Command | Purpose |
|---------|---------|
| `npm init` | Create `package.json` |
| `npm install <pkg>` | Install local |
| `npm install -g <pkg>` | Install global |
| `npm install --save` | Add to `dependencies` |
| `npm install --save-dev` | Add to `devDependencies` |
| `npm ci` | Install from `package-lock.json` |
| `npm audit` | Check vulnerabilities |
| `npx <command>` | Run local CLI tool |

### **package.json Sections**
```json
{
  "scripts": { "start": "node app.js" },
  "dependencies": { "express": "^4.18.0" },
  "devDependencies": { "nodemon": "^2.0.0" }
}
```
- `^`: minor/patch updates allowed.
- `~`: patch updates only.

---

## 🌐 **Express.js Essentials**

### **Creating an Express App**
```javascript
const express = require('express');
const app = express();
app.listen(3000);
```

### **Basic Routing**
```javascript
app.get('/', (req, res) => res.send('Hello'));
app.post('/', (req, res) => res.status(201).send());
app.put('/', (req, res) => res.send('Updated'));
app.delete('/', (req, res) => res.send('Deleted'));
```

### **Route Parameters & Query**
```javascript
// Route param
app.get('/user/:id', (req, res) => {
  res.send(req.params.id);
});

// Query string
app.get('/search', (req, res) => {
  res.send(req.query.q);
});
```

### **Middleware**
```javascript
app.use(express.json()); // Parse JSON bodies
app.use(express.urlencoded({ extended: true })); // Parse form data
app.use((req, res, next) => {
  console.log('Time:', Date.now());
  next();
});
```

---

## 🗂 **MongoDB + Mongoose**

### **Connection**
```javascript
const mongoose = require('mongoose');
mongoose.connect('mongodb://localhost:27017/mydb');
```

### **Schema & Model**
```javascript
const taskSchema = new mongoose.Schema({
  title: String,
  completed: Boolean
});
const Task = mongoose.model('Task', taskSchema);
```

### **CRUD Example**
```javascript
// GET incomplete tasks
app.get('/tasks', async (req, res) => {
  const tasks = await Task.find({ completed: false });
  res.json(tasks);
});
```

---

## ✅ **Common Exam Patterns**

### **1. Error in Route Definition**
❌ Wrong:
```javascript
app.get('/user/:id', (req, res) => {
  const user = findUser(req.query.id); // Should be req.params.id
});
```

✅ Correct:
```javascript
app.get('/user/:id', (req, res) => {
  const user = findUser(req.params.id);
});
```

### **2. Password Validation Route**
```javascript
app.post('/register', (req, res) => {
  const { username, password } = req.body;
  if (password.length < 8) {
    return res.status(400).json({ error: "Password too short" });
  }
  res.status(201).json({ message: "User created" });
});
```

### **3. Route Matching Patterns**

| Route Pattern | Matches | Example |
|--------------|---------|---------|
| `/ab?cd` | acd, abcd | `?` = 0 or 1 |
| `/ab+cd` | abcd, abbcd, abbbcd | `+` = 1 or more |
| `/ab*cd` | abXcd, ab123cd | `*` = any chars |
| `/ab(cd)?e` | abe, abcde | `()` group optional |
| `/:name([a-z]+)` | Only lowercase letters | Regex constraint |
| `/files/*.*` | files/any.extension | Wildcard filename |
| `/post/:id?` | /post, /post/123 | Optional param |
| `/*test$` | anything ending with "test" | Regex route |

---

## 🧠 **Quick Review Questions**

### **MCQs to Remember**
- Cookie sending → `res.cookie()`
- File path module → `path`
- Global install → `npm install -g`
- Default port → `3000`
- Create both client/server → `http` module
- Start Express server → `app.listen()`
- Body parsing middleware → `body-parser`
- MongoDB connect → `mongoose.connect()`
- JSON response → `res.json()`
- Initialize project → `npm init`
- Define middleware → `app.use()`
- Built-in middleware → `express.json()`

---

## 📌 **Exam Tips**
1. **Watch for `req.params` vs `req.query`**.
2. **Always call `next()` in middleware unless ending response**.
3. **Use `res.status()` for HTTP codes**.
4. **Mongoose methods are async—use `await` or `.then()`**.
5. **`package-lock.json` ensures consistent installs**.
6. **Event loop order: sync code → microtasks → macrotasks**.

---
