[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/AHFn7Vbn)
# Superjoin Hiring Assignment

### Welcome to Superjoin's hiring assignment! 🚀

### Objective
Build a solution that enables real-time synchronization of data between a Google Sheet and a specified database (e.g., MySQL, PostgreSQL). The solution should detect changes in the Google Sheet and update the database accordingly, and vice versa.

### Problem Statement
Many businesses use Google Sheets for collaborative data management and databases for more robust and scalable data storage. However, keeping the data synchronised between Google Sheets and databases is often a manual and error-prone process. Your task is to develop a solution that automates this synchronisation, ensuring that changes in one are reflected in the other in real-time.

### Requirements:
1. Real-time Synchronisation
  - Implement a system that detects changes in Google Sheets and updates the database accordingly.
   - Similarly, detect changes in the database and update the Google Sheet.
  2.	CRUD Operations
   - Ensure the system supports Create, Read, Update, and Delete operations for both Google Sheets and the database.
   - Maintain data consistency across both platforms.
   
### Optional Challenges (This is not mandatory):
1. Conflict Handling
- Develop a strategy to handle conflicts that may arise when changes are made simultaneously in both Google Sheets and the database.
- Provide options for conflict resolution (e.g., last write wins, user-defined rules).
    
2. Scalability: 	
- Ensure the solution can handle large datasets and high-frequency updates without performance degradation.
- Optimize for scalability and efficiency.

## Submission ⏰
The timeline for this submission is: **Next 2 days**

Some things you might want to take care of:
- Make use of git and commit your steps!
- Use good coding practices.
- Write beautiful and readable code. Well-written code is nothing less than a work of art.
- Use semantic variable naming.
- Your code should be organized well in files and folders which is easy to figure out.
- If there is something happening in your code that is not very intuitive, add some comments.
- Add to this README at the bottom explaining your approach (brownie points 😋)
- Use ChatGPT4o/o1/Github Co-pilot, anything that accelerates how you work 💪🏽. 

Make sure you finish the assignment a little earlier than this so you have time to make any final changes.

Once you're done, make sure you **record a video** showing your project working. The video should **NOT** be longer than 120 seconds. While you record the video, tell us about your biggest blocker, and how you overcame it! Don't be shy, talk us through, we'd love that.

We have a checklist at the bottom of this README file, which you should update as your progress with your assignment. It will help us evaluate your project.

- [x] My code's working just fine! 🥳
- [ ] I have recorded a video showing it working and embedded it in the README ▶️
- [x] I have tested all the normal working cases 😎
- [ ] I have even solved some edge cases (brownie points) 💪
- [x] I added my very planned-out approach to the problem at the end of this README 📜

## Got Questions❓
Feel free to check the discussions tab, you might get some help there. Check out that tab before reaching out to us. Also, did you know, the internet is a great place to explore? 😛

We're available at techhiring@superjoin.ai for all queries. 

All the best ✨.

## Developer's Section
*Add your video here, and your approach to the problem (optional). Leave some comments for us here if you want, we will be reading this :)*

## Project Approach and Functions

## Project Approach
In this project, I implemented a real-time synchronization system between Google Sheets and SQLite using Streamlit, enabling seamless data flow and ensuring consistency across both platforms. By utilizing the Google Sheets API and SQLite database, I created a solution that detects changes in either platform and updates the other accordingly, using hash-based change detection. I integrated CRUD operations to manage data across both systems and designed a periodic monitoring process to automate updates every 10 seconds. This project deepened my understanding of API integration, database synchronization, and real-time data management within web applications.

##Functions
- connect_to_db(): Creates and returns a connection to the SQLite database.
- create_table(): Creates a table in the SQLite database if it doesn't already exist.
- get_sheet_data(): Retrieves all data from Google Sheets using the get_all_values() method.
- hash_data(data): Generates a hash value of the current data in the sheet.
- sync_google_sheets_to_sqlite(data): Syncs data from Google Sheets to the SQLite database.
- batch_sync_sqlite_to_google_sheets(batch_size=100): Syncs data from SQLite back to Google Sheets in batches.

Streamlit App Functions
- update_data(): Checks for changes in Google Sheets by comparing the current data hash with the stored hash.

Monitoring Changes
The app allows users to start and stop monitoring changes with buttons. Once monitoring is started, the app checks for changes every 10 seconds and syncs accordingly.
Buttons in Streamlit UI

- Start/Stop Monitoring Changes: Starts or stops periodic monitoring of data changes in Google Sheets.
- Show Table Data: Displays the current data stored in the SQLite database in a table format within the app.

## Project Features

The system is designed to meet the following requirements:

### 1. Real-time Synchronization

- Google Sheets → SQLite: Detects changes in Google Sheets and updates the SQLite database accordingly.
- SQLite → Google Sheets: Detects changes in the SQLite database and updates Google Sheets.
- The system performs these checks periodically to keep both data sources in sync.

### 2. CRUD Operations

- The system allows for the creation, reading, updating, and deleting of records in both Google Sheets and SQLite database.
- Data is kept consistent between the two systems to ensure that changes in one are reflected in the other.

###How to Run the Project

Place the credentials.json file (downloaded from Google Cloud) in the root folder.
Run the Streamlit app by executing the following command:

streamlit run app.py

