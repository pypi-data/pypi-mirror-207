import pandas as pd
import numpy as np
import yfinance as yf
import matplotlib.pyplot as plt
import seaborn as sns
import math
import os

# Funciones para realizar solo el análisis finaniero
def stock_price_close(stock_list, start = '2022-01-01', end = '2023-01-01'):
    stock_dataframe = pd.DataFrame()
    for stock in stock_list:
        data = yf.download(stock, start = start, end = end, progress = False)
        stock_dataframe[stock] = data["Close"]
    return stock_dataframe

def get_name_columns(stock_list, start = '2022-01-01', end = '2023-01-01'):
    stock_dataframe = pd.DataFrame()
    for stock in stock_list:
        data = yf.download(stock, start = start, end = end, progress = False)
        stock_dataframe[stock] = data["Close"]
    columnas = ", ".join(stock_dataframe.columns)
    return columnas

def get_date_start(stock_list, start = '2022-01-01', end = '2023-01-01'):
    stock_dataframe = pd.DataFrame()
    for stock in stock_list:
        data = yf.download(stock, start = start, end = end, progress = False)
        stock_dataframe[stock] = data["Close"]
    start = stock_dataframe.index[0].strftime(format = "%Y-%m-%d")
    return start

def get_date_end(stock_list, start = '2022-01-01', end = '2023-01-01'):
    stock_dataframe = pd.DataFrame()
    for stock in stock_list:
        data = yf.download(stock, start = start, end = end, progress = False)
        stock_dataframe[stock] = data["Close"]
    end = start = stock_dataframe.index[-1].strftime(format = "%Y-%m-%d")
    return end

def return_daily(list_stock, start = '2022-01-01', end = '2023-01-01'):
    stocks = stock_price_close(list_stock, start = start, end = end)
    log_returns = np.log(stocks / stocks.shift(1))
    log_returns = log_returns.dropna()
    return log_returns

def covariance_matrix(list_stock, start = '2022-01-01', end = '2023-01-01'):
    returns_data = return_daily(list_stock, start = start, end = end)
    covmatrix = returns_data.cov()
    return covmatrix

def return_positive_negative(value):
    value = float(value)
    if value < 0:
        return 'pérdida'
    elif value >= 0:
        return 'ganancia'

# Funciones para graficar el análisis financiero
def plot_stock_price_close(func):
    def wrapper(*args, **kwargs):
        stock_dataframe = func(*args, **kwargs)
        proyect_directory = os.getcwd()
        plots_directory = os.path.join(proyect_directory, "plots")
        os.makedirs(plots_directory, exist_ok=True)
        image_file_name = 'precios_cierre.png'
        image_file_path = os.path.join(plots_directory, image_file_name)
        orange_color = sns.color_palette("YlOrBr", as_cmap = False, n_colors=5)
        sns.set_palette(orange_color)
        fig, ax = plt.subplots(figsize = (8,6), dpi = 80)
        stock_dataframe.plot(ax = ax)
        plt.legend()
        plt.title("Evolución del precio de cierre de las acciones", size = 15)
        plt.xlabel("Fecha")
        plt.ylabel("Precio de las acciones")
        for i in ['bottom', 'left']:
            ax.spines[i].set_color('black')
            ax.spines[i].set_linewidth(1.5) 
        right_side = ax.spines["right"]
        right_side.set_visible(False)
        top_side = ax.spines["top"]
        top_side.set_visible(False)
        ax.set_axisbelow(True)
        ax.grid(color='gray', linewidth=1, axis='y', alpha=0.4)
        plt.savefig(image_file_path)
        plt.close()
    return wrapper

@plot_stock_price_close
def get_stock_price_close(stock_list, start = '2022-01-01', end = '2023-01-01'):
    stock_dataframe = pd.DataFrame()
    for stock in stock_list:
        data = yf.download(stock, start = start, end = end, progress = False)
        stock_dataframe[stock] = data["Close"]
    return stock_dataframe


def histogram_stock_returns(list_stocks, start = '2022-01-01', end = '2023-01-01'):
    proyect_directory = os.getcwd()
    plots_directory = os.path.join(proyect_directory, "plots")
    os.makedirs(plots_directory, exist_ok=True)
    image_file_name = 'precios_histograma.png'
    image_file_path = os.path.join(plots_directory, image_file_name)
    return_stock = return_daily(list_stock = list_stocks, start = start, end = end)
    red_color = sns.cubehelix_palette(start=2,rot=0, dark=0, light=.95)
    sns.set_palette(red_color)
    fig, ax = plt.subplots(figsize = (8,6), dpi = 80)
    for i in return_stock.columns.values:
        plt.hist(return_stock[i], label = i, bins = 100)
    plt.legend()
    for i in ['bottom', 'left']:
            ax.spines[i].set_color('black')
            ax.spines[i].set_linewidth(1.5) 
    right_side = ax.spines["right"]
    right_side.set_visible(False)
    top_side = ax.spines["top"]
    top_side.set_visible(False)
    ax.set_axisbelow(True)
    ax.grid(color='gray', linewidth=1, axis='y', alpha=0.4)
    plt.title(f"Histograma del rendimiento\nlogarítmico de las acciones", size = 15)
    plt.xlabel("Rendimiento")
    plt.ylabel("Frecuencia")
    plt.savefig(image_file_path)
    plt.close()


