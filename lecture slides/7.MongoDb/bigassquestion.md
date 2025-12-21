Here is your LaTeX document converted to Markdown (MD) format:

```markdown
# MongoDB Comprehensive Examination Question with Complete Solution

## Examination Question: E-commerce Database System

### Scenario
You are tasked with designing and implementing a MongoDB database for an e-commerce platform called "ShopEasy". The system must handle products, customers, orders, and reviews.

---

### Requirements

#### Part 1: Database Design
Design the database structure with the following collections and implement using both MongoDB shell and Node.js:

1. **Database**: Create a database named `shopeasy`.
2. **Collections**:
   - `products`: Store product information.
   - `customers`: Store customer information.
   - `orders`: Store order information with relationships.
   - `reviews`: Store product reviews.
3. **Sample Data**: Create realistic sample data for each collection.
4. **Relationships**: Implement appropriate relationships between collections.

---

#### Part 2: CRUD Operations
Implement the following operations using both MongoDB shell and Node.js:

1. Insert at least 5 documents in each collection.
2. Query products with price greater than $50.
3. Find customers from a specific city using regex.
4. Update product stock quantity when purchased.
5. Delete inactive customers (last login > 1 year).
6. Implement a soft delete system for orders.

---

#### Part 3: Advanced Operations
Implement these advanced operations:

1. Use aggregation to calculate total sales per product.
2. Implement `$lookup` to join orders with customer information.
3. Create capped collection for audit logs.
4. Add full-text search on product descriptions.
5. Implement pagination using `limit()` and `skip()`.

---

#### Part 4: Mongoose Implementation
Using Mongoose ODM:

1. Define schemas for all collections with proper data types.
2. Implement one-to-many relationship between customers and orders.
3. Implement many-to-many relationship between products and categories.
4. Add validation to all schemas.
5. Create middleware for automatic timestamping.

---

## Complete Solution

### Part 1: Database Design

#### MongoDB Shell: Database and Collection Setup
```javascript
// 1. Create and switch to database
use shopeasy

// 2. Create collections with options
db.createCollection("products", {
    validator: {
        $jsonSchema: {
            bsonType: "object",
            required: ["name", "price", "category"],
            properties: {
                name: { bsonType: "string" },
                price: { bsonType: "decimal" },
                category: { bsonType: "string" },
                stock: { bsonType: "int", minimum: 0 }
            }
        }
    }
})

// 3. Create capped collection for audit logs
db.createCollection("audit_logs", {
    capped: true,
    size: 1048576,  // 1MB
    max: 1000
})

// 4. Create indexes for better performance
db.products.createIndex({ name: "text", description: "text" })
db.products.createIndex({ category: 1, price: -1 })
db.customers.createIndex({ email: 1 }, { unique: true })
db.orders.createIndex({ customer_id: 1, order_date: -1 })
```

#### Node.js: Database Connection and Setup
```javascript
const { MongoClient } = require('mongodb');
const url = "mongodb://localhost:27017/";

async function setupDatabase() {
    const client = new MongoClient(url);

    try {
        await client.connect();
        const db = client.db("shopeasy");

        // Create collections
        await db.createCollection("products");
        await db.createCollection("customers");
        await db.createCollection("orders");
        await db.createCollection("reviews");
        await db.createCollection("audit_logs", {
            capped: true,
            size: 1048576,
            max: 1000
        });

        // Create indexes
        await db.collection("products").createIndex({ name: "text", description: "text" });
        await db.collection("customers").createIndex({ email: 1 }, { unique: true });
        await db.collection("orders").createIndex({ customer_id: 1, order_date: -1 });

        console.log("Database setup completed!");
    } finally {
        await client.close();
    }
}

