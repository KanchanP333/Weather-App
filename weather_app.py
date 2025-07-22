import sys #Used to handle system variables
import requests #Used to handle API requests
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout

from PyQt5.QtCore import Qt #From the module QtCore, the class Qt is imported for alignment


class WeatherApp(QWidget):
    def __init__(self):
        super().__init__()
        self.cityLabel=QLabel("Enter the City name: ", self) #Adding the label to the weather app object
        self.cityInput=QLineEdit(self)
        self.getWeatherBtn=QPushButton("Get Weather", self)#When clicked sends an API request
        self.temperatureLabel=QLabel(self)
        self.emojiLabel=QLabel(self)
        self.descriptionLabel=QLabel(self)
        self.initUI()

    def initUI(self): #Used to initialize the UI
        self.setWindowTitle("Weather App")
        self.setGeometry(700,400,500,300)

        vbox=QVBoxLayout() #Vertical layout
        vbox.addWidget(self.cityLabel) 
        vbox.addWidget(self.cityInput)
        vbox.addWidget(self.getWeatherBtn)
        vbox.addWidget(self.temperatureLabel)
        vbox.addWidget(self.emojiLabel)
        vbox.addWidget(self.descriptionLabel)

        self.setLayout(vbox)

        self.cityLabel.setAlignment(Qt.AlignCenter)
        self.cityInput.setAlignment(Qt.AlignCenter)
        self.temperatureLabel.setAlignment(Qt.AlignCenter)
        self.emojiLabel.setAlignment(Qt.AlignCenter)
        self.descriptionLabel.setAlignment(Qt.AlignCenter)

        self.cityLabel.setObjectName("cityLabel")
        self.cityInput.setObjectName("cityInput")
        self.getWeatherBtn.setObjectName("getWeatherBtn")
        self.temperatureLabel.setObjectName("temperatureLabel")
        self.emojiLabel.setObjectName("emojiLabel")
        self.descriptionLabel.setObjectName("descriptionLabel")

        self.setStyleSheet("""
            QWidget {
                background-color: #f0f8ff; 
            }

            QLabel, QPushButton {
                font-family: "Segoe UI";
                color: black;
            }

            QLabel#cityLabel {
                font-size: 30px;
                font-weight: 600;
                margin-top: 20px;
            }

            QLineEdit#cityInput {
                font-size: 30px;
                padding: 10px;
                border: 2px solid skyblue; 
                border-radius: 10px;
                background-color: white;
                color: black;
            }

            QPushButton#getWeatherBtn {
                font-size: 24px;
                font-weight: bold;
                background-color: #87ceeb; /* SkyBlue */
                color: white;
                padding: 10px;
                border: none;
                border-radius: 10px;
                margin-top: 10px;
            }

            QPushButton#getWeatherBtn:hover {
                background-color: #00bfff; /* Darker sky blue */
            }

            QLabel#temperatureLabel {
                font-size: 48px;
                font-weight: 600;
                color: yellowgreen;
                margin-top: 20px;
            }

            QLabel#emojiLabel {
                font-size: 48px;
                margin-top: 10px;
            }

            QLabel#descriptionLabel {
                font-size: 25px;
                font-style: italic;
                color: yellowgreen;
                margin-bottom: 20px;
            }
        """)

        self.getWeatherBtn.clicked.connect(self.getWeather)

    def getWeather(self):
        apiKey="#"
        city=self.cityInput.text()
        url=(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={apiKey}") #Passing a url to make a request
        
        try:
            response=requests.get(url) #The request will return a response object
            response.raise_for_status() #Will raise an exception if there are any HTTP errors
            data=response.json() #Converting to JSON format

            if data["cod"]==200:
                self.displayWeather(data)
        
        except requests.exceptions.HTTPError as httpError: #When an HTTP Request returns an error code of 400/ 500
            match response.status_code:
                case 400:
                    self.displayError("Bad request:\nPlease check your input")
                case 401:
                    self.displayError("Unauthorized:\nInvalid API key")
                case 403:
                    self.displayError("Forbidden:\nAccess is denied")
                case 404:
                    self.displayError("Not found:\nCity not found")
                case 500:
                    self.displayError("Interal Server Error:\nPlease check your input")
                case 502:
                    self.displayError("Bad Gateway:\nInvalid response from the server")
                case 503:
                    self.displayError("Service Unavailable:\nServer is down")
                case 504:
                    self.displayError("Gateway Timeout:\nNo response from the server")
                case _: #Enexcepted error
                    self.displayError(f"HTTP error occured\n{httpError}")

        except requests.exceptions.ConnectionError:
            self.displayError("Connection Error:\nCheck your internet connection")
        
        except requests.exceptions.Timeout:
            self.displayError("Timeout Error:\nThe request timed out")
        
        except requests.exceptions.TooManyRedirects:
            self.displayError("Too many Redirects:\n The request timed out:\nCheck the URL")

        except requests.exceptions.RequestException as req_error: #Network problems/ Invalid URLs
            self.displayError(f"Request Error:\n{req_error}")
            
            



    def displayError(self, message):
        self.temperatureLabel.setStyleSheet("font-size: 30px;")
        self.temperatureLabel.setText(message)
        self.emojiLabel.clear() #To clear the previous data
        self.descriptionLabel.clear()

    def displayWeather(self, data): #Uses Weather Data
        self.temperatureLabel.setStyleSheet("font-size: 48px;")
        temperatureK=data["main"]["temp"] #Temperature is in Kelwin
        temperatureC=temperatureK-273.15 #Converting to Celsius
        weatherID = data["weather"][0]["id"]
        weatherDescription=data["weather"][0]["description"]
        
        self.temperatureLabel.setText(f"{temperatureC:.2f}°C")
        self.emojiLabel.setText(self.getWeatherEmoji(weatherID))
        self.descriptionLabel.setText(weatherDescription)
    
    @staticmethod #Does not rely on any instance data
    def getWeatherEmoji(weatherID):
        if 200<=weatherID<=232:
            return "⛈️"
        elif 300<=weatherID<=321:
            return "⛅"
        elif  500<=weatherID<=531:
            return "🌧️"
        elif 600<=weatherID<=622:
            return "❄️"
        elif 701<=weatherID<=741:
            return "🌫️"
        elif weatherID==762:
            return "🌋"
        elif weatherID==771:
            return "💨"
        elif weatherID==781:
            return "🌪️"
        elif weatherID==800:
            return "☀️"
        elif 801<=weatherID<=804:
            return "☁️"
        else:
            return " "


if __name__=="__main__":
    app=QApplication(sys.argv)
    weatherApp=WeatherApp()
    weatherApp.show()
    sys.exit(app.exec_()) #Used to handle methods within the application
