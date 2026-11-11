Hand Gesture Controlled Book Database

A Python project that combines hand gesture recognition, web scraping, and database management.

The project uses your webcam to recognize hand gestures and displays book information stored in an SQLite database according to the number of fingers detected.

Features
Detects hand landmarks using MediaPipe.
Counts raised fingers using hand landmark positions.
Uses OpenCV to capture and process webcam frames.
Scrapes book information from Books to Scrape.
Stores book names, prices, and image URLs in an SQLite database.
Displays database information based on detected hand gestures.
Gesture Controls
Gesture	Action
☝️ 1 Finger	Displays information about the first book.
✌️ 2 Fingers	Displays information about the first two books.
🖐️ 5 Fingers	Displays information about all books.
Libraries

This project uses the following Python libraries:

opencv-python – Webcam access and image processing.
mediapipe – Hand detection and landmark recognition.
SQLAlchemy – Database management.
requests – Sending HTTP requests to websites.
beautifulsoup4 – Extracting book information from HTML.
sqlite3 – Local database storage (through SQLAlchemy).
Installation

Install the required libraries:

bash
pip install opencv-python mediapipe sqlalchemy requests beautifulsoup4

Project Structure
text
Project/
│
├── main.py
├── database.py
└── Bookdata.db

main.py: Handles webcam access, hand detection, finger counting, and gesture recognition.
database.py: Creates the database, scrapes book information, stores records, and prints information based on the selected mode.
Bookdata.db: SQLite database containing scraped book information. It is created automatically.
Usage
1. Scrape Book Information

Run the database file:

bash
python database.py


The program visits Books to Scrape, extracts book names, prices, and image URLs from the first page, and stores them in the SQLite database.

2. Run Hand Gesture Recognition

Run the main file:

bash
python main.py


Allow access to your webcam and show your hand in front of the camera.

The program detects your fingers and calls the info_print() function with the corresponding mode.

3. Exit

Press Q to close the webcam window and terminate the program.

Database Model

The database contains a table called booksinfo with the following columns:

Column	Description
id	Primary key
name	Name of the book (unique)
price	Price of the book
image	URL of the book cover (unique)
Requirements
Python 3.x
A working webcam
Internet connection for web scraping
Required Python libraries installed
Author

Developed as a personal Python project to practice computer vision, hand gesture recognition, web scraping, and SQL database management.
