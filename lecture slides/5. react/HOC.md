# Higher-Order Components (HOC) in React – Study Notes

---

## 1. Introduction to HOC

Higher-Order Components (HOCs) are a pattern in React used to reuse component logic.  
An HOC is a function that takes a component and returns a new component with enhanced functionality.

---

## 2. Example 1: HOC for Loading State

### HOC Definition: `withLoading.jsx`

```jsx
import React from "react";

const withLoading = (WrappedComponent) => {
  return function WithLoadingComponent({ isLoading, ...props }) {
    if (isLoading) {
      return <h2>Loading...</h2>;
    }
    return <WrappedComponent {...props} />;
  };
};

export default withLoading;
```

**Explanation:**

- `withLoading` is a function that takes a `WrappedComponent`.
- It returns a new component (`WithLoadingComponent`).
- If `isLoading` is true, it shows a loading message.
- Otherwise, it renders the `WrappedComponent` with all other props passed down.

---

### Component to Enhance: `UserList.jsx`

```jsx
import React from "react";

const UserList = ({ users }) => {
  return (
    <ul>
      {users.map((user, idx) => (
        <li key={idx}>{user}</li>
      ))}
    </ul>
  );
};

export default UserList;
```

**Explanation:**

- This component receives a `users` prop (array of names).
- It maps through the array and displays each user in a list item.

---

### Using the HOC: `App.jsx`

```jsx
import React, { useState, useEffect } from "react";
import UserList from "./UserList";
import withLoading from "./withLoading";

const EnhancedUserList = withLoading(UserList);

const App = () => {
  const [loading, setLoading] = useState(true);
  const [users, setUsers] = useState([]);

  useEffect(() => {
    setTimeout(() => {
      setUsers(["Alice", "Bob", "Charlie"]);
      setLoading(false);
    }, 2000);
  }, []);

  return (
    <div>
      <h1>Users</h1>
      <EnhancedUserList isLoading={loading} users={users} />
    </div>
  );
};

export default App;
```

**Explanation:**

- `EnhancedUserList` is created by passing `UserList` to `withLoading`.
- In `App`, `loading` starts as `true` and `users` as empty.
- After 2 seconds, users are set and `loading` becomes `false`.
- The `EnhancedUserList` receives `isLoading` and `users` props and conditionally shows loading or the list.

---

## 3. Example 2: HOC for Authentication

### HOC Definition: `withAuth.jsx`

```jsx
import React from "react";

const withAuth = (WrappedComponent) => {
  return function WithAuthComponent({ isLoggedIn, ...props }) {
    if (!isLoggedIn) {
      return <h2>You must be logged in to view this content.</h2>;
    }
    return <WrappedComponent {...props} />;
  };
};

export default withAuth;
```

**Explanation:**

- `withAuth` wraps a component and checks if the user is logged in.
- If `isLoggedIn` is false, it shows a message.
- If true, it renders the wrapped component with its props.

---

### Component to Protect: `Dashboard.jsx`

```jsx
import React from "react";

const Dashboard = ({ username }) => {
  return <h2>Welcome to your dashboard, {username}!</h2>;
};

export default Dashboard;
```

**Explanation:**

- A simple dashboard component that welcomes the user by name.

---

### Using the HOC: `App.js`

```jsx
import React, { useState } from "react";
import Dashboard from "./Dashboard";
import withAuth from "./withAuth";

const ProtectedDashboard = withAuth(Dashboard);

const App = () => {
  const [isLoggedIn, setIsLoggedIn] = useState(false);

  const handleLogin = () => {
    setIsLoggedIn(true); // login logic
  };

  return (
    <div>
      <h1>My App</h1>
      {!isLoggedIn && <button onClick={handleLogin}>Login</button>}
      <ProtectedDashboard isLoggedIn={isLoggedIn} username="Ali" />
    </div>
  );
};

export default App;
```

**Explanation:**

- `ProtectedDashboard` is created by wrapping `Dashboard` with `withAuth`.
- Initially, `isLoggedIn` is false, so the button is shown.
- Clicking the button logs the user in and the dashboard is displayed.
- The `ProtectedDashboard` receives `isLoggedIn` and `username` props.

---

## 4. Key Concepts

- **HOC is a function** that takes a component and returns a new component.
- Used for **cross-cutting concerns** like loading, authentication, logging, etc.
- The wrapped component receives **additional props** from the HOC.
- HOCs **do not modify** the original component; they **compose** it with extra behavior.

---

## 5. Code Pattern Summary

```jsx
const HOC = (WrappedComponent) => {
  return function NewComponent(props) {
    // Add logic here
    return <WrappedComponent {...props} />;
  };
};
```

---

**End of Notes** – All examples and explanations from the slides are included.
