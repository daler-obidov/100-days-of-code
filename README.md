# 100-days-of-code

# Portfolio Projects

This section highlights the projects and code worked on during the 100 days of coding challenge.

## Day 33: [Kanye Quote Generator](code/day-33)

### Description
On **Day 33**, I built a simple **Kanye Quote Generator** app using **Tkinter** for the graphical user interface (GUI) and the **Kanye REST API** to fetch random Kanye West quotes.

### Key Features:
1. **GUI with Tkinter**:
   - The app uses the Tkinter library to create a window with an image background and a button to trigger the quote fetch process.
   
2. **API Integration**:
   - The app makes a GET request to the **Kanye REST API** (`https://api.kanye.rest`) to fetch a random Kanye West quote. This quote is then displayed in the window.
   
3. **Dynamic Quote Display**:
   - The `get_quote` function updates the text of the quote displayed on the canvas when the user clicks the button. The quote is fetched from the API and is displayed on the canvas element in the center of the window.

4. **Button for New Quotes**:
   - The app includes a button with an image of Kanye West that, when clicked, fetches and displays a new random quote.

### Workflow:
1. **Window Setup**:
   - The Tkinter window is created, and a background image is set using the `PhotoImage` class.
   
2. **Fetching Quotes**:
   - When the user clicks the button, the `get_quote` function is triggered. This function sends a request to the Kanye API, fetches the quote, and updates the text on the canvas.

3. **Interactive UI**:
   - The user interacts with the app by clicking the button, which changes the displayed quote. The window also features an image background and a button image for a visually appealing interface.

### Outcome:
- The app allows users to get a random Kanye West quote at the click of a button, making it a fun and interactive tool with a simple but effective GUI. It demonstrates how to work with APIs and Tkinter to build user-friendly applications.

## Day 35: [Quiz Application](code/day-34-35)

### Description
On **Day 35**, I built a **Quiz Application** that allows users to answer questions from a predefined list and keeps track of their score. The application consists of multiple components, including a question model, quiz logic, and a user interface.

### Key Features:
1. **Question Model**:
   - The `Question` class is used to define each question and its correct answer. The questions are stored in a list to be used throughout the quiz.

2. **Quiz Logic**:
   - The `QuizBrain` class handles the logic of displaying questions, checking user answers, and keeping track of the score. It also determines if there are more questions to answer.
   - The method `next_question` retrieves the next question in the list, and `check_answer` validates whether the user's answer is correct.

3. **User Interface**:
   - The `QuizInterface` class handles the graphical user interface (GUI) for the quiz, interacting with the user and displaying the questions and score.

4. **Data Integration**:
   - The quiz uses a predefined list of questions from a `question_data` file, which is imported and used to create a list of `Question` objects. This data is then passed to the `QuizBrain` for quiz execution.

### Workflow:
1. **Question Creation**:
   - The questions and answers are loaded from the `question_data` file and stored in `Question` objects.
   
2. **Quiz Progression**:
   - The quiz progresses one question at a time. After each answer, the quiz updates the score based on whether the answer is correct and moves to the next question.
   
3. **Score Keeping**:
   - The user's score is updated after each question, and at the end of the quiz, the user is presented with their final score.

### Outcome:
- The application offers an interactive way for users to take a quiz. It keeps track of answers, ensures correct answers are scored, and displays the final score once the quiz is finished.

## Day 36: [Stock Price Notification System](code/day-36)

### Description
On **Day 36**, I created a **Stock Price Notification System** that sends alerts about stock price changes and the latest news for a given stock. The system integrates several APIs: Alpha Vantage for stock price data, NewsAPI for related news, and Twilio for sending SMS notifications. 

### Key Features:
1. **Stock Price Retrieval**:
   - The system fetches the stock price for a given stock symbol (e.g., AAPL for Apple Inc) from the **Alpha Vantage API**. It compares the closing prices for the last two days to detect significant price movements.

2. **Price Change Detection**:
   - If the price change is greater than 1%, the system sends a notification with the price change direction (up or down) and the percentage change.

3. **News API Integration**:
   - The system uses the **NewsAPI** to get the latest news articles related to the stock and include them in the notification. The top 3 relevant news headlines are included in the message.

4. **Twilio SMS Notifications**:
   - The system sends SMS messages to the user with the price change details and the latest news using the **Twilio API**.

### Workflow:
1. **Retrieve Stock Data**:
   - The system fetches the stock data for the provided symbol using the Alpha Vantage API.

2. **Compare Prices**:
   - It compares the closing prices of the last two days to determine the price change and percentage difference.

3. **Send Notifications**:
   - If the price change is greater than 1%, the system formats the message with the price direction, percentage change, and the top 3 news headlines related to the stock.
   - The message is then sent via SMS to the user using the Twilio API.

### Outcome:
- The system provides real-time updates on stock price changes and keeps users informed about the latest news related to their stock. This can be useful for traders or investors who need quick updates to make informed decisions.

## Day 37: [Tracking Daily Water Intake with Pixela](code/day-37)

### Description
On **Day 37**, I integrated the **Pixela API** to track daily water intake. This involved:

1. **User Account Creation**: Using the Pixela API to create a user profile with personalized credentials (username and password) for tracking activities.
2. **Graph Setup**: Configuring a graph to visualize daily water consumption. The graph was customized to track water intake in **litres**, using a **float** type and a **"sora"** color theme.
3. **Logging Data**: A Python script was written to prompt the user for the daily water intake, which is then logged using a POST request to the Pixela API. This helps visualize hydration progress over time.

---

## Day 38: [Exercise Tracker Code(code/day-38)

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

## Day 39: [Flight Price Alert System](code/day-39-40)

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
