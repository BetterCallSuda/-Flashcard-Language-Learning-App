# -Flashcard-Language-Learning-App
A simple Python–Tkinter flashcard app for learning vocabulary. Automatically flips cards, tracks words you learn, and saves progress. Built with Malayalam words, but fully customizable for any language pair by editing the CSV files.
-------------------------------------------------
🔥 Features :-
🃏 Auto-flipping flashcards (front → back)
✏️ Easily customizable for any language
📁 Saves your progress in words_to_learn.csv
✔️ Marks words you know
🔄 Only shows the remaining words until mastery

------------------------------------------------

💡 Clean UI built with Tkinter:-
🗂 Uses CSV files for easy editing and expansion
🛠 Tech Stack
Python
Tkinter (UI)
Pandas (CSV handling)
PhotoImage for card graphics
---------------------------------------------

📂 Project Structure
project/
│
├── data/
│   ├── Malu-EN.csv
│   └── words_to_learn.csv
│
├── images/
│   ├── card_front.png
│   ├── card_back.png
│   ├── right.png
│   └── wrong.png
│
└── main.py

---------------------------------------------------

📄 How It Works :-

Loads vocabulary from words_to_learn.csv
If not found, it uses the fallback CSV (Malu-EN.csv)
Shows the first language (e.g., Malayalam)
After 3 seconds, it automatically flips to the translation
If you know the word → ✔ removes it from the learning list
If you don’t know → ❌ keeps it in rotation
Saves progress automatically

🌍 Use for Any Language
You can convert this flashcard app for any language

---------------------------------Thank you-------------------------------------------
