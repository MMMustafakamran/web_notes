# MongoDB Exam-Focused Notes
// server.js


```javascript
// 1. Import required modules
const express = require('express');
const mongoose = require('mongoose');
const app = express();
const PORT = 3001;

// 2. MongoDB connection URI
// Format: mongodb://[host]:[port]/[database_name]
const mongoURI = 'mongodb://localhost:27017/mydatabase';
// This connects to a database called 'mydatabase' on your local machine

// 3. Connect to MongoDB
mongoose.connect(mongoURI, { 
    useNewUrlParser: true, 
    useUnifiedTopology: true 
})
.then(() => console.log('✅ MongoDB connected successfully'))
.catch(err => console.log('❌ Connection error:', err));

// 4. Define a User Schema
// A schema defines the structure of your documents
const userSchema = new mongoose.Schema({
    name: String,      // Field for user's name
    email: String,     // Field for user's email
    age: Number        // Field for user's age
});

// 5. Create a Model from the Schema
//model is the tool in mongoose u use to interact/with the mongodb like a waiter
// This model will interact with the 'users' collection(table)
const User = mongoose.model('User', userSchema);
// Mongoose automatically looks for the plural, lowercase version of your model name
// So 'User' model → 'users' collection

// 6. Create a Route to Get Users
app.get('/getUsers', async (req, res) => {
    try {
        // Find all users in the collection
        // Empty object {} means "no filters, get all documents"
        const users = await User.find({}); // await causes Execution PAUSE here until User.find() completes so that no empty return returneds
        
        // Send the users as JSON response
        res.json({
            success: true,
            count: users.length,
            data: users
        });
    } catch (err) {
        // If there's an error, send error response
        res.status(500).json({
            success: false,
            error: err.message
        });
    }
});

// 7. Start the Server
app.listen(PORT, () => {
    console.log(`🚀 Server running on http://localhost:${PORT}`);
});
```
## 🔍 **Core Concepts (Must Know)**

### 1. **MongoDB Basics**
- **NoSQL database**: Document-oriented, schema-less
- **Structure**: Database → Collections → Documents
- **Key Difference from RDBMS**:
  - No tables → Collections
  - No rows → Documents
  - No columns → Fields
  - No joins → Embedded documents or `$lookup`

### 2. **MongoDB Shell Commands (Exam Focus)**
```bash
# Database operations
use database_name          # Switch/create database
show dbs                   # List databases
db.dropDatabase()          # Delete current database

# Collection operations
show collections           # List collections
db.createCollection("name") # Create collection
db.collection_name.drop()  # Delete collection

# Document CRUD (Shell version)
db.collection.insert({data})
db.collection.find()
db.collection.update(query, newData)
db.collection.remove(query)
```

### 3. **Node.js + MongoDB (Common Exam Code)**

#### **Connection**
```javascript
const MongoClient = require('mongodb').MongoClient;
const url = "mongodb://localhost:27017/mydb";

MongoClient.connect(url, (err, db) => {
  if (err) throw err;
  const dbo = db.db("mydb");
  // Operations here
  db.close();
});
```

#### **Basic Operations**
```javascript
// INSERT
dbo.collection("customers").insertOne({name: "John"}, callback);

// FIND ALL
dbo.collection("customers").find({}).toArray(callback);

// FIND WITH FILTER
dbo.collection("customers").find({address: "Park Lane"}).toArray(callback);

// DELETE ONE
dbo.collection("customers").deleteOne({address: "Mountain 21"}, callback);

// UPDATE ONE
dbo.collection("customers").updateOne(
  {address: "Valley 345"},
  {$set: {address: "Canyon 123"}},
  callback
);
```

### 4. **Important Methods (MCQ Focus)**

| Method | Purpose | Returns |
|--------|---------|---------|
| `find()` | Get all documents | Cursor |
| `findOne()` | Get first matching document | Document |
| `insertOne()` | Insert single document | Insert result |
| `updateOne()` | Update first match | Update result |
| `updateMany()` | Update all matches | Update result |
| `deleteOne()` | Delete first match | Delete result |
| `deleteMany()` | Delete all matches | Delete result |
| `sort({field: 1/-1})` | Sort ascending(1)/descending(-1) | Sorted cursor |
| `limit(n)` | Limit results to n documents | Limited cursor |
| `drop()` | Delete collection | Boolean |

### 5. **Query Operators (Must Remember)**

| Operator | Meaning | Example |
|----------|---------|---------|
| `$gt` | Greater than | `{age: {$gt: 18}}` |
| `$lt` | Less than | `{age: {$lt: 65}}` |
| `$gte` | Greater than or equal | `{score: {$gte: 50}}` |
| `$lte` | Less than or equal | `{score: {$lte: 100}}` |
| `$in` | Match any value in array | `{status: {$in: ["A", "B"]}}` |
| `$regex` | Pattern matching | `{name: {$regex: "^A"}}` |
| `/^S/` | Starts with S (regex shortcut) | `{address: /^S/}` |

### 6. **Mongoose (ODM for MongoDB)**

#### **Connection**
```javascript
const mongoose = require('mongoose');
mongoose.connect('mongodb://localhost:27017/mydb', {
  useNewUrlParser: true,
  useUnifiedTopology: true
});
```

#### **Schema & Model**
```javascript
const userSchema = new mongoose.Schema({
  name: String,
  email: {type: String, required: true},
  age: Number
});

