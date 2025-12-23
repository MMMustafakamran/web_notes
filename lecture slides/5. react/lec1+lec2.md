# React & React Native Study Notes

## Introduction to React vs React Native

**React Native** uses React to create mobile apps for Android & iOS. It’s a great choice for developers already familiar with React for web.

**React** (or ReactJS) is an open-source JavaScript library used to develop single-page web applications. It’s one of the most popular libraries for building UI for web and mobile apps. It was developed and backed by Facebook in 2011 and has gained popularity since then.

React uses the **Virtual DOM** to create amazing UX, while React Native leverages APIs to render UI components that can be used again for both Android and iOS platforms.

## Core Concepts and Requirements

### React Native also uses:

- Core components of React: Functional Components, States, Props
- React Hooks and Context
- JavaScript Basic Fundamentals: objects, arrays, error functions, callbacks

> **Note:** Without JavaScript knowledge, React Native is not a good place to start.

## What is React?

- JavaScript library created by Facebook
- Also used by Netflix & Instagram
- Used to create JS-driven dynamic web apps
- Can be compared to Angular & Vue

## What is Redux?

- A layer on-top of React
- Helps with state management of our app
  - Data in the app
  - UI state of the app

**State management means:**  
Is pop up open or closed?  
Is menu open or closed?

## Key React Topics

- React basics: components, events, templates, props & forms
- React Router: routes, route parameters, redirects
- Redux: stores, actions & reducers

## Components in React

- Components, components, COMPONENTS!
- Examples: NAVBAR, SEARCH BOX, FOOTER

## The Virtual DOM

- The Virtual DOM makes React fast
- It allows efficient updates and rendering

## Components & Templates

- Components look like HTML templates (actually JSX)
- They can contain 'state' data or UI state
- They also can contain JavaScript for functionality

### Example: Class Component with State

```jsx
class App extends React.Component {
  state = {
    name: "Ryu",
    age: 30,
  };
  render() {
    return (
      <div className="app-content">
        <h1>Hello, ninjas!</h1>
        <p>
          My name is: {this.state.name} and I am {this.state.age}
        </p>
      </div>
    );
  }
}
```

## Setting Up React

### Basic HTML Template with React

```html
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <meta http-equiv="X-UA-Compatible" content="ie=edge" />
    <title>Document</title>
  </head>
  <body>
    <div id="app"></div>
  </body>
</html>
```

### Adding React Scripts

```html
<script
  crossorigin
  src="https://unpkg.com/react@18/umd/react.development.js"
></script>
<script
  crossorigin
  src="https://unpkg.com/react-dom@18/umd/react-dom.development.js"
></script>
```

### Complete Setup Example

```html
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <meta http-equiv="X-UA-Compatible" content="ie=edge" />
    <script
      crossorigin
      src="https://unpkg.com/react@16/umd/react.development.js"
    ></script>
    <script
      crossorigin
      src="https://unpkg.com/react-dom@16/umd/react-dom.development.js"
    ></script>
    <title>Document</title>
  </head>
  <body>
    <div id="app"></div>
  </body>
</html>
```

## VS Code Packages for React Development

### Recommended Extension:

**ES7 React/Redux/GraphQL/React-Native snippets**  
Simple extensions for React, Redux and GraphQL in VS Code with ES7 syntax.

**Supported languages:**

- JavaScript (.js)
- JavaScript React (.jsx)
- TypeScript (.ts)
- TypeScript React (.tsx)

## Class Based Components

### React Hooks Timeline

- In 2018 conference hooks introduced
- React 16.8.0 is the first release to support Hooks (launch in 2019)
- In 2023 new documentation website launch for React 18 and onwards
- There are no plans to remove classes from React

**Important:** A class based component must have at least 1 function that is `render()`

### Basic Class Component Structure

```html
<html lang="en">
  <head>
    <!-- Head content with React scripts -->
  </head>
  <body>
    <div id="app"></div>
    <script>
      class App extends React.Component {
        render() {
          return (
            <div>
              <h1>Hey, ninjas</h1>
            </div>
          );
        }
      }
    </script>
  </body>
</html>
```

## JSX Rules

### Rule 1: Only One Root Element

In JSX only one root element can be defined.

**Wrong:**

```jsx
return (
    <div>
        <h1>Hey, ninjas</h1>
    </div>
    <h1>
    <h3>
)
```

