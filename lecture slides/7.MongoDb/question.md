# Extracted MongoDB Questions

From **Final Exam 2024** (`final-2024.txt`):

## Q1: Objective MCQs

21. Which method is used to retrieve all documents from a MongoDB collection?

- a) find()
- b) getAll()
- c) retrieve()
- d) fetch()

22. What does CRUD stand for in the context of MongoDB?

- a) Create, Read, Update, Delete
- b) Connect, Read, Update, Delete
- c) Create, Retrieve, Update, Delete
- d) Connect, Retrieve, Update, Delete

27. How do you connect a MongoDB database to a Node.js application using Mongoose?

- a) mongoose.connect()
- b) mongoose.bind()
- c) mongoose.link()
- d) mongoose.attach()

33. In MongoDB, which of the following is not a valid collection operation?

- a) db.collection.drop()
- b) db.collection.rename()
- c) db.collection.update()
- d) db.collection.copy()

## Q2: Application Questions

### Part C: MongoDB Integration [15 Marks]

Consider the Q2 part b. and instead of sending information from json, Get the data from MongoDB. Consider the MongoDB has already contains the collection of users. You are required to write a code of accessing data from MongoDB and sending to the client only.

**Solution:**

```javascript
// server.js
const express = require("express");
const mongoose = require("mongoose");
const app = express();
const PORT = 3001;

// MongoDB connection URI
const mongoURI = "mongodb://localhost:27017/mydatabase";

// Connect to MongoDB
mongoose
  .connect(mongoURI, { useNewUrlParser: true, useUnifiedTopology: true })
  .then(() => console.log("MongoDB connected"))
  .catch((err) => console.log(err));

// Define a user schema and model
const userSchema = new mongoose.Schema({
  name: String,
  email: String,
  age: Number,
});

const User = mongoose.model("User", userSchema);

// Route to get users
app.get("/getUsers", async (req, res) => {
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
