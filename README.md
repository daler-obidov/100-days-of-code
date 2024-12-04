# 100-Days-of-Code: Portfolio Projects

This section highlights the projects and code worked on during the **100 Days of Code** challenge.

---

| **Project Title**                      | **Technologies Used** | **Key Features**                                                                                         | **Outcome**                                                                                   | **Workflow**                                           |
|----------------------------------------|-----------------------|----------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------|-------------------------------------------------------|
| [Pomodoro Timer](code/day-28)          | Tkinter               | Countdown timer with work/break sessions                                                                  | Efficient time management using Pomodoro.                                                       | Timer logic, Tkinter UI, Start/Reset functionality.    |
| [Password Manager](code/day-29-30)     | Tkinter, JSON         | Strong password generation and secure storage                                                            | Secure password management with search functionality.                                          | Password gen, store in JSON, Tkinter UI, Search.      |
| [Flashcard Game](code/day-31)          | Tkinter, Pandas       | Korean vocabulary flashcards with automatic flip feature                                                  | Interactive flashcard game for vocabulary learning.                                            | Design flashcards, use Pandas, track answers.         |
| [Birthday Email System](code/day-32)   | CSV, smtplib          | Automated birthday emails from CSV data                                                                    | Sends personalized birthday emails.                                                            | Parse CSV, email gen, date matching.                 |
| [Kanye Quote Generator](code/day-33)   | Tkinter, Kanye API    | Displays random Kanye quotes with a button for new quotes                                                  | Fun quote generator with API integration.                                                     | API connection, Tkinter UI, random quote display.     |
| [Quiz Application](code/day-34-35)     | Tkinter, Python       | Multiple-choice quiz with score tracking                                                                  | Interactive quiz with score tracking.                                                           | Question structure, Tkinter UI, score tracking.       |
| [Stock Price Notifier](code/day-36)    | Alpha Vantage, Twilio | Tracks stock prices and sends SMS alerts for significant changes                                           | Real-time stock price alerts with news.                                                        | Fetch stock data, price change detection, SMS alerts. |
| [Water Intake Tracker](code/day-37)    | Pixela API            | Tracks daily water intake and visualizes progress                                                          | Visual progress tracking for hydration.                                                       | Connect Pixela, log data, display graph.             |
| [Exercise Tracker](code/day-38)        | Nutritionix API       | Logs exercise details and syncs with Google Sheets                                                         | Tracks and logs workouts efficiently.                                                          | Fetch exercise data, Google Sheets integration.       |
| [Flight Price Alert](code/day-39-40)   | Flight API, Twilio    | Tracks flight prices and sends SMS alerts when prices drop                                                | Notifies users of flight price drops.                                                          | Track flight prices, Google Sheets, SMS alerts.       |

## Day 28: [Pomodoro Timer](code/day-28)

### Description
On **Day 28**, I built a **Pomodoro Timer** application using **Tkinter** to help users manage their work and break intervals. The Pomodoro technique encourages working in focused intervals, followed by short breaks, enhancing productivity and maintaining focus. This app provides the following features:

### Key Features:
1. **Timer Functionality**:
   - The app uses a countdown timer that alternates between work and break sessions. Users can start and reset the timer with buttons.

2. **Work and Break Intervals**:
   - The app allows users to work for a set time (e.g., 1 minute) and take a short break after each work session. Every 4 work intervals, users get a longer break.

3. **Visual Indicators**:
   - A visual representation of the timer is displayed on the screen, and the app shows checkmarks after each work session to track progress.

4. **User Interface**:
   - The app’s interface is created with **Tkinter**, featuring a central timer display and buttons for starting and resetting the timer. The background changes color depending on the current phase (work or break).

### Workflow:
1. **Start Timer**: Clicking the "Start" button begins the countdown, alternating between work and break intervals.
2. **Reset Timer**: Clicking the "Reset" button resets the timer to the initial state, allowing users to start over.
3. **Track Progress**: Checkmarks are displayed after each completed work session, providing a visual progress indicator.