### Rule 2: Use `className` instead of `class`

Instead of `class` in JavaScript we will use `className` in JSX.

**Correct:**

```jsx
<div className="app-content">
  <h1>Hey, ninjas</h1>
</div>
```

## Rendering Components

### Complete Working Example

```html
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <meta http-equiv="X-UA-Compatible" content="ie=edge" />
    <script
      crossorigin
      src="https://unpkg.com/react@16/umd/react.development.js"
    ></script>
    <script
      crossorigin
      src="https://unpkg.com/react-dom@16/umd/react-dom.development.js"
    ></script>
    <title>Document</title>
  </head>
  <body>
    <div id="app"></div>
    <script>
      class App extends React.Component {
        render() {
          return (
            <div className="app-content">
              <h1>Hey, ninjas</h1>
            </div>
          );
        }
      }
      ReactDOM.render(<App />, document.getElementById("app"));
    </script>
  </body>
</html>
```

## Babel for JSX Transformation

### Why Babel?

Not understanding JSX: because JSX is not supported in browsers. Babel transforms JSX into regular JavaScript.

### Adding Babel

```html
<script src="https://unpkg.com/babel-standalone@6/babel.min.js"></script>
```

### Complete Babel Setup

```html
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <meta http-equiv="X-UA-Compatible" content="ie=edge" />
    <script src="https://unpkg.com/babel-standalone@6/babel.min.js"></script>
    <script
      crossorigin
      src="https://unpkg.com/react@16/umd/react.development.js"
    ></script>
    <script
      crossorigin
      src="https://unpkg.com/react-dom@16/umd/react-dom.development.js"
    ></script>
    <title>Document</title>
  </head>
  <body>
    <div id="app"></div>
    <script type="text/babel">
      class App extends React.Component {
        render() {
          return (
            <div className="app-content">
              <h1>Hey, ninjas</h1>
            </div>
          );
        }
      }
      ReactDOM.render(<App />, document.getElementById("app"));
    </script>
  </body>
</html>
```

## Using JavaScript in JSX

### Example with Math.random()

```jsx
<div className="app-content">
  <h1>Hey, ninjas</h1>
  <p>{Math.random() * 10}</p>
</div>
```

**Note:** JavaScript expressions must be wrapped in curly braces `{}`

## Component State

### What is State?

- JavaScript Object
- Describes the current state of the component (data, UI-state)
- The state of a component can be updated over time
  - A modal could close
  - The data we output could change

### Example: Shopping Cart Component State

```jsx
items: [
  { name: "navy jumper", price: 9.99 },
  { name: "ninja mask", price: 20.0 },
  { name: "black cloak", price: 15.0 },
];
```

State will be changed if another item will be added in the items.

### Example: Popup Component State

```jsx
{
  showPopup: true;
}
{
  showPopup: false;
}
```

### Implementing State in Components

```jsx
class App extends React.Component {
  state = {
    name: "Ryu",
    age: 30,
  };
  render() {
    return (
      <div className="app-content">
        <h1>Hey, ninjas</h1>
        <p>
          My name is: {this.state.name} and I am {this.state.age}
        </p>
      </div>
    );
  }
}
```

### Displaying State Values

```jsx
<p>
  My name is: {this.state.name} and I am {this.state.age}
</p>
```

**Key Concept:** Whenever a state will be changed, the data will be changed in the UI.

## React Dev Tools

### Installation

Download React DevTools for a better development experience:  
https://chromewebstore.google.com/detail/react-developer-tools/fmkadmapgofadopljbjfkapdkoienihi

### Purpose

- To interact with components
- Not for end users - just for developers to play around with
- Allows viewing component props and state

### Features

- Highlight Updates
- Highlight Search
- View component hierarchy
- Inspect props and state

## DOM Events in React

### Basic Event Handling

```jsx
class App extends React.Component {
  state = {
    name: "Ryu",
    age: 30,
  };

  render() {
    return (
      <div className="app-content">
        <h1>Hey, ninjas</h1>
        <p>
          My name is: {this.state.name} and I am {this.state.age}
        </p>
        <button>Click Me</button>
      </div>
    );
  }
}
```

### Correct Event Syntax

**Wrong:**

```jsx
<button onClick="callfunc()">Click Me</button>
<button onClick=callfunc()>Click Me</button>
<button onClick=(handleClick)>Click Me</button>
```

