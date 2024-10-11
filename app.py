from flask import Flask, render_template, request
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from keras.models import load_model
from sklearn.preprocessing import MinMaxScaler
import yfinance as yf
import io
import base64

app = Flask(__name__)

# Load the pre-trained LSTM model
model = load_model('model/stock_price_model.h5')

# Initialize the MinMaxScaler
scaler = MinMaxScaler(feature_range=(0, 1))

def fetch_data(stock_symbol):
    """Fetch historical stock data for the given symbol."""
    stock_data = yf.download(stock_symbol, start='2010-01-01', end=pd.Timestamp.today().strftime('%Y-%m-%d'))
    return stock_data

def fetch_live_price(stock_symbol):
    """Fetch the current stock price for the given symbol."""
    live_data = yf.Ticker(stock_symbol)
    current_price = live_data.history(period='1d')
    return current_price['Close'].iloc[0]

def preprocess_data(stock_data):
    """Preprocess the stock data for model prediction."""
    data = stock_data[['Open', 'Close']]
    scaled_data = scaler.fit_transform(data)  # Fit scaler and transform data
    return scaled_data

def generate_graph(x_data, y_data_list, title, xlabel, ylabel, labels, colors):
    """Generate a graph and return it as a base64 encoded string."""
    img = io.BytesIO()
    plt.figure(figsize=(10, 5))
    for y_data, label, color in zip(y_data_list, labels, colors):
        plt.plot(x_data, y_data, label=label, color=color)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.legend()
    plt.xticks(rotation=45)  # Rotate x-axis labels for better visibility
    plt.tight_layout()  # Adjust layout to prevent clipping of tick-labels
    plt.savefig(img, format='png')
    img.seek(0)
    return base64.b64encode(img.getvalue()).decode()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    stock_symbol = request.form['symbol']
    
    # Fetch the latest stock data
    stock_data = fetch_data(stock_symbol)
    
    if stock_data.empty:
        return render_template('prediction.html', error='Invalid stock symbol or no data available')

    # Preprocess data
    scaled_data = preprocess_data(stock_data)

    # Get the last 60 days of data for prediction
    last_60_days = scaled_data[-60:]
    last_60_days = np.reshape(last_60_days, (1, last_60_days.shape[0], last_60_days.shape[1]))

    # Make prediction for next day's open and close prices
    predicted_scaled = model.predict(last_60_days)
    predicted_prices = scaler.inverse_transform(predicted_scaled)

    next_day_open_price = predicted_prices[0, 0]
    next_day_close_price = predicted_prices[0, 1]

    # Render prediction.html with predicted values
    return render_template('predict.html', 
                           stock_symbol=stock_symbol.upper(),
                           next_day_open=next_day_open_price, 
                           next_day_close=next_day_close_price)

@app.route('/today_price', methods=['POST'])
def today_price():
    stock_symbol = request.form['symbol']
    
    # Fetch today's stock price
    today_data = fetch_data(stock_symbol)
    
    if today_data.empty:
        return render_template('today.html', error='No data available for today.')

    today_open_price = today_data['Open'].iloc[0]
    today_close_price = today_data['Close'].iloc[-1]

    # Fetch the live price
    live_price = fetch_live_price(stock_symbol)

    # Generate chart for today's close prices
    close_chart_url = generate_graph(
        today_data.index, [today_data['Close']],
        title=f"{stock_symbol} - Today's Close Price History",
        xlabel="Time", ylabel="Close Price",
        labels=["Close Price"], colors=['blue']
    )

    # Generate chart for opening and closing prices for the past 30 days
    past_30_days = today_data.tail(30)
    open_close_chart_url = generate_graph(
        past_30_days.index, [past_30_days['Open'], past_30_days['Close']],
        title=f"{stock_symbol} - Opening and Closing Prices (Last 30 Days)",
        xlabel="Date", ylabel="Price",
        labels=["Opening Price", "Closing Price"], colors=['green', 'red']
    )

    return render_template('today.html', 
                           stock_symbol=stock_symbol,
                           today_open=today_open_price,
                           today_close=today_close_price,
                           live_price=live_price,
                           close_chart_url=close_chart_url,
                           open_close_chart_url=open_close_chart_url)

@app.route('/historical', methods=['POST'])
def historical():
    stock_symbol = request.form['symbol']
    start_date = request.form['start_date']
    end_date = request.form['end_date']
    
    # Validate the dates
    if start_date >= end_date:
        return render_template('historical.html', error='Start date must be before end date.')

    # Fetch historical data for the given stock symbol and date range
    historical_data = yf.download(stock_symbol, start=start_date, end=end_date)
    
    if historical_data.empty:
        return render_template('historical.html', error='No data available for the given date range.')

    # Generate chart for historical closing and opening prices
    historical_chart_url = generate_graph(
        historical_data.index, 
        [historical_data['Close'], historical_data['Open']],  # Added 'Open' price here
        title=f"{stock_symbol} - Historical Open and Close Prices ({start_date} to {end_date})",
        xlabel="Date", 
        ylabel="Price",
        labels=["Closing Price", "Opening Price"],  # Updated labels for both lines
        colors=['red', 'green']  # Different colors for each line
    )

    return render_template('historical.html', 
                           stock_symbol=stock_symbol.upper(),
                           start_date=start_date,
                           end_date=end_date,
                           historical_chart_url=historical_chart_url)

if __name__ == '__main__':
    app.run(debug=True) 