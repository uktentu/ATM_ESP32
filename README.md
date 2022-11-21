
# >Model ATM_ESP32< !

This project is based on userinterface using Tkinter with python and a working model of ESP32 using Google workspaces like Spreadsheet's for online Cloud.

## 🛠 Languages
Arduino, Python, Google Apps script...


## Libraries
### Arduino

In Arduino ide use ```"WiFi.h"``` for ESP32 to access the Wifi and ```<HTTPClient.h>``` for sending ```http``` requests to internet.

### Python
In Python ide use ```tkinter``` for creating GUI (Graphical User Interface) and ```serial``` for accessing the Serial Port and seting BaudRate.

**Install these Libraries using the Following Commands**

```
pip install tkinter

pip install pyserial
```

### Google AppsScript
In AppsScript ```doGet``` function to access the parameters sent by ESP32 and return the desired outputs to ESP32.
## Features

- Multiple User Interface
- New User Creation
- Login (Username and Password verification)
- Displaying Account Holder name
- Debiting money
- Crediting money
- See Available balance
- See Mini Statement of last 5 transactions.



## Demo


![](https://github.com/uktentu/ATM_ESP32/blob/main/Demo.gif)
## Acknowledgements

 - This is a part of Evaluation of Embeded Systems course Instructed by Ankit A. Bhurane and Amit Agarwal, Here is the [Problem statement](https://github.com/uktentu/ATM_ESP32/blob/main/Problem%20Statement)