def return_log_mean_and_standard_deviation(list_stocks, start = '2022-01-01', end = '2023-01-01'):
    proyect_directory = os.getcwd()
    plots_directory = os.path.join(proyect_directory, "plots")
    os.makedirs(plots_directory, exist_ok=True)
    image_file_name = 'rendimiento_volatilidad_anualizada.png'
    image_file_path = os.path.join(plots_directory, image_file_name)
    return_stock = pd.DataFrame(return_daily(list_stock = list_stocks, start = start, end = end).mean()).rename(columns = {
        0:'Rendimiento promedio anualizado %'
    }).reset_index()
    return_stock = return_stock.rename(columns = {'index':"Acción"})
    return_stock["Rendimiento promedio anualizado %"] = return_stock["Rendimiento promedio anualizado %"]
    std_stock = pd.DataFrame(return_daily(list_stock = list_stocks, start = start, end = end).var()).rename(columns = {
        0:'Desviación estándar %'
    }).reset_index()
    std_stock = std_stock.rename(columns = {'index':'Acción'})
    df = pd.merge(return_stock, std_stock, on = "Acción", how = 'left')
    df = df.set_index("Acción")
    df["Rendimiento promedio anualizado %"] = df["Rendimiento promedio anualizado %"] * 252 * 100
    df["Desviación estándar %"] = df["Desviación estándar %"] * 252
    df["Desviación estándar anualizada %"] = df["Desviación estándar %"].apply(lambda x : math.sqrt(x)*100)
    
    fig, ax1 = plt.subplots(figsize = (8,6), dpi = 80)
    ax1.bar(df.index, df["Rendimiento promedio anualizado %"], color = 'tab:blue', alpha = 0.8)
    ax1.set_ylabel('Rendimiento promedio %')
    ax2 = ax1.twinx()
    ax2.plot(df.index, df["Desviación estándar anualizada %"],linewidth = 4, color = 'tab:orange', alpha = 0.8)
    ax2.set_ylabel('Desviación estándar %')
    
    for i in ['bottom', 'left']:
        ax2.spines[i].set_color('black')
        ax2.spines[i].set_linewidth(1.5) 
    right_side = ax2.spines["right"]
    right_side.set_visible(False)
    top_side = ax2.spines["top"]
    top_side.set_visible(False)
    ax2.set_axisbelow(True)
    ax2.grid(color='gray', linewidth=1, axis='y', alpha=0.4)
    plt.title(f'Rendimiento promedio y volatilidad anualizada\nde las acciones', size = 15)
    plt.savefig(image_file_path)
    plt.close()
    
    
def plot_covariance_matrix(list_stock, start = '2022-01-01', end = '2023-01-01'):
    proyect_directory = os.getcwd()
    plots_directory = os.path.join(proyect_directory, "plots")
    os.makedirs(plots_directory, exist_ok=True)
    image_file_name = 'variaza_covarianza.png'
    image_file_path = os.path.join(plots_directory, image_file_name)
    covmatrix = covariance_matrix(list_stock, start = start, end = end)
    fig, ax = plt.subplots(figsize = (15,8), dpi = 80)
    plt.title("Matriz de varianza y covarianza", size = 15)
    ax = sns.heatmap(covmatrix, cmap = 'Blues', annot = True)
    plt.savefig(image_file_path)
    plt.close()
    

def plot_correlation_matrix(list_stock, start = '2022-01-01', end = '2023-01-01'):
    proyect_directory = os.getcwd()
    plots_directory = os.path.join(proyect_directory, "plots")
    os.makedirs(plots_directory, exist_ok=True)
    image_file_name = 'matriz_correlacion.png'
    image_file_path = os.path.join(plots_directory, image_file_name)
    return_stock = return_daily(list_stock, start = start, end = end)
    fig, ax = plt.subplots(figsize = (15,8), dpi = 80)
    ax = sns.heatmap(data = return_stock.corr(), annot = True, cmap = 'YlGnBu')
    plt.title("Matriz de Correlación", size = 15)
    plt.savefig(image_file_path)
    plt.close()
    

def plot_return_log(list_stock, start = '2022-01-01', end = '2023-01-01'):
    proyect_directory = os.getcwd()
    plots_directory = os.path.join(proyect_directory, "plots")
    os.makedirs(plots_directory, exist_ok=True)
    image_file_name = 'rendimiento_log.png'
    image_file_path = os.path.join(plots_directory, image_file_name)
    return_stocks = return_daily(list_stock = list_stock, start = start, end = end)
    dark_color = sns.dark_palette("#69d", reverse = True, as_cmap = False, n_colors=5)
    sns.set_palette(dark_color)
    fig, ax = plt.subplots(figsize = (8,6), dpi = 80)
    return_stocks.plot(ax = ax)
    plt.xlabel("Fecha")
    plt.ylabel("Rendimiento logarítmico")
    plt.title("Evolución del rendimiemto logarítmico de las acciones", size = 15)
    for i in ['bottom', 'left']:
        ax.spines[i].set_color('black')
        ax.spines[i].set_linewidth(1.5) 
    right_side = ax.spines["right"]
    right_side.set_visible(False)
    top_side = ax.spines["top"]
    top_side.set_visible(False)
    ax.set_axisbelow(True)
    ax.grid(color='gray', linewidth=1, axis='y', alpha=0.4)
    plt.legend()
    plt.savefig(image_file_path)
    plt.close()
    
