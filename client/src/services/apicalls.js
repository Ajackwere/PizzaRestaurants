// Restaurants Api

const URL = 'https://pizza-restaurants-ztzb.onrender.com/'
export const getRestaurants = () => {
    return fetch(URL+'restaurants')
}
