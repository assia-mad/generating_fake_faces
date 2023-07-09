import React, { useState } from 'react';
import axios from 'axios';
import './App.css';

function App() {
  const [imageSrc, setImageSrc] = useState(null);
  const [numImages, setNumImages] = useState(5);

  const generateImage = () => {
    axios
      .get(`http://localhost:8000/generate_image?num_images=${numImages}`)
      .then((response) => {
        const { image } = response.data;
        setImageSrc(`data:image/png;base64,${image}`);
      })
      .catch((error) => {
        console.error('Error:', error);
      });
  };

  const handleNumImagesChange = (e) => {
    setNumImages(e.target.value);
  };

  return (
    <div className="app-container">
      <h1 className="app-title">Generated Image</h1>
      <div className="input-container">
        <label htmlFor="square">Square Dimension:</label>
        <input
          type="number"
          id="square"
          value={numImages}
          onChange={handleNumImagesChange}
        />
      </div>
      <button className="generate-button" onClick={generateImage}>
        Generate
      </button>
      {imageSrc && <img src={imageSrc} alt="Generated Image" />}
    </div>
  );
}

export default App;