setupDatabase().catch(console.error);
```

---

### Part 2: CRUD Operations

#### MongoDB Shell Operations
```javascript
// 1. Insert sample data
db.products.insertMany([
    {
        _id: 1,
        name: "Laptop Pro",
        description: "High-performance laptop",
        price: 1200.99,
        category: "Electronics",
        stock: 50,
        tags: ["laptop", "electronics", "computers"]
    },
    {
        _id: 2,
        name: "Wireless Mouse",
        description: "Ergonomic wireless mouse",
        price: 29.99,
        category: "Electronics",
        stock: 200,
        tags: ["mouse", "accessories"]
    },
    {
        _id: 3,
        name: "Coffee Maker",
        description: "Automatic coffee machine",
        price: 89.99,
        category: "Home Appliances",
        stock: 75,
        tags: ["coffee", "appliances", "kitchen"]
    },
    {
        _id: 4,
        name: "Desk Chair",
        description: "Ergonomic office chair",
        price: 249.99,
        category: "Furniture",
        stock: 30,
        tags: ["furniture", "office", "chair"]
    },
    {
        _id: 5,
        name: "Smartphone X",
        description: "Latest smartphone model",
        price: 999.99,
        category: "Electronics",
        stock: 100,
        tags: ["phone", "mobile", "electronics"]
    }
]);

// 2. Query products with price > $50
db.products.find({ price: { $gt: 50 } }).pretty();

// 3. Find customers from cities starting with "San"
db.customers.find({ "address.city": /^San/ }).pretty();

// 4. Update product stock (using $inc operator)
db.products.updateOne(
    { _id: 1 },
    { $inc: { stock: -1 } }
);

// 5. Delete inactive customers (last login > 1 year ago)
const oneYearAgo = new Date();
oneYearAgo.setFullYear(oneYearAgo.getFullYear() - 1);

db.customers.deleteMany({
    last_login: { $lt: oneYearAgo }
});

// 6. Soft delete for orders (using status field)
db.orders.updateOne(
    { _id: "ORD001" },
    { $set: { status: "cancelled", cancelled_at: new Date() } }
);
```

#### Node.js CRUD Operations
```javascript
const { MongoClient, ObjectId } = require('mongodb');
const url = "mongodb://localhost:27017/";

class ECommerceDB {
    constructor() {
        this.client = new MongoClient(url);
        this.db = null;
    }

    async connect() {
        await this.client.connect();
        this.db = this.client.db("shopeasy");
    }

    async insertProduct(product) {
        return await this.db.collection("products").insertOne(product);
    }

    async findExpensiveProducts(minPrice) {
        return await this.db.collection("products")
            .find({ price: { $gt: minPrice } })
            .sort({ price: -1 })
            .toArray();
    }

    async searchCustomersByCity(cityPattern) {
        const query = { "address.city": new RegExp(cityPattern, 'i') };
        return await this.db.collection("customers")
            .find(query)
            .toArray();
    }

    async updateStock(productId, quantityChange) {
        return await this.db.collection("products").updateOne(
            { _id: productId },
            { $inc: { stock: quantityChange } }
        );
    }

    async deleteInactiveCustomers() {
        const oneYearAgo = new Date();
        oneYearAgo.setFullYear(oneYearAgo.getFullYear() - 1);

        return await this.db.collection("customers").deleteMany({
            last_login: { $lt: oneYearAgo }
        });
    }

    async close() {
        await this.client.close();
    }
}

// Usage example
async function runOperations() {
    const db = new ECommerceDB();

    try {
        await db.connect();

        // Insert products
        await db.insertProduct({
            name: "Tablet",
            price: 299.99,
            category: "Electronics",
            stock: 25
        });

        // Find expensive products
        const expensiveProducts = await db.findExpensiveProducts(100);
        console.log("Expensive products:", expensiveProducts);

        // Update stock
        await db.updateStock(1, -5);

    } finally {
        await db.close();
    }
}

runOperations().catch(console.error);
```

---

### Part 3: Advanced Operations

#### Advanced MongoDB Operations
```javascript
// 1. Aggregation: Calculate total sales per product
db.orders.aggregate([
    { $unwind: "$items" },
    {
        $group: {
            _id: "$items.product_id",
            totalQuantity: { $sum: "$items.quantity" },
            totalRevenue: {
                $sum: {
                    $multiply: ["$items.quantity", "$items.price"]
                }
            }
        }
    },
    {
        $lookup: {
            from: "products",
            localField: "_id",
            foreignField: "_id",
            as: "product_info"
        }
    },
    { $sort: { totalRevenue: -1 } }
]);

