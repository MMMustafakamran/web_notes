# 📘 **Express.js Exam-Focused Notes with Question Predictions**

---

## 🏗️ **1. Express Basics & Server Setup**

### Core Characteristics:
- **Minimal** – Lightweight framework that stays out of your way
- **Flexible** – Extensible through middleware
- **Unopinionated** – You decide structure, middleware order, file organization

### Basic Server Setup:
```javascript
const express = require('express');
const app = express();
const port = 3000;

app.get('/', (req, res) => res.send('Hello World!'));
app.listen(port, () => console.log(`Server running on port ${port}`));
```

🔴 **PREDICTED QUESTION TYPE:** "Write a basic Express server that listens on port 3000 and returns 'Hello World' for the root path."

---

## 🛣️ **2. Routing Fundamentals**

### Route Structure:
```javascript
app.METHOD(PATH, HANDLER)
```

### Common HTTP Methods:
- `GET` – Retrieve data
- `POST` – Create/send data
- `PUT` – Update/replace data
- `DELETE` – Remove data

### Route Parameters (EXAM FAVORITE):
```javascript
// Correct way
app.get('/user/:id', (req, res) => {
    const userId = req.params.id;  // NOT req.query.id!
});

// URL: /user/123 → req.params.id = "123"
```

🔴 **PREDICTED QUESTION TYPE:** "Find the bug in this route" or "Write a route that accepts user ID as parameter"

### Route Patterns (100% IN EXAM):
| Pattern | Example Matches | Description |
|---------|----------------|-------------|
| `/ab?cd` | `/acd`, `/abcd` | `b` is optional |
| `/ab+cd` | `/abcd`, `/abbcd`, `/abbbcd` | `b` repeats 1+ times |
| `/ab*cd` | `/abcd`, `/abxcd`, `/ab123cd` | `*` matches any chars between |
| `/ab(cd)?e` | `/abe`, `/abcde` | `(cd)` group is optional |
| `/.*fly$/` | `/butterfly`, `/dragonfly` | Regex: ends with "fly" |
| `/flights/:from-:to` | `/flights/LAX-SFO` | Multiple params with separator |

🔴 **PREDICTED QUESTION TYPE:** "Which URLs match this pattern?" or "Explain this route pattern"

### Special Route Methods:
```javascript
app.all('/secret', ...)  // Matches ALL HTTP methods for this path
app.route('/book')       // Chainable route handlers
  .get(...)
  .post(...)
  .put(...)
```

---

## ⚙️ **3. Middleware (GUARANTEED EXAM QUESTION)**

### What is Middleware?
Functions with access to `req`, `res`, `next` that:
1. Execute code
2. Modify req/res objects
3. End request-response cycle
4. Call next middleware

### Middleware Rules (MEMORIZE FOR EXAM):
1. **Order matters** – Executes in defined order
2. **Must call `next()`** to pass to next middleware
3. **OR send response** (`res.send()`, `res.json()`, etc.)
4. **Don't do both** – If you call `next()`, don't send response

🔴 **PREDICTED QUESTION TYPE:** "Trace the middleware execution" or "Find why this middleware chain breaks"

### Types of Middleware:

#### 1. Application-Level:
```javascript
app.use((req, res, next) => {
    console.log('Time:', Date.now());
    next();  // ← MUST CALL THIS unless sending response
});
```

#### 2. Error-Handling Middleware (EXAM FAVORITE):
```javascript
// MUST have 4 parameters - THIS WILL BE TESTED!
app.use((err, req, res, next) => {
    console.error(err.stack);
    res.status(500).send('Something broke!');
});
```

🔴 **PREDICTED QUESTION TYPE:** "Fix this error handler" or "Write error handling middleware"

### Skipping Middleware:
```javascript
next('route')    // Skip to next route in same router
next('router')   // Exit current router entirely
```

---

## 🎨 **4. Templating with EJS (LIKELY IN EXAM)**

### Setup:
```javascript
app.set('view engine', 'ejs');
```

