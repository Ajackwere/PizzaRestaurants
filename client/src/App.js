import "./App.css";
import PizzaList from "./Components/PizzaList";
import RestaurantList from "./Components/RestaurantList";

function App() {
  return (
    <div className="">
      <h1>Pizza App</h1>
      <RestaurantList/>
      <PizzaList/>
    </div>
  );
}

export default App;
