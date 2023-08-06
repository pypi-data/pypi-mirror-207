import zeep
from zeep.cache import SqliteCache
from zeep.transports import Transport

from TRIdentification.service.helper import IsFromSyrian


class IdentificationService:
    transport = Transport(cache=SqliteCache(), timeout=10)
    base_url = 'https://tckimlik.nvi.gov.tr/Service'

    def __call__(self, method, *args):
        method = getattr(self, method)
        return method(*args)

    # Türk vatandaşlarını nüfus müdürlüğünden kontrol et
    def TRIdentificationNumberValidator(self, tckn: str, ad: str, soyad: str, dogumyil: int) -> bool:
        api_url = f'{self.base_url}/KPSPublic.asmx?WSDL'
        service = zeep.Client(wsdl=api_url, transport=self.transport)
        response = service.service.TCKimlikNoDogrula(tckn, ad.upper(), soyad.upper(), dogumyil)
        return response

    # Yabancı uyruklu vatandaşları nüfus müdürlüğünden kontrol et
    def ForeignTRIdentificationNumberValidator(self, tckn: str, ad: str, soyad: str, dogumgun: int, dogumay: int,
                                               dogumyil: int) -> bool:
        api_url = f'{self.base_url}/KPSPublicYabanciDogrula.asmx?WSDL'
        service = zeep.Client(wsdl=api_url, transport=self.transport)
        response = service.service.YabanciKimlikNoDogrula(tckn, ad.upper(), soyad.upper(), dogumgun, dogumay,
                                                          dogumyil)
        return response

    # Eski Nüfus Cüzdanı Doğrulama
    def OldPersonAndIdentificationCardValidator(self, tckn: str, ad: str, soyad: str, dogumgun: int, dogumay: int,
                                                dogumyil: int,
                                                serino: str, cuzdan_no: int) -> bool:
        api_url = f'{self.base_url}/KPSPublicV2.asmx?WSDL'
        service = zeep.Client(wsdl=api_url, transport=self.transport)
        response = service.service.KisiVeCuzdanDogrula(tckn, ad.upper(), soyad.upper(), dogumgun, dogumay,
                                                       dogumyil,
                                                       serino.upper(), cuzdan_no)
        return response

    # Yeni Kimlik Kartı Doğrulama
    def NewPersonAndIdentificationCardValidator(self, tckn: str, ad: str, soyad: str, dogumgun: int, dogumay: int,
                                                dogumyil: int,
                                                tck_seri_no: str) -> bool:
        api_url = f'{self.base_url}/KPSPublicV2.asmx?WSDL'
        service = zeep.Client(wsdl=api_url, transport=self.transport)
        response = service.service.KisiVeCuzdanDogrula(tckn, ad.upper(), soyad.upper(), dogumgun, dogumay,
                                                       dogumyil,
                                                       tck_seri_no.upper())
        return response

    # Türk vatandaşları veya Ikamet izni olanları kontrol et
    def IdentityClassify(self, tckn: str, ad: str, soyad: str, dogumgun: int, dogumay: int, dogumyil: int) -> bool:
        if IsFromSyrian(tckn):
            return self.ForeignTRIdentificationNumberValidator(tckn, ad.upper(), soyad.upper(), dogumgun, dogumay,
                                                               dogumyil)
        return self.TRIdentificationNumberValidator(tckn, ad.upper(), soyad.upper(), dogumyil)