const User = mongoose.model('User', userSchema);
```

#### **CRUD with Mongoose**
```javascript
// CREATE
User.create({name: "John", email: "john@email.com"});

// READ ALL
User.find({});

// READ WITH FILTER
User.find({age: {$gt: 18}});

// UPDATE
User.updateOne({email: "john@email.com"}, {age: 25});

// DELETE
User.deleteOne({email: "john@email.com"});
```

### 7. **Relationships in MongoDB**

#### **One-to-One** (Embedded)
```javascript
// Document contains owner directly
{
  _id: 1,
  street: "100 Maple Street",
  owner: {name: "Alex Merced"}
}
```

#### **One-to-Many** (Reference with populate)
```javascript
// House references Owner ID
const houseSchema = new mongoose.Schema({
  street: String,
  owner: {type: mongoose.Types.ObjectId, ref: "Owner"}
});

// Query with populate
House.find({}).populate("owner");
```

#### **Many-to-Many** (Junction collection)
```javascript
// Separate collection for relationships
const HouseOwner = mongoose.model('HouseOwner', {
  owner: {type: mongoose.Types.ObjectId, ref: "Owner"},
  house: {type: mongoose.Types.ObjectId, ref: "House"}
});
```

### 8. **$lookup (Like SQL JOIN)**
```javascript
dbo.collection('orders').aggregate([
  {
    $lookup: {
      from: "products",           // Collection to join
      localField: "product_id",   // Field from orders
      foreignField: "_id",        // Field from products
      as: "orderdetails"         // Output array field
    }
  }
]).toArray(callback);
```

## 📝 **Exam Tips**

### **Common MCQ Answers:**
1. **find()** - retrieves all documents
2. **CRUD** = Create, Read, Update, Delete
3. **mongoose.connect()** - connects to MongoDB
4. **db.collection.copy()** - NOT a valid operation
5. **$gt** - greater than operator
6. **updateOne()** - updates first matching document
7. **deleteMany()** - deletes multiple documents
8. **sort({field: 1})** - ascending order
9. **limit(5)** - limits to 5 documents
10. **populate()** - fills referenced documents

### **Code Pattern Recognition:**
- **Connection URI always ends with database name**: `mongodb://localhost:27017/mydb`
- **Error handling**: `if (err) throw err;` or `try-catch`
- **Callback pattern**: Last parameter is always callback function
- **Mongoose**: Always define Schema before Model
- **Async/Await**: Modern exams may use async/await instead of callbacks

### **Frequent Exam Tasks:**
1. Connect to MongoDB from Node.js
2. Define a Mongoose schema
3. Create GET/POST routes with database operations
4. Filter data (completed: false, age > 18, etc.)
5. Implement CRUD operations
6. Handle relationships (populate, embedded docs)

## 🎯 **Quick Reference Table**

| Concept | MongoDB Native | Mongoose |
|---------|---------------|----------|
| Connect | `MongoClient.connect()` | `mongoose.connect()` |
| Create | `insertOne()` | `Model.create()` |
| Read | `find()` | `Model.find()` |
| Update | `updateOne()` | `Model.updateOne()` |
| Delete | `deleteOne()` | `Model.deleteOne()` |
| Schema | Not enforced | `new mongoose.Schema()` |
| Relations | `$lookup` (aggregation) | `populate()` |

---

**Remember**: For exams, focus on:
1. Method names and their purposes
2. Correct syntax for common operations
3. Difference between `updateOne` and `updateMany`
4. How to filter and sort data
5. Basic Mongoose schema definition
6. Connection patterns (both native driver and Mongoose)

**Pro Tip**: Practice writing the connection code and basic CRUD operations from memory - these are almost always tested!