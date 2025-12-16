# Secure Password Generator
A robust and user-friendly Password Generator built using Python. This project demonstrates random string manipulation, GUI development with Tkinter, and clipboard integration to create secure passwords easily.

![alt text](<Image.jpeg>)

# 📌 Features
1. **Customizable Length:** Users can define the exact length of the password (minimum 8 characters).

2. **Character Set Selection:** Toggle options for Uppercase, Lowercase, Numbers, and Symbols.

3. **Guaranteed Complexity:** Logic ensures at least one character from every selected category is included.

4. **Clipboard Integration:** One-click button to copy the generated password immediately.

5. **Input Validation:** Prevents weak passwords by enforcing length constraints and numeric inputs.

6. **Error Handling:** Displays user-friendly error messages for invalid inputs.

7. **Clean GUI:** Simple and intuitive interface built with Tkinter.

# Project Structure
```text
Password-Generator
├─ main.py       # Main application script
└─ README.md     # Documentation
```

# 🔐 Generation Logic
1. The generator ensures high entropy and randomness using the following steps:

2. Pool Creation: A character pool is built based on user selection (A-Z, a-z, 0-9, special chars).

3. Mandatory Inclusion: To ensure complexity, the script first forcibly selects one random character from each checked category.

4. Filling: The remaining length is filled with random choices from the combined pool.

5. Shuffling: The resulting list of characters is shuffled using random.shuffle() to prevent predictable patterns.

# ⚙️ Setup Instructions
Follow these steps to set up and run the project locally.

**1. Clone the Repository**
```text
git clone https://github.com/nishankkhadpe7-afk/Random-Password-Generator.git
cd RandomPasswordGenerator
```

**2. Environment Setup**

This project relies entirely on Python's Standard Library, so no external package installation is required. However, using a virtual environment is good practice.
```text
python -m venv venv
```

Activate the environment:

* **Windows**:
```text
venv\Scripts\activate
```

* **Linux / macOS**:
```text
source venv/bin/activate
```

**3. Run the Application**
```text
python main.py
```

(Note: Ensure your script file is named main.py or adjust the command accordingly).

# 🛠 Technologies Used

* **Python 3.x**: Core programming language.

* **Tkinter**: Standard Python interface to the Tcl/Tk GUI toolkit.

* **Random**: Implements pseudo-random number generators for distributions.

* **String**: Provides constants for ASCII character sets.

# 🚀 Learning Outcomes

By working with this project, you will gain experience in:

* **GUI Development**: Managing layouts (Grid geometry manager) and widgets (Labels, Entries, Checkbuttons).

* **Event-Driven Programming**: Binding button clicks to specific functions.

* **Data Security Logic**: Implementing constraints to ensure passwords meet complexity requirements.

* **Input Sanitization**: Using try-except blocks to handle user input errors.

* **System Interaction**: Interfacing with the OS clipboard.