**Correct:**

```jsx
<button onClick={this.handleClick}>Click Me</button>
```

### Creating Event Handlers

```jsx
class App extends React.Component {
  state = {
    name: "Ryu",
    age: 30,
  };

  handleClick(e) {
    console.log(e.target);
  }

  render() {
    return (
      <div className="app-content">
        <h1>Hey, ninjas</h1>
        <p>
          My name is: {this.state.name} and I am {this.state.age}
        </p>
        <button onClick={this.handleClick}>Click Me</button>
      </div>
    );
  }
}
```

### Multiple Event Handlers

```jsx
class App extends React.Component {
  state = {
    name: "Ryu",
    age: 30,
  };

  handleClick(e) {
    console.log(e.target);
  }

  handleMouseOver(e) {
    console.log(e.target, e.pageX);
  }

  handleCopy(e) {
    console.log("Try being original for once!");
  }

  render() {
    return (
      <div className="app-content">
        <h1>Hey, ninjas</h1>
        <p>
          My name is: {this.state.name} and I am {this.state.age}
        </p>
        <button onClick={this.handleClick}>Click Me</button>
        <button onMouseOver={this.handleMouseOver}>Hover me</button>
        <p onCopy={this.handleCopy}>What we think, we become</p>
      </div>
    );
  }
}
```

**Reference:** Events in React - https://reactjs.org/docs/events.html#supported-events

## The 'this' Context Problem

### The Issue

When using event handlers, the context of `this` is lost. In render function React handles it by itself, but in our custom functions we have to deal with it manually.

**Error Example:**

```jsx
handleClick(e){
    console.log(this.state.age); // Error: Cannot read property 'state' of undefined
}
```

### Solution: Arrow Functions

Arrow functions preserve the `this` context from where they were defined.

```jsx
handleClick = (e) => {
  console.log(this.state);
};

handleMouseOver = (e) => {
  console.log(e.target, e.pageX);
};

handleCopy = (e) => {
  console.log("Try being original for once!");
};
```

### Complete Example with Arrow Functions

```jsx
class App extends React.Component {
  state = {
    name: "Ryu",
    age: 30,
  };

  handleClick = (e) => {
    console.log(this.state);
  };

  handleMouseOver = (e) => {
    console.log(e.target, e.pageX);
  };

  handleCopy = (e) => {
    console.log("Try being original for once!");
  };

  render() {
    return (
      <div className="app-content">
        <h1>Hey, ninjas</h1>
        <p>
          My name is: {this.state.name} and I am {this.state.age}
        </p>
        <button onClick={this.handleClick}>Click Me</button>
        <button onMouseOver={this.handleMouseOver}>Hover me</button>
        <p onCopy={this.handleCopy}>What we think, we become</p>
      </div>
    );
  }
}
```

## Changing State

### Wrong Way to Change State

**Not a good practice:**

```jsx
handleClick = (e) => {
  this.state.name = "yoshi"; // Direct mutation - DON'T DO THIS
  console.log(this.state);
};
```

### Correct Way: Using setState()

```jsx
handleClick = (e) => {
  this.setState({
    name: "Yoshi",
  });
  console.log(this.state);
};
```

### Changing Multiple State Values

```jsx
handleClick = (e) => {
  this.setState({
    name: "Yoshi",
    age: 25,
  });
  console.log(this.state);
};
```

### Complete Example with State Updates

```jsx
class App extends React.Component {
  state = {
    name: "Ryu",
    age: 30,
  };

  handleClick = (e) => {
    this.setState({
      name: "Yoshi",
      age: 25,
    });
  };

  handleMouseOver = (e) => {
    console.log(e.target, e.pageX);
  };

  handleCopy = (e) => {
    console.log("Try being original for once!");
  };

  render() {
    return (
      <div className="app-content">
        <h1>Hey, ninjas</h1>
        <p>
          My name is: {this.state.name} and I am {this.state.age}
        </p>
        <button onClick={this.handleClick}>Click Me</button>
        <button onMouseOver={this.handleMouseOver}>Hover me</button>
        <p onCopy={this.handleCopy}>What we think, we become</p>
      </div>
    );
  }
}
```

**Result:** When the button is clicked, the UI updates to show "My name is: Yoshi and I am 25"
