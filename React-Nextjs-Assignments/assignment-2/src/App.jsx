import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'

function App() {
   const [count, setCount] = useState(0);

  const [text, setText] = useState('');

  const [isVisible, setIsVisible] = useState(true);

  return (
    <div style={{ padding: '20px', fontFamily: 'Arial' }}>
      {/* Counter Component */}
      <div style={{ marginBottom: '30px' }}>
        <h2>1. Counter to increase and decrease value</h2>
        <p>Count: {count}</p>
        <button onClick={() => setCount(count + 1)}>Increment</button>
        <button onClick={() => setCount(count - 1)} style={{ marginLeft: '10px' }}>Decrement</button>
      </div>

      {/* Input Display Component */}
      <div style={{ marginBottom: '30px' }}>
        <h2>Live Text Display </h2>
        <input
          type="text"
          placeholder="Type something..."
          value={text}
          onChange={(e) => setText(e.target.value)}
        />
        <p>You typed: {text}</p>
      </div>

      {/* Visibility Toggle Component */}
      <div>
        <h2>Visibility Toggle</h2>
        <button onClick={() => setIsVisible(!isVisible)}>
          {isVisible ? 'Hide' : 'Show'} Paragraph
        </button>
        {isVisible && <p>This is a toggleable paragraph. Click the button to hide me.</p>}
      </div>
    </div>
  );
}

export default App
