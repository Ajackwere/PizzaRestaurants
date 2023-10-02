import React, { useState } from 'react'
import { useEffect } from 'react';

export default function PizzaList() {
    const [pizzas, setPizza] = useState([]);
    useEffect(() => {
        fetch("https://pizza-restaurants-ztzb.onrender.com/pizzas")
          .then((r) => r.json())
          .then((data) => setPizza(data))
          .catch((error) => console.error(error));
      }, []);
      return <div>
        <h2>List of Available Pizzas</h2>
        <ul>
            {pizzas.map((pizza) => (
                <li key={pizza.id}>{pizza.name} {pizza.ingredient}</li>
            ))}
        </ul>
      </div>;
}