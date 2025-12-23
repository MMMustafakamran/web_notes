# **React Lecture Notes (Lectures 3 & 4)**

---

## **LECTURE 3: Intro to Forms, React App Setup, Components & Props**

### **1. Introduction to Forms in React**

- Forms in React are handled using **state** and **event handlers**.
- By default, form submission refreshes the page. We prevent this using `e.preventDefault()`.

#### Example: Basic Form with State

```jsx
class App extends React.Component {
  state = {
    name: "Ryu",
    age: 30,
  };

  handleChange = (e) => {
    this.setState({
      name: e.target.value,
    });
  };

  handleSubmit = (e) => {
    e.preventDefault();
    console.log("form submitted", this.state.name);
  };

  render() {
    return (
      <div className="app-content">
        <h1>My name is {this.state.name}</h1>
        <form onSubmit={this.handleSubmit}>
          <input type="text" onChange={this.handleChange} />
          <button>Submit</button>
        </form>
      </div>
    );
  }
}
```

- `onChange` updates state as the user types.
- `onSubmit` prevents page refresh and logs the submitted value.

---

### **2. Create React App**

- **Create React App** is a CLI tool to bootstrap React projects.
- It includes a development server, ES6+ support, modular code structure, and build tools.

#### Commands:

```bash
npx create-react-app my-app
cd my-app
npm start
```

- App runs on `http://localhost:3000`.
- Production build: `npm run build`.

#### Project Structure:

```
my-app/
├── node_modules
├── public/
│   ├── index.html
│   └── favicon.ico
├── src/
│   ├── App.js
│   ├── index.js
│   └── index.css
├── package.json
└── README.md
```

- `index.html` contains a root `<div id="root">` where the React app is injected.
- `App.js` is the main component.
- `index.js` renders `App` into the DOM.

#### Cleaning Up the Template:

- Remove logo imports and extra CSS.
- Simplify `App.js` to basic JSX.

```jsx
import React, { Component } from "react";

class App extends Component {
  render() {
    return (
      <div className="App">
        <h1>My first React app!</h1>
        <p>Welcome :)</p>
      </div>
    );
  }
}

export default App;
```

---

### **3. Single Page Apps (SPA) vs Multi-Page Apps**

- **React apps are SPAs**:
  - Only one HTML page (`index.html`) is served.
  - React dynamically updates the content based on routes/components.
- **Multi-Page Apps**:
  - Each page is a separate HTML file (e.g., `index.html`, `contact.html`).
- In SPAs, navigation changes the component view without reloading the page.

---

### **4. Nesting Components**

- Components can be nested inside the root `App` component.
- Example: Creating a `Ninjas` component.

#### `Ninjas.js`:

```jsx
import React, { Component } from "react";

class Ninjas extends Component {
  render() {
    return (
      <div className="ninja">
        <div>Name: Ryu</div>
        <div>Age: 30</div>
        <div>Belt: Black</div>
      </div>
    );
  }
}

export default Ninjas;
```

#### `App.js` (using Ninjas):

```jsx
import React, { Component } from "react";
import Ninjas from "./Ninjas";

class App extends Component {
  render() {
    return (
      <div className="App">
        <h1>My first React app!</h1>
        <p>Welcome :)</p>
        <Ninjas />
      </div>
    );
  }
}
```

---

### **5. Props: Passing Data to Components**

- **Props** pass data from parent to child components.
- Props are read-only in the child.

#### Passing Props from `App` to `Ninjas`:

```jsx
// App.js
<Ninjas name="Ryu" age={30} belt="Black" />;

// Ninjas.js
class Ninjas extends Component {
  render() {
    return (
      <div className="ninja">
        <div>Name: {this.props.name}</div>
        <div>Age: {this.props.age}</div>
        <div>Belt: {this.props.belt}</div>
      </div>
    );
  }
}
```

#### Destructuring Props:

```jsx
const { name, age, belt } = this.props;
```

---

### **6. Outputting Lists with `map()`**

- Use `map()` to render lists of data.
- Each list item must have a unique `key` prop.

#### Example with Array in State:

```jsx
// App.js state
state = {
  ninjas: [
    { name: "Ryu", age: 30, belt: "black", id: 1 },
    { name: "Yoshi", age: 20, belt: "green", id: 2 },
    { name: "Crystal", age: 25, belt: "pink", id: 3 },
  ],
};

// Pass to Ninjas
<Ninjas ninjas={this.state.ninjas} />;

// Ninjas.js
const ninjaList = ninjas.map((ninja) => {
  return (
    <div className="ninja" key={ninja.id}>
      <div>Name: {ninja.name}</div>
      <div>Age: {ninja.age}</div>
      <div>Belt: {ninja.belt}</div>
    </div>
  );
});

return <div className="ninja-list">{ninjaList}</div>;
```

---

### **7. Stateless (Functional) vs Stateful (Class) Components**

- **Container/Stateful Components**:
  - Have state and lifecycle methods.
  - Usually class-based.
  - Manage data and logic.
