# MongoDB with Node.js – Complete Study Notes

---

## **Learning Objectives**
- Node.js MongoDB Create Database
- Node.js MongoDB Create Collection
- Node.js MongoDB Insert
- Node.js MongoDB Find
- Node.js MongoDB Query
- Node.js MongoDB Sort
- Node.js MongoDB Delete
- Node.js MongoDB Drop Collection
- Node.js MongoDB Update
- Node.js MongoDB Limit
- Node.js MongoDB Join
- Node.js MongoDB Relationships using mongoose

---

## **Install MongoDB Driver**
Node.js can be used in database applications with MongoDB.

To download and install the official MongoDB driver, open the Command Terminal and execute:

```bash
npm install mongodb
```

Now you have downloaded and installed a MongoDB database driver.

Node.js can use this module to manipulate MongoDB databases:

```js
var mongo = require('mongodb');
```

---

## **Creating a Database**
To create a database in MongoDB, start by creating a `MongoClient` object, then specify a connection URL with the correct IP address and the name of the database you want to create.

MongoDB will create the database if it does not exist and make a connection to it.

**Example:** Create a database called `"mydb"`

```js
var MongoClient = require('mongodb').MongoClient;
var url = "mongodb://localhost:27017/mydb";

MongoClient.connect(url, function(err, db) {
    if (err) throw err;
    console.log("Database created!");
    db.close();
});
```

Save the code above in a file called `"demo_create_mongo_db.js"` and run:

```bash
node demo_create_mongo_db.js
```

**Note:** MongoDB waits until you have created a collection (table), with at least one document (record) before it actually creates the database (and collection).

---

## **Creating a Collection**
To create a collection in MongoDB, use the `createCollection()` method.

**Example:** Create a collection called `"customers"`

```js
var MongoClient = require('mongodb').MongoClient;
var url = "mongodb://localhost:27017/";

MongoClient.connect(url, function(err, db) {
    if (err) throw err;
    var dbo = db.db("mydb");
    dbo.createCollection("customers", function(err, res) {
        if (err) throw err;
        console.log("Collection created!");
        db.close();
    });
});
```

Save as `"demo_mongodb_createcollection.js"` and run:

```bash
node demo_mongodb_createcollection.js
```

---

## **Node.js MongoDB Insert**
To insert a record (document) into a collection, use `insertOne()`.

The first parameter is an object containing the name(s) and value(s) of each field. It also takes a callback function for errors or the insertion result.

**Example:** Insert a document in the `"customers"` collection

```js
var MongoClient = require('mongodb').MongoClient;
var url = "mongodb://localhost:27017/";

MongoClient.connect(url, function(err, db) {
    if (err) throw err;
    var dbo = db.db("mydb");
    var myobj = { name: "Company Inc", address: "Highway 37" };
    dbo.collection("customers").insertOne(myobj, function(err, res) {
        if (err) throw err;
        console.log("1 document inserted");
        db.close();
    });
});
```

Save as `"demo_mongodb_insert.js"` and run:

```bash
node demo_mongodb_insert.js
```

---

## **Node.js MongoDB Find**
In MongoDB, use `find()` and `findOne()` to find data in a collection.

### **Find One**
The `findOne()` method returns the first occurrence in the selection.

**Example:** Find the first document in the customers collection

```js
var MongoClient = require('mongodb').MongoClient;
var url = "mongodb://localhost:27017/";

MongoClient.connect(url, function(err, db) {
    if (err) throw err;
    var dbo = db.db("mydb");
    dbo.collection("customers").findOne({}, function(err, result) {
        if (err) throw err;
        console.log(result.name);
        db.close();
    });
});
```

Save as `"demo_mongodb_findone.js"` and run:

```bash
node demo_mongodb_findone.js
```

### **Find All**
The `find()` method returns all occurrences. No parameters is like `SELECT *` in MySQL.

**Example:** Find all documents in the customers collection