### Outcome:
- This app helps users manage their time efficiently, promoting productivity and regular breaks. It provides a simple and effective tool for implementing the Pomodoro technique.


## Day 30: [Password Manager](code/day-29-30)

### Description
On **Day 30**, I built a **Password Manager** using **Tkinter** to create a simple graphical interface. This app allows users to store and manage their website credentials (username/email and password). The app provides the following features:

### Key Features:
1. **Password Generation**:
   - The app has a password generator that creates strong, random passwords consisting of letters, symbols, and numbers. Users can easily copy the generated password to their clipboard.

2. **Saving Credentials**:
   - Users can store their website, email/username, and password in a JSON file. If the fields are empty, the app shows a warning message.

3. **Search for Credentials**:
   - Users can search for a saved website by entering the website's name. If the website is found, the app displays the corresponding email/username and password.

4. **User Interface**:
   - The app's interface is created with **Tkinter**, which includes entry fields for the website, email, and password, as well as buttons for generating passwords, saving, and searching.

### Workflow:
1. **Generate Password**: Clicking the "Generate Password" button creates a random password and copies it to the clipboard.
2. **Save Password**: Enter the website, email, and password, then click "Add" to save the data to a JSON file.
3. **Search for Password**: Enter a website name and click "Search" to retrieve the credentials from the saved data.

### Outcome:
- This app provides a convenient way to manage and retrieve passwords securely. It allows for efficient password generation and retrieval for different websites.



## Day 31: [Flashcard Game with Tkinter](code/day-31)

### Description
On **Day 31**, I built a **Flashcard Game** using the **Tkinter** library. This game helps users learn Korean words and their English translations by displaying them as flashcards. The user can click buttons to mark whether they have answered correctly or incorrectly, and the game proceeds to the next card.

### Key Features:
1. **Flashcard Display**:
   - The app uses Tkinter’s `Canvas` widget to display flashcards. Each card shows a word in either Korean or English and flips after 5 seconds to display the translation.

2. **Data Handling**:
   - The app loads a CSV file (`words.csv`) containing a list of words in both Korean and English using **Pandas**. The words are then converted into a dictionary for easy access.

3. **Timer for Card Flip**:
   - After displaying the Korean word, the app automatically flips the card after 5 seconds to show the English translation, giving the user time to recall the word.

4. **User Interaction**:
   - The user can click on buttons to mark whether they got the answer right or wrong. The game will then show a new flashcard.

### Workflow:
1. The app loads a CSV file containing Korean and English words.
2. It displays a random Korean word on the screen.
3. After 5 seconds, the word flips to show the English translation.
4. The user clicks "right" or "wrong" to move to the next card.

### Outcome:
- The app helps users learn vocabulary through interactive flashcards. The integration of a timer and random word selection makes it an effective study tool.



## Day 32: [Automated Birthday Email System](code/day-32)

### Description
On **Day 32**, I built an **Automated Birthday Email System** that sends personalized birthday emails. The system checks if today's date matches someone's birthday from a CSV file, selects a random birthday message template, personalizes it, and sends the email.

### Key Features:
1. **Birthday Data Loading**:
   - The system loads birthday data from a CSV file (`birthdays.csv`), containing names, birthdays, and emails.
   - The data is converted into a dictionary where the key is a tuple of the month and day, and the value is the person's details (name, email).

2. **Check for Today's Birthday**:
   - The system checks if today's date matches any of the birthdays in the loaded dictionary.

3. **Personalized Letter Selection**:
   - If it's someone's birthday, a random birthday letter (from 3 available templates) is selected.
   - The letter is personalized by replacing `[NAME]` with the birthday person's name.

4. **Sending Email**:
   - The script connects to Gmail's SMTP server using `smtplib` and sends a personalized birthday email to the person using their email address from the CSV file.

### Workflow:
1. The script loads the birthday data from `birthdays.csv`.
2. It checks if today's date matches any birthday.
3. If it matches, a random letter template is selected, personalized with the name, and sent to the person’s email.

### Outcome:
- This system automates the process of sending personalized birthday emails, making it easier to wish people on their special day.


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
