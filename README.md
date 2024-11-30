# 100-days-of-code

# Portfolio Projects

This section highlights the projects and code worked on during the 100 days of coding challenge.

## Day 37: [Tracking Daily Water Intake with Pixela](./Day37/water_tracker.py)

### Description
On **Day 37**, I integrated the **Pixela API** to track daily water intake. This involved:

1. **User Account Creation**: Using the Pixela API to create a user profile with personalized credentials (username and password) for tracking activities.
2. **Graph Setup**: Configuring a graph to visualize daily water consumption. The graph was customized to track water intake in **litres**, using a **float** type and a **"sora"** color theme.
3. **Logging Data**: A Python script was written to prompt the user for the daily water intake, which is then logged using a POST request to the Pixela API. This helps visualize hydration progress over time.

---

## Day 38: [Exercise Tracker Code](./Day38/exercise_tracker.py)

This Python script tracks the user's exercise data and logs it into a Google Sheet via the Sheety API, integrating data from the Nutritionix API. The main features of the code are as follows:

### Functionality
1. **User Input**:
   - The user is prompted to enter the type of exercise they performed.

2. **Nutritionix API**:
   - The code sends a POST request to the [Nutritionix API](https://trackapi.nutritionix.com/) to fetch exercise details such as calories burned and exercise duration.
   - The user's gender, weight, height, and age are sent along with the exercise query to get accurate results.

3. **Exercise Data Parsing**:
   - The response from the Nutritionix API is parsed to extract details about the exercise such as name, duration, and calories burned.

4. **Logging to Google Sheet**:
   - The code formats the exercise details into a JSON structure and sends a POST request to the [Sheety API](https://sheety.co/), which logs the data into a specified Google Sheet.

5. **Date and Time**:
   - The current date and time are captured using the `datetime` module to log when the exercise occurred.

### Example Workflow

1. User enters the exercise: "Running".
2. The script sends a request to the Nutritionix API, and the exercise details (e.g., duration and calories) are returned.
3. The data is formatted and sent to a Google Sheet using the Sheety API.
4. The script outputs a confirmation message with the result of the POST request to Sheety.

---

## Day 39: [Flight Price Alert System](./Day39/flight_price_alert.py)

### Description
On **Day 39**, I built a **Flight Price Alert System** that automatically tracks flight prices and sends notifications to customers when the price drops below a specified threshold. The system integrates data from multiple sources, including a Google Sheet for destination data, a flight search API to get flight prices, and a notification manager to send updates to customers.

### Key Features:
1. **Airport Code Update**:
   - The code first ensures all destination cities have an airport IATA code by calling an API to retrieve the codes and updating the Google Sheet.
   
2. **Flight Search**:
   - The system searches for direct flights first and then looks for indirect flights if direct flights are unavailable. It checks flight prices for destinations from a specific origin airport for the next six months.

3. **Cheapest Flight Detection**:
   - The script identifies the cheapest flight option, whether direct or indirect, and compares it to the lowest price already recorded in the Google Sheet for that destination.

4. **Notifications and Emails**:
   - If the price drops below the recorded lowest price, the system sends notifications via **WhatsApp** and emails to a list of customers.

### Workflow:
1. **Data Retrieval**:
   - The system retrieves destination data and customer emails from the Google Sheet.
   
2. **Flight Price Check**:
   - The system checks for the cheapest flights for each destination. If no direct flight is found, it searches for indirect options.

3. **Sending Notifications**:
   - If a cheaper flight is found, the system sends an SMS or WhatsApp message and emails to all customers on the list with details of the flight and pricing.

### Outcome:
- This system allows users to be alerted when flight prices drop, helping them book tickets at a lower cost. The code also ensures that customers are kept up-to-date on available flight deals.