### Rendering Templates:
```javascript
app.get('/books', (req, res) => {
    const books = [...];
    res.render('books', { books: books });  // Pass data as object
});
```

### EJS Syntax (MUST KNOW):
```html
<% %>    <!-- Execute JavaScript (no output) -->
<%= %>   <!-- Output escaped value -->
<%- %>   <!-- Output raw HTML -->
```

🔴 **PREDICTED QUESTION TYPE:** "Write EJS template to display array of books" or "Fix this EJS syntax error"

---

## 🔄 **5. REST API Implementation (ALWAYS IN EXAM)**

### CRUD Operations Table:
| Method | Endpoint | Action |
|--------|----------|--------|
| POST | `/books` | Create new book |
| GET | `/books` | Get all books |
| GET | `/books/:id` | Get specific book |
| PUT/POST | `/books/:id` | Update book |
| DELETE | `/books/:id` | Delete book |

### Example CRUD Endpoints:
```javascript
// CREATE (POST) - EXAM FAVORITE
app.post('/register', (req, res) => {
    const { username, password } = req.body;
    if (password.length < 8) {
        return res.status(400).json({ error: "Password too short" });
    }
    res.status(201).json({ message: "User created" });
});

// READ ALL (GET)
app.get('/tasks', async (req, res) => {
    const tasks = await Task.find({ completed: false }); // Filtering likely asked
    res.json(tasks);
});
```

🔴 **PREDICTED QUESTION TYPE:** 
1. "Write a POST route with validation"
2. "Create CRUD operations for a resource"
3. "Add error handling to MongoDB query"

---

## 🗄️ **6. MongoDB with Mongoose (HIGHLY LIKELY)**

### Connection Setup:
```javascript
mongoose.connect('mongodb://localhost:27017/mydb', {
    useNewUrlParser: true,
    useUnifiedTopology: true
});
```

### Schema Definition:
```javascript
const taskSchema = new mongoose.Schema({
    title: String,
    completed: Boolean  // Filtering on this field often asked
});
const Task = mongoose.model('Task', taskSchema);
```

### CRUD with Mongoose (EXAM FAVORITE):
```javascript
// GET filtered results - VERY COMMON QUESTION
app.get('/incomplete-tasks', async (req, res) => {
    try {
        const tasks = await Task.find({ completed: false });
        res.json(tasks);
    } catch (err) {
        res.status(500).json({ error: err.message });
    }
});
```

🔴 **PREDICTED QUESTION TYPE:** "Replace JSON array with MongoDB" or "Write GET route with filter"

---

## ⚠️ **7. Common Exam Pitfalls (WILL BE TESTED)**

### 1. Parameter vs Query Confusion (GUARANTEED):
```javascript
// WRONG - This will appear in "find the bug" question
app.get('/user/:id', (req, res) => {
    const user = findUser(req.query.id);  // ❌ Should be req.params.id
});

// CORRECT ANSWER
app.get('/user/:id', (req, res) => {
    const user = findUser(req.params.id);  // ✅
});
```

### 2. Middleware Chain Breaking (VERY COMMON):
```javascript
// QUESTION: "What gets logged?"
app.use((req, res, next) => {
    console.log('A');
    next();
});

app.use((req, res) => {
    console.log('B');
    res.send('Done');
});

app.use(() => {
    console.log('C');  // Answer: Never prints
});
```

### 3. Error Handler Signature (ALWAYS TESTED):
```javascript
// WRONG - Will be in "fix the code" question
app.use((err, req, res) => {  // ❌ Missing 'next'
    res.status(500).send('Error');
});

// CORRECT ANSWER
app.use((err, req, res, next) => {  // ✅ All 4 parameters
    res.status(500).send('Error');
});
```

---

## 🎯 **8. Question Types Breakdown**

### Type 1: Code Analysis (Short Answer)
- "Find the bug in this route"
- "What will be logged/output?"
- "Explain this route pattern"

