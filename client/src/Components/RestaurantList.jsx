import React, { useEffect, useState } from "react";

export default function RestaurantList() {
  const [restaurants, setRestaurants] = useState([]);

  useEffect(() => {
    fetch("https://pizza-restaurants-ztzb.onrender.com/restaurants")
      .then((r) => r.json())
      .then((data) => setRestaurants(data))
      .catch((error) => console.error(error));
  }, []);
  return <div>
    <h2 className="bg-red-300">List of Restaurants</h2>
    <ul>
        {restaurants.map((restaurant) => (
            <li key={restaurant.id}>{restaurant.name} {restaurant.address}</li>
        ))}
    </ul>
  </div>;
}
