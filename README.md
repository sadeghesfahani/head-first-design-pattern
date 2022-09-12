# فصل اول: الگو طراحی استراتژی
خیلی مواقع پیش میاد که ما با الگو هایی طرف هستیم که اشیائ مختلف خصوصیات مختلف و متضادی از هم دارند.

فرض کنید میخواییم یک بازی اول شخص بسازیم که میتونیم کارکتر های مختلفی داشته باشیم. 

درست حدس زدید این یک بازی خشن و پر از خون ریزیه.

خب ما توی این بازی دو مدل مختلف کارکتر داریم، یکسری از کارکتر ها با شمشیر های بلند هستد و کارکتر های بعدی تیر و کمان دارن.

خب حالا باییم یکم وارد کد نویسی بشیم.

```
class Character(ABC):
    def __init__(self, name, level):
        self.name = name
        self.level = level

    @abstractmethod
    def attack(self):
        pass

    @abstractmethod
    def move(self):
        pass

```

خب حالا میدونیم که کارکتر های مختلفمون باید از این کلاس ارثبری کنند. دو تا کارکتر مختلف رو با هم بسازیم.

```
class Archer(Character):
    def __init__(self, name, level):
        super().__init__(name, level)

    def attack(self):
        print(f'{self.name} attacks with a bow.')

    def move(self):
        print(f'{self.name} moves slowly.')


class Knight(Character):
    def __init__(self, name, level):
        super().__init__(name, level)

    def attack(self):
        print(f'{self.name} attacks with a sword.')

    def move(self):
        print(f'{self.name} moves quickly.')
```

تا اینجا همه چیز عالیه، ایول عجب کدی زدم. حالا که اینقدر خوب کد میزنم بذارید یه کارکتر کماندار خفن تر هم بسازم.

```
class RoyalArcher(Character):
    def __init__(self, name, level):
        super().__init__(name, level)

    def attack(self):
        print(f'{self.name} attacks with a bow.')

    def move(self):
        print(f'{self.name} moves slowly.')
```

خیلی خوب شد، ولی صبر کن ببینم. اولا این دو تا با هم چه فرقی می کنند؟ دوما دارم یک تیکه کد رو تکرار می کنم. خب سوال اول اینکه به نظرم تیر انداز معمولی از فاصله کمتری میتونه بزنه به هدف و احتمالا دقت کمتری هم داره. خب پس بذارید اینارو هم اضافه کنم.

```
class Character(ABC):
    def __init__(self, name, level, range=None, accuracy=None):
        self.name = name
        self.level = level
        self._range = range
        self._accuracy = accuracy

    @abstractmethod
    def attack(self):
        pass

    @abstractmethod
    def move(self):
        pass
```
اینجوری خیلی بهتر شد حالا راحت میتونم این دوتارو دوباره تعریف کنم.


```
class Archer(Character):
    def __init__(self, name, level, range, accuracy):
        super().__init__(name, level, range, accuracy)

    def attack(self):
        print(f'{self.name} attacks with a bow. Range: {self._range}, Accuracy: {self._accuracy}')

    def move(self):
        print(f'{self.name} moves slowly.')


class RoyalArcher(Character):
    def __init__(self, name, level, range, accuracy):
        super().__init__(name, level, range, accuracy)

    def attack(self):
        print(f'{self.name} attacks with a bow. Range: {self._range}, Accuracy: {self._accuracy}')

    def move(self):
        print(f'{self.name} moves slowly.')
``` 

حالا اگر بخوام یک شوالیه تعریف کنم چی؟ اطلاعات مربوط به تیرانداز های راه دور چرا باید توی شوالیه من باشه؟ اگر یکی اشتباهی ازشون استفاده کنه چی؟ به نظرم بهتره که دو تا کلاس ابسترکت دیگه از روی کارکتر بسازم و خصوصیات هر کدوم رو به خودشون بدم.

```
class Character(ABC):
    def __init__(self, name, level):
        self.name = name
        self.level = level

    @abstractmethod
    def attack(self):
        pass

    @abstractmethod
    def move(self):
        pass


class RangeCharacter(ABC, Character):
    def __init__(self, name, level, range, accuracy):
        super().__init__(name, level)
        self._range = range
        self._accuracy = accuracy

    @abstractmethod
    def attack(self):
        pass

    @abstractmethod
    def move(self):
        pass


class MelleCharacter(ABC, Character):
    def __init__(self, name, level, speed):
        super().__init__(name, level)
        self._speed = speed

    @abstractmethod
    def attack(self):
        pass

    @abstractmethod
    def move(self):
        pass
```

حالا خیلی راحت میتونم از روشون هر چیزی که میخوام بسازم

```
class Archer(RangeCharacter):
    def __init__(self, name, level, range, accuracy):
        super().__init__(name, level, range, accuracy)

    def attack(self):
        print(f'{self.name} attacks with a bow. Range: {self._range}, Accuracy: {self._accuracy}')

    def move(self):
        print(f'{self.name} moves slowly.')


class Knight(MelleCharacter):
    def __init__(self, name, level, speed):
        super().__init__(name, level, speed)

    def attack(self):
        print(f'{self.name} attacks with a sword.')

    def move(self):
        print(f'{self.name} moves quickly.')
```

خیلی عالی شد، حالا میریم و ۴۸ مدل تیرانداز مختلف میسازیم. همه چیز داره عالی پیش میره تا اینکه میگیم صبر کن ببینم، اکر ما بخواییم خصوصیت آب و هوایی روی دقت و رنج تیر انداز ها تاثیر بذاره چی؟

اووووم، بذار فکر کنم. آها کاری نداره که ما یه تاثیر آب و هوایی اضافه می کنیم به کلاس اصلی و خیلی راحت تاثیرشو توی اتک ها اعمال می کنیم. اینجوری:

```
class RangeCharacter(ABC, Character):
    def __init__(self, name, level, range, accuracy, weather_influence_factor):
        super().__init__(name, level)
        self._range = range
        self._accuracy = accuracy
        self._weather_influence_factor = weather_influence_factor

    @abstractmethod
    def attack(self):
        pass

    @abstractmethod
    def move(self):
        pass
```

کاری نداشت که. ولی صبر کن ببینم. یعنی الان باید برم این تغییر رو توی ۴۸ تا مدل کارکتری که ساختم پیاده کنم؟ آقا من نیستم خداحافظ.