// 2. Join orders with customer information
db.orders.aggregate([
    {
        $lookup: {
            from: "customers",
            localField: "customer_id",
            foreignField: "_id",
            as: "customer_details"
        }
    },
    {
        $lookup: {
            from: "products",
            localField: "items.product_id",
            foreignField: "_id",
            as: "product_details"
        }
    },
    { $unwind: "$customer_details" }
]);

// 3. Full-text search on products
db.products.find({
    $text: { $search: "laptop performance" }
}, {
    score: { $meta: "textScore" }
}).sort({
    score: { $meta: "textScore" }
});

// 4. Pagination with limit and skip
const page = 2;
const pageSize = 10;
const skipCount = (page - 1) * pageSize;

db.products.find()
    .sort({ price: -1 })
    .skip(skipCount)
    .limit(pageSize);

// 5. Complex query with multiple conditions
db.orders.find({
    $and: [
        { order_date: { $gte: new Date("2024-01-01") } },
        { order_date: { $lt: new Date("2024-02-01") } },
        { status: "completed" },
        { "items.quantity": { $gt: 2 } }
    ]
});
```

---

### Part 4: Mongoose Implementation

#### Mongoose Schemas and Relationships
```javascript
const mongoose = require('mongoose');
const Schema = mongoose.Schema;

// Connect to MongoDB
mongoose.connect('mongodb://localhost:27017/shopeasy', {
    useNewUrlParser: true,
    useUnifiedTopology: true
});

// 1. Product Schema with validation
const productSchema = new Schema({
    name: {
        type: String,
        required: [true, 'Product name is required'],
        trim: true,
        maxlength: [100, 'Name cannot exceed 100 characters']
    },
    description: {
        type: String,
        required: true
    },
    price: {
        type: Number,
        required: true,
        min: [0, 'Price must be positive']
    },
    category: {
        type: String,
        required: true,
        enum: ['Electronics', 'Clothing', 'Books', 'Home', 'Other']
    },
    stock: {
        type: Number,
        default: 0,
        min: 0
    },
    tags: [String],
    isActive: {
        type: Boolean,
        default: true
    },
    createdAt: {
        type: Date,
        default: Date.now
    },
    updatedAt: {
        type: Date,
        default: Date.now
    }
}, {
    timestamps: true  // Automatically manage createdAt and updatedAt
});

// Indexes
productSchema.index({ name: 'text', description: 'text' });
productSchema.index({ category: 1, price: -1 });

// Middleware for automatic timestamp updates
productSchema.pre('save', function(next) {
    this.updatedAt = Date.now();
    next();
});

const Product = mongoose.model('Product', productSchema);

// 2. Customer Schema
const customerSchema = new Schema({
    name: {
        type: String,
        required: true
    },
    email: {
        type: String,
        required: true,
        unique: true,
        lowercase: true,
        match: [/^\S+@\S+\.\S+$/, 'Please enter a valid email']
    },
    address: {
        street: String,
        city: String,
        state: String,
        zip: String,
        country: {
            type: String,
            default: 'USA'
        }
    },
    phone: String,
    lastLogin: Date,
    preferences: {
        newsletter: {
            type: Boolean,
            default: true
        },
        theme: {
            type: String,
            default: 'light'
        }
    }
});

const Customer = mongoose.model('Customer', customerSchema);

// 3. Order Schema with one-to-many relationship
const orderItemSchema = new Schema({
    product: {
        type: Schema.Types.ObjectId,
        ref: 'Product',
        required: true
    },
    quantity: {
        type: Number,
        required: true,
        min: 1
    },
    price: {
        type: Number,
        required: true
    }
});

