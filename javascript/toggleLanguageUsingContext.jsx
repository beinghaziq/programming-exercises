import React, { useState, createContext, useContext } from 'react';
import { createRoot } from 'react-dom/client';

const languages = ['JavaScript', 'Python'];
const ToggleContext = createContext();

const ToggleProvider = ({ children }) => {
  const [value, setValue] = useState('Python');

  const toggleLanguage = () => {
    setValue(prev => (prev === 'Python' ? 'JavaScript' : 'Python'));
  };

  return (
    <ToggleContext.Provider value={{ value, toggleLanguage }}>
      {children}
    </ToggleContext.Provider>
  );
};

function MainSection() {
  const { value, toggleLanguage } = useContext(ToggleContext);

  return (
    <div>
      <p id="favoriteLanguage">Favorite programming language: {value}</p>
      <button id="changeFavorite" onClick={toggleLanguage}>
        Toggle Language
      </button>
    </div>
  );
}

function App() {
  return (
    <ToggleProvider>
      <MainSection />
    </ToggleProvider>
  );
}

const container = document.getElementById('root');
const root = createRoot(container);
root.render(<App />);
