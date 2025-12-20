# Chapter: React - Modern Front-end Development

React is a powerful JavaScript library for building user interfaces, developed by Facebook. It focuses on reusable components and efficient rendering via the Virtual DOM.

---

## 1. Core Concepts
### React vs React Native
- **React**: For web applications (Single Page Apps).
- **React Native**: For mobile application development (Android/iOS).

### The Virtual DOM
React creates an in-memory database cache (Virtual DOM) that tracks changes. When the UI changes, React compares the Virtual DOM to the real DOM and updates only the necessary parts, leading to better performance.

### JSX (JavaScript XML)
A syntax extension that looks like HTML but lives in JavaScript.
- Must have a single root element.
- Use `className` instead of `class`.
- Use `htmlFor` instead of `for` for labels.

---

## 2. Components
Components are the building blocks of a React app.
- **Functional Components (Stateless)**: Simple functions that return JSX.
- **Class Components (Container)**: Use ES6 classes and have access to `this`, `state`, and lifecycle methods.

---

## 3. State and Props
### State
An internal data store for a component. When state changes, the component re-renders.
- Always use `this.setState()` in class components to update state.
- In functional components, use the `useState` hook.

### Props (Properties)
Data passed from a parent component to a child component. Props are read-only for the child.

---

## 4. Handling Events
- React events are named using camelCase (e.g., `onClick`, `onSubmit`).
- **`this` Context**: In class components, `this` is lost in custom functions. Solutions:
  - Bind in constructor: `this.myFunc = this.myFunc.bind(this)`.
  - Use **Arrow Functions**: `myFunc = () => { ... }`.

---

## 5. Forms and Interactivity
- **Controlled Components**: Input values are driven by state.
- **`e.preventDefault()`**: Used in form submission to stop the default page refresh.
- **Functions as Props**: Passing a function from parent to child allows the child to communicate back to the parent (e.g., deleting an item from a list held in parent state).

---

## 6. Development Tools and Setup
- **React Dev Tools**: Browser extension for inspecting component hierarchies and state/props.
- **Create React App (CRA)**: A standard toolchain for setting up a modern React project.
  - `npx create-react-app my-app`
  - `npm start`: Runs the app in development mode.

---

## 7. React Router
Used to handle navigation in a Single Page App without refreshing the page.
- **`<BrowserRouter>`**: Wraps the whole app.
- **`<Route>`**: Defines a path and the component to render.
- **`<Link>` and `<NavLink>`**: Replace `<a>` tags for internal navigation.
- **Route Parameters**: `path="/post/:id"`.

---

## 8. Advanced Topics
### Higher-Order Components (HOCs)
A function that takes a component and returns a new ("enhanced") component. Used for shared logic like authentication or loading states.
```javascript
const Protected = withAuth(Dashboard);
```

### Hooks (ES6+)
- **`useState`**: Adds state to functional components.
- **`useEffect`**: Handles side effects (like data fetching). Replaces lifecycle methods like `componentDidMount`.

### Data Fetching (Axios)
Axios is a popular library to fetch data from APIs.
```javascript
useEffect(() => {
  axios.get('https://api.example.com/posts')
    .then(res => setPosts(res.data));
}, []);
```

---

## Visual Aids from Slides
*(Refer to extracted images for Virtual DOM diagrams and component life cycles)*

![Virtual DOM Concept](Lec1_images/page_14_img_1.png)
![Component Nesting](Lec3_images/page_53_img_1.png)
![React Router](Lec5_images/page_7_img_1.jpeg)
