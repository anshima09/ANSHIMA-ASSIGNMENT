export default function handler(req, res) {
  const articles = [
    {
      id: 1,
      title: 'Understanding React Hooks',
      content: `React Hooks like useState, useEffect, and useContext allow you to use state and other React features without writing a class. Hooks simplify component logic and make code more reusable by separating concerns into smaller functions.`,
    },
    {
      id: 2,
      title: 'Introduction to REST APIs',
      content: `REST APIs are a standard way to enable communication between different software systems using HTTP requests. They follow CRUD operations—Create, Read, Update, Delete—and are widely used in modern web and mobile applications.`,
    },
    {
      id: 3,
      title: 'JavaScript ES6 Features',
      content: `ES6 introduced many improvements to JavaScript, such as arrow functions, template literals, destructuring, spread/rest operators, and ` + "`let`" + ` and ` + "`const`" + `. These features make your code more concise and easier to maintain.`,
    },
    {
      id: 4,
      title: 'Why Use TypeScript?',
      content: `TypeScript is a statically typed superset of JavaScript that helps catch errors at compile time and improves developer productivity. It offers features like interfaces, enums, and optional chaining while still compiling down to clean JavaScript.`,
    },
    {
      id: 5,
      title: 'What is CI/CD?',
      content: `Continuous Integration (CI) and Continuous Deployment (CD) are practices that help automate software delivery. CI ensures code changes are automatically tested and merged, while CD automates deployment to production, increasing release speed and reliability.`,
    },
  ];

  res.status(200).json(articles);
}