- **UI/Stateless Components**:
  - No state, only receive props.
  - Usually functional.
  - Focus on presentation.

#### Converting Ninjas to a Stateless Component:

```jsx
import React from "react";

const Ninjas = (props) => {
  const { ninjas } = props;
  const ninjaList = ninjas.map((ninja) => (
    <div className="ninja" key={ninja.id}>
      <div>Name: {ninja.name}</div>
      <div>Age: {ninja.age}</div>
      <div>Belt: {ninja.belt}</div>
    </div>
  ));

  return <div className="ninja-list">{ninjaList}</div>;
};

export default Ninjas;
```

---

## **LECTURE 4: Conditional Output, Forms Revisited, Functions as Props**

### **1. Conditional Output**

- Conditionally render JSX based on state or props.
- Use `if` statements or ternary operators inside `map()`.

#### Example: Only Show Ninjas Over Age 20

```jsx
const ninjaList = ninjas.map((ninja) => {
  if (ninja.age > 20) {
    return (
      <div className="ninja" key={ninja.id}>
        <div>Name: {ninja.name}</div>
        <div>Age: {ninja.age}</div>
        <div>Belt: {ninja.belt}</div>
      </div>
    );
  } else {
    return null;
  }
});
```

#### Using Ternary Operator:

```jsx
const ninjaList = ninjas.map((ninja) =>
  ninja.age > 20 ? (
    <div className="ninja" key={ninja.id}>
      <div>Name: {ninja.name}</div>
      <div>Age: {ninja.age}</div>
      <div>Belt: {ninja.belt}</div>
    </div>
  ) : null
);
```

---

### **2. Forms Revisited – Adding New Data**

- Goal: Create a form to add a new ninja to the list.
- Steps:
  1. Create an `AddNinja` component.
  2. Store form inputs in local state.
  3. On submit, pass new ninja to parent (`App`) via props.

#### `AddNinja.js` (Class Component):

```jsx
import React, { Component } from "react";

class AddNinja extends Component {
  state = {
    name: null,
    age: null,
    belt: null,
  };

  handleChange = (e) => {
    this.setState({
      [e.target.id]: e.target.value,
    });
  };

  handleSubmit = (e) => {
    e.preventDefault();
    this.props.addNinja(this.state);
  };

  render() {
    return (
      <div>
        <form onSubmit={this.handleSubmit}>
          <label htmlFor="name">Name:</label>
          <input type="text" id="name" onChange={this.handleChange} />
          <label htmlFor="age">Age:</label>
          <input type="text" id="age" onChange={this.handleChange} />
          <label htmlFor="belt">Belt:</label>
          <input type="text" id="belt" onChange={this.handleChange} />
          <button>Submit</button>
        </form>
      </div>
    );
  }
}
```

---

### **3. Functions as Props**

- Pass a function from parent to child as a prop.
- Child calls the function to update parent’s state.

#### In `App.js`:

```jsx
addNinja = (ninja) => {
  ninja.id = Math.random();
  let newNinjas = [...this.state.ninjas, ninja];
  this.setState({
    ninjas: newNinjas,
  });
};

// In render
<AddNinja addNinja={this.addNinja} />;
```

- **Important**: Never mutate state directly. Use `setState`.

#### Spread Operator Review:

```js
const numbers = [1, 2, 3, 4];
const newNumbers = [...numbers, 5]; // [1, 2, 3, 4, 5]
```

---

### **4. Full Example: Adding and Displaying Ninjas**

#### `App.js`:

```jsx
import React, { Component } from "react";
import Ninjas from "./Ninjas";
import AddNinja from "./AddNinja";

class App extends Component {
  state = {
    ninjas: [
      { name: "Ryu", age: 30, belt: "black", id: 1 },
      { name: "Yoshi", age: 20, belt: "green", id: 2 },
      { name: "Crystal", age: 25, belt: "pink", id: 3 },
    ],
  };

  addNinja = (ninja) => {
    ninja.id = Math.random();
    let newNinjas = [...this.state.ninjas, ninja];
    this.setState({
      ninjas: newNinjas,
    });
  };

  render() {
    return (
      <div className="App">
        <h1>My first React app!</h1>
        <p>Welcome :)</p>
        <Ninjas ninjas={this.state.ninjas} />
        <AddNinja addNinja={this.addNinja} />
      </div>
    );
  }
}
```

---

### **5. Next Step: Delete Functionality**

- Suggested exercise: Add a “Delete Ninja” feature.
- Pass a `deleteNinja` function as props to `Ninjas` component.
- Use `filter()` to remove ninja from state.

---

## **Key Takeaways**

- **Forms**: Controlled components via state and `onChange`.
- **SPA**: Single HTML page, dynamic content.
- **Components**: Can be class-based (stateful) or functional (stateless).
- **Props**: Pass data and functions from parent to child.
- **Lists**: Use `map()` and provide `key`.
- **State Update**: Never mutate directly; use `setState` and spread operator.
- **Conditional Rendering**: Use `if` or ternary inside JSX.

---

**End of Notes – All code examples and explanations from slides are included.**
