import React from "react";

function CocktailList({ cocktails, onSelect }) {
  if (cocktails.length === 0) {
    return <p>No cocktails found.</p>;
  }
}

export default CocktailList;