```js
var MongoClient = require('mongodb').MongoClient;
var url = "mongodb://localhost:27017/";

MongoClient.connect(url, function(err, db) {
    if (err) throw err;
    var dbo = db.db("mydb");
    dbo.collection("customers").find({}).toArray(function(err, result) {
        if (err) throw err;
        console.log(result);
        db.close();
    });
});
```

Save as `"demo_mongodb_find.js"` and run:

```bash
node demo_mongodb_find.js
```

---

## **Node.js MongoDB Query**
### **Filter the Result**
Use a query object as the first argument of `find()` to limit the search.

**Example:** Find documents with address `"Park Lane 38"`

```js
var MongoClient = require('mongodb').MongoClient;
var url = "mongodb://localhost:27017/";

MongoClient.connect(url, function(err, db) {
    if (err) throw err;
    var dbo = db.db("mydb");
    var query = { address: "Park Lane 38" };
    dbo.collection("customers").find(query).toArray(function(err, result) {
        if (err) throw err;
        console.log(result);
        db.close();
    });
});
```

Save as `"demo_mongodb_query.js"` and run:

```bash
node demo_mongodb_query.js
```

### **Filter With Regular Expressions**
Regular expressions can only be used to query strings.

**Example:** Find documents where address starts with `"S"`

```js
var MongoClient = require('mongodb').MongoClient;
var url = "mongodb://localhost:27017/";

MongoClient.connect(url, function(err, db) {
    if (err) throw err;
    var dbo = db.db("mydb");
    var query = { address: /^S/ };
    dbo.collection("customers").find(query).toArray(function(err, result) {
        if (err) throw err;
        console.log(result);
        db.close();
    });
});
```

Save as `"demo_mongodb_query_s.js"` and run:

```bash
node demo_mongodb_query_s.js
```

---

## **Node.js MongoDB Sort**
Use `sort()` to sort results in ascending (`1`) or descending (`-1`) order.

**Example:** Sort alphabetically by name

```js
var MongoClient = require('mongodb').MongoClient;
var url = "mongodb://localhost:27017/";

MongoClient.connect(url, function(err, db) {
    if (err) throw err;
    var dbo = db.db("mydb");
    var mysort = { name: 1 };
    dbo.collection("customers").find().sort(mysort).toArray(function(err, result) {
        if (err) throw err;
        console.log(result);
        db.close();
    });
});
```

Save as `"demo_sort.js"` and run:

```bash
node demo_sort.js
```

---

## **Node.js MongoDB Delete**
### **Delete One Document**
Use `deleteOne()`. The first parameter is a query object. Only the first matching document is deleted.

**Example:** Delete document with address `"Mountain 21"`

```js
var MongoClient = require('mongodb').MongoClient;
var url = "mongodb://localhost:27017/";

MongoClient.connect(url, function(err, db) {
    if (err) throw err;
    var dbo = db.db("mydb");
    var myquery = { address: 'Mountain 21' };
    dbo.collection("customers").deleteOne(myquery, function(err, obj) {
        if (err) throw err;
        console.log("1 document deleted");
        db.close();
    });
});
```

Save as `"demo_delete.js"` and run:

```bash
node demo_delete.js
```

### **Delete Many Documents**
Use `deleteMany()` to delete multiple documents.

**Example:** Delete all documents where address starts with `"O"`

```js
var MongoClient = require('mongodb').MongoClient;
var url = "mongodb://localhost:27017/";

MongoClient.connect(url, function(err, db) {
    if (err) throw err;
    var dbo = db.db("mydb");
    var myquery = { address: /^O/ };
    dbo.collection("customers").deleteMany(myquery, function(err, obj) {
        if (err) throw err;
        console.log(obj.result.n + " document(s) deleted");
        db.close();
    });
});
```

Save as `"demo_delete_many.js"` and run:

```bash
node demo_delete_many.js
```

---

## **Node.js MongoDB Drop Collection**
Use `drop()` to delete a collection.

**Example:** Delete the `"customers"` collection

