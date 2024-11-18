import React, { useState } from "react";

function SearchBar({ onSearch }) {
    const [query, setQuery] = useState("")
    
    return (
    <div className="w-full max-w-xl flex mx-auto p-20 text-xl">
        <input 
            type="text"
            className="w-full placeholder-gray-400 text-gray-900 p-4"
            placeholder="Enter Cocktail or Ingredient Name"
            value={query}
        />
        <button className="bg-white p-4"></button>
    </div>
  );
}

export default SearchBar;
