# React

## 1. Introduction & Setup

### What is React?

- **Core Feature**: The **Virtual DOM**, copy of real dom , updates only changes made to the real dom.

### Setup Methods

#### A. CDN Scripts (For Quick Prototypes)

You can include React and Babel (for JSX transformation) directly in your HTML(between script tag add source and link).

#### B. Create React App (Professional Setup)

```bash
npx create-react-app my-app
cd my-app
npm start
```

## 2. Components & JSX

Everything in React is a component (e.g.Footer). They are reusable bricks of UI.

### JSX (JavaScript XML)

almost html but in live in javascript.

- **Rule 1**: Only ONE root element (use `<div>` or `<> Fragments`).
- **Rule 2**: Use `className` instead of `class`.
- **Rule 3**: JavaScript expressions go inside curly braces `{}`.

```jsx
const Welcome = ({ name }) => {
  return (
    <div className="welcome-box">
      <h1>Hello, {name}!</h1>
      <p>Current Luck: {Math.random()}</p>
    </div>
  );
}; //name=prop)
```

## 3. State & Event Handling

### Component State

its obj that hold data that may change over time. if changes =compon rerenders.

### Handling Events

Events=camelCased (`onClick`, `onChange`).In Class Components, use arrow functions to solve the `this` context problem.

#### Code : Counter with State (Class Component)

```jsx
class Counter extends React.Component {
  state = { count: 0 };

  // Arrowfunc keep correct `this` context
  handleIncrement = () => {
    this.setState({ count: this.state.count + 1 });
  };

  render() {
    return (
      <div>
        {/* Display current count from state */}
        <p>You clicked {this.state.count} times</p>

        {/* camelCased event handler */}
        <button onClick={this.handleIncrement}>Increment</button>
      </div>
    );
  }
}
```

---

## 4. Props & Data Flow

### Passing Props

to pass data from a Parent component to a Child component. They are read-only.

### Functions as Props

You can pass a function from a parent to a child so the child can trigger a state change in the parent.

```jsx
// Child func gets props
const GreetChild = ({ name, sayHello }) => (
  <button onClick={() => sayHello(name)}>Greet {name}</button>
);

// Parent
class App extends React.Component {
  greet = (name) => alert(`Hello ${name}`);
  render() {
    return <GreetChild name="Ryu" sayHello={this.greet} />;
  }
}
```

---

## 5. Working with Lists & Conditions

### Outputting Lists

Use the `.map()` function to render arrays. Every item must have a unique `key`.

### Conditional Rendering

Use ternary operators (`condition ? true : false`) or logical `&&` for conditional output.

#### Code Example: List of Ninjas

```jsx
const NinjaList = ({ ninjas }) => {
  return (
    <div className="list">
      {ninjas.map((ninja) =>
        ninja.age > 20 ? (
          <div key={ninja.id}>
            {ninja.name} ({ninja.age})
          </div>
        ) : null
      )}
    </div>
  );
};
```

---

## 6. Forms & Controlled Components

In React, form data is usually handled by the state, making the component "controlled."

#### Code Example: Controlled Input

```jsx
class AddNinja extends React.Component {
  state = { name: "" };

  handleChange = (e) => {
    this.setState({ name: e.target.value });
  };

  handleSubmit = (e) => {
    e.preventDefault();
    console.log("Submitting:", this.state.name);
  };

  render() {
    return (
      <form onSubmit={this.handleSubmit}>
        <input
          type="text"
          onChange={this.handleChange}
          value={this.state.name}
        />
        <button>Submit</button>
      </form>
    );
  }
}
```

---

## 7. React Router

React Router allows navigation without page refreshes.

- `<BrowserRouter>`: Wraps the app.
- `<Route>`: Defines paths.
- `<Link>` / `<NavLink>`: Navigates without reload.
- `props.history.push('/')`: Programmatic redirect.

#### Code Example: Basic Router Setup

```jsx
import { BrowserRouter, Route, Link, Switch } from "react-router-dom";

const App = () => (
  <BrowserRouter>
    <nav>
      <Link to="/">Home</Link>
      <Link to="/about">About</Link>
    </nav>
    <Switch>
      <Route exact path="/" component={Home} />
      <Route path="/about" component={About} />
      <Route path="/post/:id" component={PostDetails} />
    </Switch>
  </BrowserRouter>
);
```

---

## 8. Higher-Order Components (HOCs)

An HOC is a function that takes a component and returns a new component with added logic (e.g., authentication, loading states).

#### Code Example: withLoading HOC

```jsx
const withLoading = (WrappedComponent) => {
  return ({ isLoading, ...props }) => {
    return isLoading ? <h2>Loading...</h2> : <WrappedComponent {...props} />;
  };
};

const UserListWithLoading = withLoading(UserList);
```

---

## 9. External Data (Axios) & Lifecycle

Use `componentDidMount` (in classes) or `useEffect` (in functions) to fetch data from APIs using **Axios**.

#### Code Example: Fetching Data

```jsx
import axios from "axios";

class Home extends React.Component {
  state = { posts: [] };

  componentDidMount() {
    axios
      .get("https://jsonplaceholder.typicode.com/posts")
      .then((res) => this.setState({ posts: res.data.slice(0, 5) }));
  }

  render() {
    return (
      <div>
        {this.state.posts.map((post) => (
          <p key={post.id}>{post.title}</p>
        ))}
      </div>
    );
  }
}
```

---

## 10. Tools

- **React Developer Tools**: Chrome extension to inspect component hierarchy, props, and state.

---

**End of Combined Notes**
