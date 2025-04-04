all_functions = [
    {
        "type":"function",
        "function":{
            "name": "get_restaurant_pages",
            "description": "This function finds a restaurant that has similar food or name to what the user is asking for. Not all the restaurants found are necessarily the best option for the user, use the description of the restaurant as a proxy to suggest it to them.",
            "parameters": {
                "type": "object",
                "properties": {
                    "name_of_restaurant": {
                        "type": "string",
                        "description": "Not mandatory. The name of the restaurant. In case the user didn't specify it in the request, it should be set to null."
                    },
                    "type_of_restaurant": {
                        "type": "string",
                        "description": "The type of food or restaurant that the user requested. E.g. Italian, Pizza, Sushi, Indian, Vegan, etc..."
                    },
                    "food_requested": {
                        "type": "array",
                        "description": "Not mandatory. The array of foods that the user requested. E.g. Pizza, Pasta, etc... . In case the user didn't specify it in the request, it should be set to [null].",
                        "items": {
                            "type": "string"
                        }
                    },
                    "quantity": {
                        "type": "integer",
                        "description": "Not mandatory. The amount of restaurants you judge its preferable to search in order to serve the user. It should be default to 1, however if the user request is broad you should set 2,3,4 or even 5"
                    },
                    "other_information": {
                        "type": "string",
                        "description": "All other information that the user provided that could potentially help finding the best matching restaurant for them. In case there aren't any information, set it to null"
                    }
                }
            },
            "required": [
                "name_of_restaurant",
                "type_of_restaurant",
                "food_requested",
                "other_information",
                "quantity"
            ]
        }
    },
    {
        "type":"function",
        "function":{
            "name": "open_restaurant_page",
            "description": "This function opens the page of a given restaurant, it can only open one restaurant at a time. Always confirm with the user that you are going to search and open a restaurant page with the information provided before calling the function. This function can only be called after the function get_restaurant_pages.",
            "parameters": {
                "type": "object",
                "properties": {
                    "restaurant_uuid": {
                        "type": "string",
                        "description": "The number of the restaurant page that comes in the function get_restaurant_pages previously called"
                    }
                }
            },
            "required": [
                "restaurant_uuid"
            ]
        }
    },
    {
        "type":"function",
        "function":{
            "name": "close_restaurant_page",
            "description": "This function closes the page of a given restaurant and goes back to the main page (menu with all the restaurants) x. This function can be called if a restaurant page is already open, you can check the recent actions with get_user_actions to verify it, before calling the function",
            "parameters": {
                "type": "object",
                "properties": {}
            }
        }
    },
    {
        "type":"function",
        "function":{
            "name": "get_user_actions",
            "description": "This function returns the list of the latest 10 user actions. This function should be called when you need to collect more information about what were the latest actions the user of the chatbot interface, like what is the current opened restaurant, what is the current state of the shopping cart, etc... Very often it is best to call this function before calling some other functions",
            "parameters": {
                "type": "object",
                "properties": {}
            }
        }
    },
    {
        "type":"function",
        "function":{
            "name": "get_menu_of_restaurant",
            "description": "This function returns the list of the menu of a given restaurant. This function should be called when you need to collect more information about what is the menu of a given restaurant. Very often it is best to get the recent actions before calling this function, so you can know what is the restaurant uuid that you need to pass to this function. Always after calling this function create a short-list of suggestions based on the chat history with the user, displaying name, description and price of the given food",
            "parameters": {
                "type": "object",
                "properties": {
                    "restaurant_uuid": {
                        "type": "string",
                        "description": "The id of the restaurant page that comes in the function get_restaurant_pages previously called, or in the get_user_actions function if the user opened a restaurant page"
                    }
                }
            },
            "required": [
                "restaurant_uuid"
            ]
        }
    },
    {
        "type":"function",
        "function":{
            "name": "add_food_to_cart",
            "description": "This function adds food to the user's shopping cart. It should only be called if you have the information of the restaurant_id, food_id and amount (quantity) of the food the user is referring to. You can get more information of the restaurant_id opened in the users interface by calling the get_user_actions and you can get the food_id by calling the get_menu_of_restaurant function. You can call this function multiple times in a row if there are several food items to be added",
            "parameters": {
                "type": "object",
                "properties": {
                    "restaurant_uuid": {
                        "type": "string",
                        "description": "The id of the restaurant page that comes in the function get_restaurant_pages previously called, or in the get_user_actions function if the user opened a restaurant page"
                    },
                    "food_id": {
                        "type": "string",
                        "description": "The id of the food that comes in the function get_menu_of_restaurant previously called"
                    },
                    "quantity": {
                        "type": "integer",
                        "description": "The quantity of the food that the user wants to add to the cart"
                    }
                }
            },
            "required": [
                "restaurant_uuid",
                "food_id",
                "quantity"
            ]
        }
    },
    {
        "type":"function",
        "function":{
            "name": "remove_food_from_cart",
            "description": "This function removes food from the user's shopping cart. It should only be called if you have the information of the restaurant_id and food_id of the food the user is referring to. You can get more information of the restaurant_id opened in the users interface by calling the get_user_actions and you can get the food_id by calling the get_menu_of_restaurant function. You can call this function multiple times in a row if there are several food items to be removed",
            "parameters": {
                "type": "object",
                "properties": {
                    "restaurant_uuid": {
                        "type": "string",
                        "description": "The id of the restaurant page that comes in the function get_restaurant_pages previously called, or in the get_user_actions function if the user opened a restaurant page. Make sure you know all the parameters before calling this function. Call auxiliary functions before calling it, if necessary."
                    },
                    "food_id": {
                        "type": "string",
                        "description": "The id of the food that comes in the function get_menu_of_restaurant previously called"
                    }
                }
            },
            "required": [
                "restaurant_uuid",
                "food_id"
            ]
        }
    },
    {
        "type":"function",
        "function":{
            "name": "open_shopping_cart",
            "description": "This function opens the shopping cart of the user. It should be called if the user wants it, or if you need more information about the items in the shopping cart",
            "parameters": {
                "type": "object",
                "properties": {}
            }
        }
    },
    {
        "type":"function",
        "function":{
            "name": "close_shopping_cart",
            "description": "This function closes the shopping cart of the user. It should be called if the user wants it, or after placing an order",
            "parameters": {
                "type": "object",
                "properties": {}
            }
        }
    },
    {
        "type":"function",
        "function":{
            "name": "place_order",
            "description": "This function places an order with the food items that the user has in the shopping cart. It should be called if the user specifies or confirms that they want to place an order",
            "parameters": {
                "type": "object",
                "properties": {}
            }
        }
    },
    {
        "type":"function",
        "function":{
            "name": "activate_handsfree",
            "description": "This function activates a handsfree chat experience where you are always answering by voice to the user interface",
            "parameters": {
                "type": "object",
                "properties": {}
            }
        }
    }
]