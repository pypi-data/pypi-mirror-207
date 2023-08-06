# Indonesia Earthquake Report
This package will provide the most update of Indonesian bureau of Forecast (BMKG)

## How It Work?
This package will scrape from [BMKG](https://www.bmkg.go.id) to get the latest earthquake reports in Indonesia.

This package will use BeautifulSoup4 and Request, to then produce in the form of JSON that is ready to be used in web or mobile applications.

## How To Use This Package?
```
import updateGempa

if __name__ == '__main__':
    print('Aplikasi Utama')
    result = updateGempa.ekstraksi_data()
    updateGempa.tampilkan_data(result)
```
# Author
Hasan Gani