# Definición de la clase que será capaz de realizar el análisis de adquisición y venta de acciones

class BuySellStocks:
    
    def __init__(self, ticker, start, end, weights, investment):
        self.ticker = ticker
        self.start = start
        self.end = end
        self.weights = weights
        self.investment = investment
    
    def first_price_stock(self):
        stock_first_df = pd.DataFrame()
        for i in self.ticker:
            tickers = yf.Ticker(i).history(start = self.start, end = self.end)["Close"].head(1)
            stock_first_df[i] = tickers
        stock_first_df = pd.melt(stock_first_df.reset_index(), id_vars = ['Date'], var_name = 'Ticket',
           value_name = 'Precio')
        stock_first_df = stock_first_df.set_index("Date")
        stock_first_df["Precio"] = round(stock_first_df["Precio"],2)
        stock_first_df["Pesos %"] = [100 * x for x in self.weights] 
        stock_first_df["Inversión Parcial"] = [self.investment * x for x in self.weights]
        stock_first_df["Número de Acciones"] = round(stock_first_df["Inversión Parcial"] / stock_first_df["Precio"],0)
        stock_first_df["Inversión Inicial"] = self.investment
        stock_first_df = stock_first_df[["Inversión Inicial", "Ticket", "Precio", "Pesos %", "Inversión Parcial", 
                                         "Número de Acciones"]]
        stock_first_df = stock_first_df.reset_index()
        return stock_first_df
    
    def last_price_stock(self):
        stock_last_df = pd.DataFrame()
        for i in self.ticker:
            tickers = yf.Ticker(i).history(start = self.start, end = self.end)["Close"].tail(1)
            stock_last_df[i] = tickers
        stock_last_df = pd.melt(stock_last_df.reset_index(), id_vars = ['Date'], var_name = 'Ticket',
           value_name = 'Precio')
        stock_last_df = stock_last_df.set_index("Date")
        stock_last_df["Precio"] = round(stock_last_df["Precio"],2)
        stock_last_df["Pesos %"] = [100 * x for x in self.weights]
        stock_last_df["Inversión Inicial"] = self.investment
        stock_last_df["Inversión Parcial"] = [self.investment * x for x in self.weights]
        quantity_stock = round(stock_last_df["Inversión Parcial"] / stock_last_df["Precio"],0)
        stock_last_df["Número de Acciones"] = quantity_stock
        stock_last_df["Ingreso Parcial"] = round(stock_last_df["Número de Acciones"] * stock_last_df["Precio"],2)
        stock_last_df = stock_last_df[["Inversión Inicial", "Ticket", "Inversión Parcial", "Pesos %", "Precio", 
                                       "Número de Acciones", "Ingreso Parcial"]]
        stock_last_df = stock_last_df.reset_index()
        return stock_last_df
    
    def benefits_buy_sell_stock(self):
        result = self.last_price_stock()
        income = result["Ingreso Parcial"].sum()
        benefits = round(income - self.investment,2)
        return benefits    
    
    def plot_income_outcome_benefits(self):
        proyect_directory = os.getcwd()
        plots_directory = os.path.join(proyect_directory, "plots")
        os.makedirs(plots_directory, exist_ok=True)
        image_file_name = 'beneficio_ingreso_inversion.png'
        image_file_path = os.path.join(plots_directory, image_file_name)
        df = []
        df_columns = ["Inversión", "Ingreso", "Beneficio"]
        result = self.last_price_stock()
        income = result["Ingreso Parcial"].sum()
        benefits = round(income - self.investment, 2)
        df.append(round(self.investment,2))
        df.append(round(income, 2))
        df.append(round(benefits, 2))
        df = pd.DataFrame({
            'Column':df_columns,
            'Values':df
        })
        fig, ax = plt.subplots(figsize = (8,6), dpi = 80)
        bars = ax.bar(df["Column"], df["Values"], width = 0.5)
        for i, bar in enumerate(bars):
            if df['Values'][i] < 0:
                bar.set_color('#E9512E')
            else:
                bar.set_color('#3675D6')
        ax.set_ylabel('Valores')
        ax.bar_label(ax.containers[0], fontsize = 8.5)
        plt.title(f'Inversión, Ingreso y Beneficio', size = 15)
        for i in ['bottom', 'left']:
            ax.spines[i].set_color('black')
            ax.spines[i].set_linewidth(1.5) 
        right_side = ax.spines["right"]
        right_side.set_visible(False)
        top_side = ax.spines["top"]
        top_side.set_visible(False)
        ax.set_axisbelow(True)
        plt.savefig(image_file_path)
        plt.close()