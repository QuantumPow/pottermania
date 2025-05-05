# 🧙 Pottermania Quiz Bot

A magical chatbot quiz powered by [Rasa](https://rasa.com/), designed to test your knowledge of the wizarding world of Harry Potter. Get ready to answer five enchanted questions ranging from spells to potions!

---

## 📋 Prerequisites

Before getting started, make sure you have the following tools installed on your system:

* **Python 3.9** – Recommended version for compatibility. Check your version by running:

  * Windows: `python --version`
  * macOS/Linux: `python3 --version`

    > ⚠️ Make sure `python` refers to Python 3.9. If you have multiple versions installed, consider using `py -3.9` (Windows) or specifying `python3.9` explicitly on macOS/Linux.

* **Git** – To clone the repository. Verify installation with:

  ```bash
  git --version
  ```

* **Internet connection** – Required for downloading dependencies.

It is also recommended to have a Python-friendly text editor or IDE like **VS Code** or **PyCharm** to explore or modify the code if needed.

---

## 🛠️ Installation Guide

Follow these steps to set up the project on your local machine:

### 1. Clone the repository

Using HTTPS:

```bash
git clone https://github.com/yourusername/pottermania.git
```

Then enter the project directory:

```bash
cd pottermania
```

### 2. Create a Virtual Environment with Python 3.9

To ensure compatibility and isolate dependencies, it's important to use Python 3.9 to create a virtual environment:

* **Windows:**

  ```bash
  python -m venv venv
  .\venv\Scripts\activate
  ```
> ⚠️ If multiple Python versions are installed, you can try using `py -3.9 -m venv venv` to ensure the right version is used.

* **macOS/Linux:**

  ```bash
  python3.9 -m venv venv
  source venv/bin/activate
  ```

You should see `(venv)` or similar at the beginning of your terminal prompt when the environment is active.

> 💡 Remember to activate the virtual environment in every new terminal session where you plan to run the bot.

### 3. Install Dependencies

With the virtual environment activated, run:

```bash
pip install -r requirements.txt
```

> This will install Rasa and any additional libraries needed for the bot to run correctly.

Check that Rasa is installed:

```bash
rasa --version
```

You should see your Rasa and Python versions listed.

---

## 🚀 Getting Started

1. Train the model:

   ```bash
   rasa train
   ```

2. Run the chatbot in shell mode:

   ```bash
   rasa shell
   ```

3. Run the action server (if `action_check_quiz` is implemented in `actions.py`):

   ```bash
   rasa run actions
   ```

---

## 🧪 Features

* Collects the user's name and uses it in personalized interactions.
* Asks 5 quiz questions related to the Harry Potter universe:

  * Patronus charm
  * Luna Lovegood
  * Ollivanders wand shop
  * Golden Snitch
  * Polyjuice potion
* Supports a range of natural answers and even humorous or vague replies.
* Evaluates answers using custom action logic (see `actions.py`).

---

## 📂 Project Structure Overview

```
📁 pottermania
├── data/
│   └── nlu.yml         # Intent and entity training examples
├── domain.yml          # Intents, entities, slots, responses, actions
├── actions.py          # Custom actions like quiz evaluation
├── config.yml          # Pipeline and policies configuration
├── rules.yml           # Dialogue rules
├── stories.yml         # Conversation training stories
└── requirements.txt    # Python dependencies
```

---

## 🤖 Powered by

* [Rasa Open Source](https://rasa.com/)
* Python 3.9

---

Feel free to fork this repository or adapt it for your own magical chatbot ideas! ✨

