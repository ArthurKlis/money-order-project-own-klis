# Program ułatwiający wypełnianie formularza zamówienia zaliczki gotówkowej

<p align="center">
<img src="code_screen.jpg"  width="216" height="384" />
<img src="amounts_screen.jpg" width="216" height="384" />
<img src="result_screen.jpg" width="216" height="384" />
</p>

## Program, który napisałem na własne potrzeby, aby jeszcze szybciej wykonywać swoją pracę maksymalnie wykorzystując fakt zadaniowego czasu pracy.

Nie chce mi się rano skrupulatnie liczyć sumy kwot z powiedzmy 10-ciu lub więcej kwitków. Jest to nudne. I zdarza się przy tym pomylić. Już nawet z powodu wyrobienia się w skupieniu tylko z tak błachego powodu jak źle wciśnięty przycisk, ale się zdarza. Ponadto czasem człowiek musi to zrobić bardzo szybko, a pośpiech przy liczeniu sum czy dzieleniu ich nie jest wskazany - każda pomyłka choć możliwa do poprawy spożytkuje cenny czas. Po policzeniu sumy kwot ich podział na nominały jest jeszcze bardziej rutynowy. Czasem, jak człowiek się nad tym pochyli przy dużej kwocie to potem już ma mało czasu na to, żeby zastosować znajomość obszaru i pozmieniać coś adekwatnie do klientów.

Stwierdziłem, że potrzebuje interpreter Python-a na iOS, który będzie pozbawiony reklam i darmowy. Obecność reklam niesie ryzyko dużej ilości elementów śledzących zachowanie użytkownika aplikacji w niej samej. Brak reklam był także istotny, bo nie chciałem być zmuszonym zużywać swojego zasobu transferu danych mobilnych. Oczywiście program postanowiłem napisać w Python-ie ze względu na brak sprzętu firmy Apple do stworzenia natywnej aplikacji systemu operacyjnego oraz brak zaznajomienia z narzędziami, które pozwalają tworzyć aplikacje bez tego. Także aplikacje na iOS będąca inerpreterem Python-a ograniczonym w funkcjonalności do biblioteki standardowej Python-a w darmowej wersji oraz Python jako język programowania to są optymalne podwaliny rozwiązania.

Kolejnym aspektem do przemyślenia były działania arytmetyczne na liczbach z częścią dziesiętną reprezentowanych w komputerze. Reprezentacja liczb w systemie dwójkowym w ramach poleceń samego języka jest obarczona niedokładnością wynikająca ze sposobu zaokrąglania. Długo zastanawiałem się, czy uwzględnić jakąkolwiek bibliotekę (zwaną modułem w przypadku Pythona) by to w ten sposób zrealizować dzielenie i uprościć kod. Ze względu jednak na to, że to miał być Python i darmowy jego interpreter uznałem, że lepszym podejściem jest więcej kodu i bardziej proceduralny charakter kodu. W ten sposób doszedłem do podziału nominałów na całości oraz części dziesiętne, gdzie każde grupy nominałów dzielę tak, jak by to były liczny całkowite.

Interesujące może się wydać unikanie moinałów 500 oraz 200 złotych. Oczywiście dobry program pownien to uwzględniać jednak specyfika pracy i oczekiwania klientów na to nie pozwalają. W krótkim czasie będę jednak potrzebował dodać możliwość zamiany nominałów choć uważam, że to zbytnio skomplikuje program. Zamiana w głowie podczas przepisywania na kartkę papieru dla tak prostych operacji wydaje się być lepsza.

### Kolejna wersja - wersja druga
Tworząc ten prosty program/skrypt uznałem, że zależy mi na rozwiązaniu, które zapewni mi zmniejszenie nakładu czasu na czynność, która zajmuje najwięcej. Do tej pory liczyłem sumą ręcznie na kalkulatorze. Obecnie rozbudowałem kod o obsługę sumy tak by kolejna czynność była ujęta w tym rozwiązaniu.
