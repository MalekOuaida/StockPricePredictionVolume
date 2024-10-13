import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import sklearn.linear_model

stock_data = pd.read_csv('all_stocks_5yr.csv')

unique_stocks = stock_data['Name'].unique()
print("Available stocks:", ', '.join(unique_stocks))

selected_stock = input("Enter the stock symbol you want to analyze: ")

stock_data_filtered = stock_data[stock_data['Name'] == selected_stock]

if stock_data_filtered.empty:
    print(f"No data found for stock: {selected_stock}")
else:
    X = np.c_[stock_data_filtered['volume']]
    y = np.c_[stock_data_filtered['close']]

    stock_data_filtered.plot(kind='scatter', x='volume', y='close')
    plt.xlabel("Volume")
    plt.ylabel("Close Price")
    plt.title(f"Volume vs. Close Price for {selected_stock}")
    plt.show()

    model = sklearn.linear_model.LinearRegression()
    model.fit(X, y)

    try:
        user_volume = float(input("Enter the volume you want to predict the close price for: "))

        X_new = [[user_volume]]
        predicted_close_price = model.predict(X_new)

        print(f"Predicted Close Price for {selected_stock} with {user_volume} volume: {predicted_close_price[0][0]}")
    except ValueError:
        print(f"Invalid volume entered. Please enter a numerical value.")