### Type 2: Implementation (Medium Answer)
- "Write a POST route with validation"
- "Create error handling middleware"
- "Convert JSON route to use MongoDB"

### Type 3: Full Implementation (Long Answer)
- "Build complete CRUD API for X resource"
- "Implement authentication middleware"
- "Create EJS template with data rendering"

### Type 4: Explanation
- "Explain middleware execution order"
- "Difference between app.use() and app.get()"
- "When to use params vs query vs body"

---

## 📝 **9. Previous Exam Patterns Analysis**

### From Mock Final Paper:
1. **Parameter access bug** – Fix `req.query` to `req.params`
2. **POST route with validation** – Return 400 if password < 8 chars
3. **Mongoose filtered query** – `find({ completed: false })`

🔴 **EXPECT SIMILAR:** Fixing common mistakes + simple validation + MongoDB queries

### From Final 2024 Paper:
1. **Middleware trace** – Follow `next()` calls carefully
2. **JSON ↔ MongoDB conversion** – Know both approaches
3. **EJS template** – Loop through array and display
4. **Route pattern matching** – Match URLs to patterns

🔴 **EXPECT SIMILAR:** Execution tracing + data source switching + templating

---

## 🚨 **10. High-Probability Exam Questions**

### GUARANTEED TO APPEAR:
1. **Fix this bug:** `req.query` vs `req.params` confusion
2. **Write a route:** POST with validation (check password length, email format)
3. **Explain pattern:** What URLs match `/ab?cd` or `/.*fly$/`
4. **Middleware trace:** Given code, what gets logged in what order

### VERY LIKELY:
1. **EJS template:** Display array of objects in table/list
2. **Mongoose query:** Filter by status (`completed: false`)
3. **Error handler:** Write 4-parameter error middleware
4. **REST endpoint:** Complete one CRUD operation

### POSSIBLE:
1. **Static files:** Serve from `public` directory
2. **Router:** Create and use Express Router
3. **Body parsing:** Setup `express.json()` middleware
4. **Route chaining:** Use `app.route()` or `router.route()`

---

## ⏱️ **11. Exam Strategy**

### Quick Reference Sheet:
```javascript
// PARAMETERS:
req.params.id      // /users/:id
req.query.page     // /users?page=1
req.body.name      // POST/PUT data

// RESPONSES:
res.send('text')           // Text/HTML
res.json({data: value})    // JSON
res.status(404).send()     // Status + message
res.render('view', data)   // Template

// MIDDLEWARE:
next()           // Continue
next('route')    // Skip to next route
res.send()       // End chain
```

### When You See:
- **"Bug" or "Error"** → Check `req.params` vs `req.query`
- **"Middleware order"** → Trace `next()` calls
- **"Validation"** → Check length, format, return 400 if invalid
- **"Mongoose"** → Add `async/await` + `try/catch`
- **"Template"** → Use `<%= %>` for output, `<% %>` for logic

### Time Allocation:
- **Short answers (5 min):** Bug fixes, explanations
- **Medium answers (10 min):** Single route implementation
- **Long answers (15 min):** Full CRUD or templating

---

## 📌 **12. Last-Minute Checklist**

### MEMORIZE THESE:
- [ ] `req.params` = route parameters (`:id`)
- [ ] `req.query` = query string (`?page=1`)
- [ ] `req.body` = request body (needs parser)
- [ ] Error handlers need 4 parameters
- [ ] `next()` must be called or response sent
- [ ] EJS: `<% %>` for logic, `<%= %>` for output
- [ ] Status codes: 200 OK, 201 Created, 400 Bad Request, 404 Not Found
- [ ] `find({ completed: false })` for filtering

### COMMON MISTAKES TO AVOID:
- Using `req.query` for route parameters
- Forgetting `async/await` with Mongoose
- Missing `next` parameter in error handler
- Not calling `next()` in middleware
- Forgetting to set view engine for EJS
- Not handling errors in async routes

---

**REMEMBER:** Exams often test the *same concepts* from previous papers, just with different data. Focus on patterns, not memorizing exact code!