```js
var MongoClient = require('mongodb').MongoClient;
var url = "mongodb://localhost:27017/";

MongoClient.connect(url, function(err, db) {
    if (err) throw err;
    var dbo = db.db("mydb");
    dbo.collection("customers").drop(function(err, delOK) {
        if (err) throw err;
        if (delOK) console.log("Collection deleted");
        db.close();
    });
});
```

Save as `"demo_drop.js"` and run:

```bash
node demo_drop.js
```

---

## **Node.js MongoDB Update**
### **Update One Document**
Use `updateOne()`. First parameter is a query object, second is new values.

**Example:** Update document with address `"Valley 345"`

```js
var MongoClient = require('mongodb').MongoClient;
var url = "mongodb://127.0.0.1:27017/";

MongoClient.connect(url, function(err, db) {
    if (err) throw err;
    var dbo = db.db("mydb");
    var myquery = { address: "Valley 345" };
    var newvalues = { $set: { name: "Mickey", address: "Canyon 123" } };
    dbo.collection("customers").updateOne(myquery, newvalues, function(err, res) {
        if (err) throw err;
        console.log("1 document updated");
        db.close();
    });
});
```

Save as `"demo_update_one.js"` and run:

```bash
node demo_update_one.js
```

### **Update Only Specific Fields**
Using `$set` updates only specified fields.

**Example:** Update address from `"Valley 345"` to `"Canyon 123"`

```js
var MongoClient = require('mongodb').MongoClient;
var url = "mongodb://localhost:27017/";

MongoClient.connect(url, function(err, db) {
    if (err) throw err;
    var dbo = db.db("mydb");
    var myquery = { address: "Valley 345" };
    var newvalues = { $set: { address: "Canyon 123" } };
    dbo.collection("customers").updateOne(myquery, newvalues, function(err, res) {
        if (err) throw err;
        console.log("1 document updated");
        db.close();
    });
});
```

### **Update Many Documents**
Use `updateMany()` to update all matching documents.

**Example:** Update all documents where name starts with `"S"`

```js
var MongoClient = require('mongodb').MongoClient;
var url = "mongodb://127.0.0.1:27017/";

MongoClient.connect(url, function(err, db) {
    if (err) throw err;
    var dbo = db.db("mydb");
    var myquery = { address: /^S/ };
    var newvalues = { $set: { name: "Winnie" } };
    dbo.collection("customers").updateMany(myquery, newvalues, function(err, res) {
        if (err) throw err;
        console.log(res.result.nModified + " document(s) updated");
        db.close();
    });
});
```

Save as `"demo_update_many.js"` and run:

```bash
node demo_update_many.js
```

---

## **Node.js MongoDB Limit**
Use `limit()` to restrict the number of documents returned.

**Example:** Limit result to 5 documents

```js
var MongoClient = require('mongodb').MongoClient;
var url = "mongodb://localhost:27017/";

MongoClient.connect(url, function(err, db) {
    if (err) throw err;
    var dbo = db.db("mydb");
    dbo.collection("customers").find().limit(5).toArray(function(err, result) {
        if (err) throw err;
        console.log(result);
        db.close();
    });
});
```

Save as `"demo_mongodb_limit.js"` and run:

```bash
node demo_mongodb_limit.js
```

---

## **Node.js MongoDB Join**
MongoDB supports left outer join using the `$lookup` stage.

**Example collections:**

**orders**
```json
{ "_id": 1, "product_id": 154, "status": 1 }
```

**products**
```json
[
    { "_id": 154, "name": "Chocolate Heaven" },
    { "_id": 155, "name": "Tasty Lemons" },
    { "_id": 156, "name": "Vanilla Dreams" }
]
```

**Join example:**

