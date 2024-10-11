
---

# 📈 Stock Price Prediction Web Application 🚀

![Screenshot 2024-10-11 183441](https://github.com/user-attachments/assets/8adffb5f-6af7-4a49-9c2f-defb43db2890)
![Screenshot (63)](https://github.com/user-attachments/assets/6c1debc4-019c-48c2-87e3-96fd7d4c1405)
![Screenshot 2024-10-11 183417](https://github.com/user-attachments/assets/ecaff7b0-6a13-4ac9-8231-9d6235db469b)

## 🌟 Overview

Welcome to the **Stock Price Prediction Web Application**! This powerful platform uses **Long Short-Term Memory (LSTM)** networks to accurately predict stock prices based on historical data. With real-time updates and insightful analytics, this app is perfect for traders and investors looking to enhance their decision-making. 💹

---

## 🛠️ Features

- **🔮 Predict Next Day's Stock Price**: Enter a stock symbol to receive predictions for the next day’s opening and closing prices. Perfect for planning your trades! 📅

- **📈 See Live Prices**: Access live stock prices during market hours, providing both actual and predicted values to inform your trading strategy. 💵

- **📚 Historical Stock Price Data**: Retrieve and analyze historical stock price data for specific symbols and date ranges to uncover trends and patterns. 📊



- **🎨 User-Friendly Interface**: Enjoy an attractive frontend with easy navigation, designed for a seamless user experience. ✨

---

## 📥 Getting Started

### ⚙️ Prerequisites

Before you begin, ensure you have the following installed:
- **Python 3.10 or higher** 🐍
- **Flask** 🌐
- **yfinance** 📈
- **TensorFlow** 🧠
- **Pandas** 🐼
- **Numpy** ➗

### 🏗️ Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/shreyai347/stock-price-prediction.git
   ```
2. **Navigate to the project directory**:
   ```bash
   cd stock-price-prediction
   ```
3. **Install the required packages**:
   ```bash
   pip install -r requirements.txt
   ```
4. **Run the Flask application**:
   ```bash
   python app.py
   ```
5. **Open your web browser** and go to `http://127.0.0.1:5000` to start exploring! 🌐

---

## 📂 Project Structure

Here's a detailed look at the project structure:

```
your_project/
│
├── app.py                       # Main application file to run the Flask web server 🚀
├── model/
│   └── stock_price_model.h5     # Pre-trained LSTM model for stock price predictions 🔮
├── templates/
│   ├── index.html               # Homepage template with navigation options 🏠
│   ├── predict.html             # Template to display prediction results for selected stocks 📊
│   ├── today.html               # Template for showing today's stock prices and related information 📈
│   └── historical.html          # Template for analyzing historical stock data and trends 📚
└── static/
    ├── style_index.css          # CSS styles for the homepage layout and design 🎨
    ├── style_today.css          # CSS styles for today's stock prices display 📅
    ├── style_predict.css         # CSS styles for the prediction results page 🔍
    └── style_hist.css            # CSS styles for the historical data analysis page 📜
```

---

## 📝 Usage

1. **🔮 Predict Next Day Price**: Click the "Predict Next Day Price" button, enter the stock symbol, and receive predictions for tomorrow's prices! 📈
   
2. **📈 See Live Prices**: Enter the stock symbol in the "See Live Prices" section to view real-time updates during market hours. 💵
   
3. **📚 Historical Stock Price Data**: Provide the stock symbol and desired date range to fetch historical stock data, enabling you to make informed investment decisions. 📊

---

## ⏰ Important Note

- **Required Libraries**: Ensure you have all the necessary libraries installed as listed in `requirements.txt`. This includes packages such as Flask, yfinance, TensorFlow, and others needed for the application to function correctly. 📚

- **No Market Open/Close Handling**: The application does not handle specific market open and close times, but it provides real-time updates and predictions regardless of market hours. You can use the app to analyze and predict stock prices at any time! 🕒

---

## 📬 Contact

For inquiries, feedback, or collaboration opportunities, feel free to reach out:
- **📧 Email**: shreyashreya2322@gmail.com
- **💼 LinkedIn**: [Shreya Nagarbawdi](https://www.linkedin.com/in/shreya-nagarbawdi)

---

## 🤝 Contributing

We welcome contributions! If you have suggestions or improvements, please open an issue or submit a pull request. Let’s make this project even better together! 🌟

---

## 📜 License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for more details. 📝

---

Feel free to adjust any sections to fit your personal touch for project!
