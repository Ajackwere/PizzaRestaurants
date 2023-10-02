import "./index.css";

import PizzaList from "./Components/PizzaList";
import RestaurantList from "./Components/RestaurantList";

function App() {
  return (
    <div className="mb-6 justify-center">
      <h1 className="mt-5 mb-6 bg-slate-100 justify-center front-semibold">Pizza App</h1>
      <RestaurantList />
      <PizzaList />
    </div>
  );
}

export default App;
