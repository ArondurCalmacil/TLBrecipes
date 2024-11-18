import React, { useState } from "react";
import axios from 'axios';
import SearchBar from "./components/SearchBar";
import CocktailList from "./components/CocktailList";
import CocktailDetails from "./components/CocktailDetails";

const API_HOST = "https://the-cocktail-db.p.rapidapi.com";
const API_KEY = "540b011b8fmshbd4250a8cc9bba9p146cbdjsn9edcab48a0f8";

function App() {
  return (
    <div className="App">
      <h1>Cocktail Finder</h1>
      <SearchBar />
    </div>
  );
}

export default App;