const orderSchema = new Schema({
    orderNumber: {
        type: String,
        unique: true,
        required: true
    },
    customer: {
        type: Schema.Types.ObjectId,
        ref: 'Customer',
        required: true
    },
    items: [orderItemSchema],
    totalAmount: {
        type: Number,
        required: true
    },
    status: {
        type: String,
        enum: ['pending', 'processing', 'shipped', 'delivered', 'cancelled'],
        default: 'pending'
    },
    shippingAddress: {
        type: Object,
        required: true
    },
    paymentMethod: String,
    notes: String
}, {
    timestamps: true
});

// Virtual for formatted order date
orderSchema.virtual('formattedDate').get(function() {
    return this.createdAt.toLocaleDateString('en-US', {
        year: 'numeric',
        month: 'long',
        day: 'numeric'
    });
});

const Order = mongoose.model('Order', orderSchema);

// 4. Review Schema with relationships
const reviewSchema = new Schema({
    product: {
        type: Schema.Types.ObjectId,
        ref: 'Product',
        required: true
    },
    customer: {
        type: Schema.Types.ObjectId,
        ref: 'Customer',
        required: true
    },
    rating: {
        type: Number,
        required: true,
        min: 1,
        max: 5
    },
    title: String,
    comment: String,
    helpful: {
        type: Number,
        default: 0
    },
    verifiedPurchase: {
        type: Boolean,
        default: false
    }
}, {
    timestamps: true
});

reviewSchema.index({ product: 1, rating: -1 });
reviewSchema.index({ customer: 1, createdAt: -1 });

const Review = mongoose.model('Review', reviewSchema);

// 5. Category Schema for many-to-many relationship
const categorySchema = new Schema({
    name: {
        type: String,
        required: true,
        unique: true
    },
    description: String,
    parentCategory: {
        type: Schema.Types.ObjectId,
        ref: 'Category'
    },
    isActive: {
        type: Boolean,
        default: true
    }
});

const Category = mongoose.model('Category', categorySchema);

// Many-to-many relationship between products and categories
productSchema.add({
    categories: [{
        type: Schema.Types.ObjectId,
        ref: 'Category'
    }]
});

// 6. Usage examples with relationships
async function createOrder() {
    const customer = await Customer.findOne({ email: 'john@example.com' });
    const product = await Product.findOne({ name: 'Laptop Pro' });

    const order = new Order({
        orderNumber: 'ORD' + Date.now(),
        customer: customer._id,
        items: [{
            product: product._id,
            quantity: 1,
            price: product.price
        }],
        totalAmount: product.price,
        shippingAddress: customer.address,
        paymentMethod: 'credit_card'
    });

    await order.save();

    // Update product stock
    product.stock -= 1;
    await product.save();
}

// 7. Query with population (joins)
async function getOrderWithDetails(orderId) {
    return await Order.findById(orderId)
        .populate('customer')
        .populate({
            path: 'items.product',
            select: 'name price category'
        });
}

// 8. Complex aggregation with Mongoose
async function getSalesReport(startDate, endDate) {
    return await Order.aggregate([
        {
            $match: {
                createdAt: { $gte: startDate, $lte: endDate },
                status: { $ne: 'cancelled' }
            }
        },
        { $unwind: '$items' },
        {
            $lookup: {
                from: 'products',
                localField: 'items.product',
                foreignField: '_id',
                as: 'productDetails'
            }
        },
        { $unwind: '$productDetails' },
        {
            $group: {
                _id: '$productDetails.category',
                totalSales: { $sum: '$items.quantity' },
                totalRevenue: { $sum: { $multiply: ['$items.quantity', '$items.price'] } },
                averageOrderValue: { $avg: '$totalAmount' }
            }
        },
        { $sort: { totalRevenue: -1 } }
    ]);
}

// 9. Text search with Mongoose
async function searchProducts(searchTerm) {
    return await Product.find(
        { $text: { $search: searchTerm } },
        { score: { $meta: 'textScore' } }
    ).sort({ score: { $meta: 'textScore' } });
}