```js
var MongoClient = require('mongodb').MongoClient;
var url = "mongodb://127.0.0.1:27017/";

MongoClient.connect(url, function(err, db) {
    if (err) throw err;
    var dbo = db.db("mydb");
    dbo.collection('orders').aggregate([
        { $lookup: {
            from: 'products',
            localField: 'product_id',
            foreignField: '_id',
            as: 'orderdetails'
        }}
    ]).toArray(function(err, res) {
        if (err) throw err;
        console.log(JSON.stringify(res));
        db.close();
    });
});
```

Save as `"demo_mongodb_join.js"` and run:

```bash
node demo_mongodb_join.js
```

**Result:**
```json
{
    "_id": 1,
    "product_id": 154,
    "status": 1,
    "orderdetails": [
        { "_id": 154, "name": "Chocolate Heaven" }
    ]
}
```

---

## **MongoDB Relationships using Mongoose**
Mongoose is a third-party package that builds upon the official MongoDB driver. It uses schemas to define data structure, making it easier to store and fetch data.

**Installation:**
```bash
npm install --save mongoose
```

### **Schema**
A description of the shape of data.

**Example:**
```js
const mongoose = require("mongoose");

const houseSchema = new mongoose.Schema({
    street: String,
    city: String,
    state: String,
    zip: String
});

const House = mongoose.model("House", houseSchema);

// Query for all houses
House.find({});
```

### **One-to-One Relationships**
One house has one owner. Data can be nested.

**Example:**
```js
const mongoose = require("mongoose");

const Owner = new mongoose.Schema({
    name: String
});

const houseSchema = new mongoose.Schema({
    street: String,
    city: String,
    state: String,
    zip: String,
    owner: Owner
});

const House = mongoose.model("House", houseSchema);

// Create a new house
House.create({
    street: "100 Maple Street",
    city: "Fort Townville",
    state: "New West Virgota",
    zip: "77777",
    owner: { name: "Alex Merced" }
});

// Query for all houses, includes nested owner info
House.find({});
```

### **One-to-Many Relationships**
One owner can have many houses. Use `ObjectId` and `populate()`.

**Example:**
```js
const mongoose = require("mongoose");

const ownerSchema = new mongoose.Schema({ name: String });
const Owner = mongoose.model("Owner", ownerSchema);

const houseSchema = new mongoose.Schema({
    street: String,
    city: String,
    state: String,
    zip: String,
    owner: { type: mongoose.Types.ObjectId, ref: "Owner" }
});

const House = mongoose.model("House", houseSchema);

// Create an Owner
const alex = await Owner.create({ name: "Alex Merced" });

// Create a new house
House.create({
    street: "180 Maple Street",
    city: "Fort Townville",
    state: "New West Virgota",
    zip: "77777",
    owner: alex
});

// Query for all houses, use populate to include owner info
House.find({}).populate("owner");
```

### **Many-to-Many Relationships**
Houses can have many owners, owners can have many houses. Use a junction collection.

**Example:**
```js
const mongoose = require("mongoose");

const ownerSchema = new mongoose.Schema({ name: String });
const Owner = mongoose.model("Owner", ownerSchema);

const houseSchema = new mongoose.Schema({
    street: String,
    city: String,
    state: String,
    zip: String
});
const House = mongoose.model("House", houseSchema);

const houseOwnerSchema = new mongoose.Schema({
    owner: { type: mongoose.Types.ObjectId, ref: "Owner" },
    house: { type: mongoose.Types.ObjectId, ref: "House" }
});
const HouseOwner = mongoose.model("HouseOwner", houseOwnerSchema);

// Create an Owner
const alex = await Owner.create({ name: "Alex Merced" });

// Create a House
const mapleStreet = await House.create({
    street: "180 Maple Street",
    city: "Fort Townville",
    state: "New West Virginia",
    zip: "77777"
});

// Create record that the owner owns the house
HouseOwner.create({ owner: alex, house: mapleStreet });

// Query for all houses owned by alex
HouseOwner.find({ owner: alex }).populate("house");

// Query for all owners of the Maple Street house
HouseOwner.find({ house: mapleStreet }).populate("owner");
```

---

**End of Notes**