import bs4
import requests

class Bencana:
    def __init__(self, website, description):
        self.description = description
        self.result = None
        self.url = website

    def tampilkan_keterangan(self):
        print(self.description)
    def scrapping_data(self):
        print('scrapping data not available')
    def tampilkan_data(self):
        print('data was not ready')
    def run(self):
        self.scrapping_data()
        self.tampilkan_data()

class banjirTerbaru(Bencana):
    def __init__(self, url):
        super(banjirTerbaru, self).__init__(url,
        'Not yet implemented, but it should return last flood in Indonesia')
class gempaTerbaru(Bencana):
    def __init__(self, url):
        super(gempaTerbaru, self).__init__(url,
        'To get the latest earthquake in Indonesia from Bureau website https: www.bmkg.go.id')

    def scrapping_data(self):
        """
        Tanggal     : 01 Mei 2023
        Waktu       : 10:20:12 WIB
        Magnitude   : 3.8
        Kedalaman   : 10 km
        Lokasi      : LS = 4.01 BT = 136.07
        Episentrum  : Pusat gempa berada di darat 12 km Timur Laut Dogiyai
        Testimoni   : Dirasakan (Skala MMI): II Dogiyai
        :return:
        """

        try:
            content = requests.get(self.url)
        except Exception:
            return None
        if content.status_code == 200:
            soup = bs4.BeautifulSoup(content.text, 'html.parser')

            result = soup.find('span', {'class': 'waktu'})
            result = result.text.split(', ')
            tanggal = result[0]
            waktu = result[1]

            result = soup.find('div', {'class': 'col-md-6 col-xs-6 gempabumi-detail no-padding'})
            result = result.findChildren('li')

            i = 0
            magnitude = None
            kedalaman = None
            koordinat = None
            lokasi = None
            dirasakan = None
            ls = None
            bt= None
            for res in result:
                if i == 1:
                    magnitude = res.text
                elif i == 2:
                    kedalaman = res.text
                elif i == 3:
                    koordinat = res.text.split(' - ')
                    ls = koordinat[0]
                    bt = koordinat[1]
                elif i == 4:
                    lokasi = res.text
                elif i == 5:
                    dirasakan = res.text
                i = i + 1

            hasil = dict()
            hasil['tanggal'] = tanggal
            hasil['waktu'] = waktu
            hasil['magnitude'] = magnitude
            hasil['kedalaman'] = kedalaman
            hasil['koordinat'] = {'ls': ls, 'bt': bt}
            hasil['lokasi'] = lokasi
            hasil['dirasakan'] = dirasakan
            self.result = hasil
        else:
            return None

    def tampilkan_data(self):

        if self.result is None:
            print('Tidak bisa menemukan data gempa terkini')
            return

        print('\nGempa terakhir berdasarkan BMKG')
        print(f"Tanggal {self.result['tanggal']}")
        print(f"Waktu {self.result['waktu']}")
        print(f"Magnitude {self.result['magnitude']}")
        print(f"Kedalaman {self.result['kedalaman']}")
        print(f"Koordinat: LS =  {self.result['koordinat']['ls']}, BT =  {self.result['koordinat']['bt']}")
        print(f"Lokasi {self.result['lokasi']}")
        print(f"{self.result['dirasakan']}")

if __name__ == '__main__':
    gempaIndonesia = gempaTerbaru('https://www.bmkg.go.id/')
    gempaIndonesia.tampilkan_keterangan()
    gempaIndonesia.run()

    banjirIndonesia = banjirTerbaru('Not Yet Available')
    banjirIndonesia.tampilkan_keterangan()
    banjirIndonesia.run()

    daftar_bencana = [gempaIndonesia, banjirIndonesia]
    print('\nSemua bencana yang ada')
    for bencana in daftar_bencana:
        bencana.tampilkan_keterangan()