module.exports = {
    Product,
    Customer,
    Order,
    Review,
    Category,
    createOrder,
    getOrderWithDetails,
    getSalesReport,
    searchProducts
};
```

---

### Testing and Validation

#### Test Script for All Operations
```javascript
const { MongoClient } = require('mongodb');
const url = "mongodb://localhost:27017/";

async function testAllOperations() {
    const client = new MongoClient(url);

    try {
        await client.connect();
        const db = client.db("shopeasy");

        console.log("=== Testing All MongoDB Operations ===\n");

        // Test 1: Insert operations
        console.log("1. Testing Insert Operations:");
        const insertResult = await db.collection("test_products").insertOne({
            name: "Test Product",
            price: 99.99,
            category: "Test"
        });
        console.log(`   Inserted ID: ${insertResult.insertedId}\n`);

        // Test 2: Find operations
        console.log("2. Testing Find Operations:");
        const expensiveProducts = await db.collection("products")
            .find({ price: { $gt: 50 } })
            .toArray();
        console.log(`   Found ${expensiveProducts.length} expensive products\n`);

        // Test 3: Update operations
        console.log("3. Testing Update Operations:");
        const updateResult = await db.collection("products").updateOne(
            { _id: 1 },
            { $set: { updated: true }, $inc: { stock: -1 } }
        );
        console.log(`   Updated ${updateResult.modifiedCount} document(s)\n`);

        // Test 4: Delete operations
        console.log("4. Testing Delete Operations:");
        const deleteResult = await db.collection("test_products").deleteOne({ _id: insertResult.insertedId });
        console.log(`   Deleted ${deleteResult.deletedCount} document(s)\n`);

        // Test 5: Aggregation
        console.log("5. Testing Aggregation:");
        const aggResult = await db.collection("orders").aggregate([
            { $group: { _id: "$status", count: { $sum: 1 } } }
        ]).toArray();
        console.log(`   Aggregation result:`, aggResult, '\n');

        // Test 6: Lookup (Join)
        console.log("6. Testing Lookup Operation:");
        const joinResult = await db.collection("orders").aggregate([
            {
                $lookup: {
                    from: "customers",
                    localField: "customer_id",
                    foreignField: "_id",
                    as: "customer_info"
                }
            },
            { $limit: 1 }
        ]).toArray();
        console.log(`   Join successful: ${joinResult.length > 0}\n`);

        // Test 7: Index operations
        console.log("7. Testing Index Operations:");
        const indexes = await db.collection("products").indexes();
        console.log(`   Collection has ${indexes.length} indexes\n`);

        console.log("=== All Tests Completed Successfully ===");

    } catch (error) {
        console.error("Test failed:", error);
    } finally {
        await client.close();
    }
}

// Run tests
testAllOperations();
```

---

### Summary of Concepts Covered


MongoDB Concepts Covered in the Solution


| Concept                | Covered in Solution                                                                 |
|------------------------|------------------------------------------------------------------------------------|
| Database Creation      | `use shopeasy`, Node.js connection                                                 |
| Collection Operations  | `createCollection()`, `drop()`, capped collections                                 |
| Document CRUD          | `insert()`, `find()`, `update()`, `remove()`                                       |
| Query Operations       | Comparison operators, regex, sorting, limiting                                    |
| Aggregation            | `$group`, `$unwind`, `$match`, `$sort`                                             |
| Joins                  | `$lookup` for left outer joins                                                     |
| Indexing               | Single field, compound, text, unique indexes                                       |
| Data Modeling          | Embedded documents, references, relationships                                     |
| Mongoose ODM           | Schemas, models, validation, middleware                                           |
| Relationships          | One-to-one, one-to-many, many-to-many                                             |
| Advanced Features      | Text search, geospatial, transactions                                              |
| Performance            | Indexing, query optimization, pagination                                          |
| Error Handling         | Try-catch, validation, error patterns                                             |

---

**Total Solution Lines of Code:** Approximately 500+ lines
**Concepts Covered:** 100% of topics from both provided documents
```