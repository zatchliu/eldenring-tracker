// src/components/CharacterList.js
import React, { useState, useEffect } from 'react';
import axios from 'axios';

const CharacterList = () => {
  const [characters, setCharacters] = useState([]);

  useEffect(() => {
    fetchCharacters();
  }, []);

  const fetchCharacters = async () => {
    try {
      const response = await axios.get('/api/characters/');
      setCharacters(response.data);
    } catch (error) {
      console.error('Error fetching characters:', error);
    }
  };

  return (
    <div>
      <h2>Character List</h2>
      <ul>
        {characters.map((character) => (
          <li key={character.id}>
            <p>Name: {character.name}</p>
            <p>Class: {character.character_class}</p>
            {/* Add other character information as needed */}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default CharacterList;

