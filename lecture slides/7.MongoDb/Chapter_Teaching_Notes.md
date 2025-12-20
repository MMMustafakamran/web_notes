# Chapter: MongoDB and Mongoose - Database Management

MongoDB is a NoSQL, document-oriented database that stores data in flexible, JSON-like documents. This means fields can vary from document to document and data structure can be changed over time.

---

## 1. Core Concepts
| RDBMS Terminology | MongoDB Terminology |
| :--- | :--- |
| Database | Database |
| Table | Collection |
| Row / Tuple | Document |
| Column | Field |
| Table Join | Embedded Documents / $lookup |
| Primary Key | Primary Key (Default `_id`) |

### Advantages of MongoDB
- **Schema-less**: Documents in a collection don't need the same fields.
- **Easy Scalability**: Designed to scale out across servers.
- **High Performance**: Uses internal memory for faster data access.

---

## 2. MongoDB Shell Commands
- **`use mydb`**: Switch to or create a database.
- **`db.createCollection('users')`**: Create a new collection.
- **`db.users.insert({name: 'John'})`**: Insert a document.
- **`db.users.find()`**: Query all documents.
- **`db.users.update({name: 'John'}, {$set: {age: 30}})`**: Update a document.
- **`db.users.remove({name: 'John'})`**: Remove a document.
- **`db.dropDatabase()`**: Delete the current database.

---

## 3. Using MongoDB with Node.js
### Native MongoDB Driver
Requires the `mongodb` npm package.
```javascript
const { MongoClient } = require('mongodb');
const url = "mongodb://localhost:27017/";

MongoClient.connect(url, (err, db) => {
  if (err) throw err;
  const dbo = db.db("mydb");
  dbo.collection("customers").findOne({}, (err, result) => {
    console.log(result.name);
    db.close();
  });
});
```

---

## 4. Mongoose - Elegant Object Modeling
Mongoose provides a schema-based solution to model your application data.
- **Schema**: Defines the structure of the document.
- **Model**: A constructor that creates documents based on the schema.

### Defining a Schema and Model
```javascript
const mongoose = require('mongoose');

const userSchema = new mongoose.Schema({
  name: String,
  email: { type: String, required: true },
  createdAt: { type: Date, default: Date.now }
});

const User = mongoose.model('User', userSchema);
```

---

## 5. Relationships in MongoDB
1. **One-to-One (Nesting)**: Embed one document inside another.
   - Example: A user and their address.
2. **One-to-Many (References)**: Use `ObjectId` and `ref` to link documents across collections.
   - Use `.populate()` to fetch referenced data.
   ```javascript
   const houseSchema = new mongoose.Schema({
     owner: { type: mongoose.Types.ObjectId, ref: "Owner" }
   });
   ```
3. **Many-to-Many**: Create a third "junction" collection to track relationships between two other collections.

---

## Visual Aids from Slides
*(Refer to extracted images for document structure and relationship diagrams)*

![Document Structure](1. No_SQL_ MongoDB_images/page_17_img_1.jpeg)
![Mongoose Flow](2 No_SQL_ MongoDB_Node.js_images/page_28_img_1.jpeg)
