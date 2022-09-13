# فصل اول: الگو طراحی استراتژی
خیلی مواقع پیش میاد که ما با الگو هایی طرف هستیم که اشیائ مختلف خصوصیات مختلف و متضادی از هم دارند.

فرض کنید میخواییم یک بازی اول شخص بسازیم که میتونیم کارکتر های مختلفی داشته باشیم. 

درست حدس زدید این یک بازی خشن و پر از خون ریزیه.

خب ما توی این بازی دو مدل مختلف کارکتر داریم، یکسری از کارکتر ها با شمشیر های بلند هستد و کارکتر های بعدی تیر و کمان دارن.
![Melle](https://github.com/sadeghesfahani/head-first-design-pattern/raw/main/images/condo_gua.png)
![Archer](https://github.com/sadeghesfahani/head-first-design-pattern/raw/main/images/imp_arc_post.png)

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


## اصل اول: کامپوزیشن را به ارث بری ترجیح بده

خب به نظرم این شیوه طراحی اصلا خوب نبود. بذارید دوباره از اول فکر کنیم. ما باید تمام آن چیز هایی که ثابت هستند رو یکجا نگه داریم و متغییر هارو جدا کنیم. خب ما میدونیم که همه کارکتر های ما یک رفتاری به نام حمله یا اتک دارند. اگر ما به جای ارث بری و ساخت کلاس های جدید، رفتار های مختلف حمله رو کلاس بندی کنیم چی؟

مثلا یه چیزی توی این مایه ها:

```
class AttachBehavior(ABC):
    
    @abstractmethod
    def attack(self):
        pass
```

بعدش بیاییم رفتار های مختلف رو بسازیم:

```
class RangeAttack(AttachBehavior):

    def __init__(self, range, accuracy, weather_influence_factor):
        self._range = range
        self._accuracy = accuracy
        self._weather_influence_factor = weather_influence_factor

    def attack(self):
        print(f'Attacks with a bow. Range: {self._range}, Accuracy: {self._accuracy} with the weather influence factor of {self._weather_influence_factor}')


class MelleAttack(AttachBehavior):

    def __init__(self, damage_power):
        self.damage_power = damage_power

    def attack(self):
        print(f'Attacks with a sword. damage power: {self.damage_power}')

```

اینطوری میتونم خیلی راحت به هر کارکتر یک رفتار نسبت بدم و در آینده اگر بخوام تغییری توی اون رفتار ایجاد کنم دیگه نیازی نیست توی تک تک کلاس هام اینکارو بکنم. بریم با هم ببینیم:

```
class Archer(Character):

    def __init__(self, name, level, attack_behavior):
        super().__init__(name, level)
        self._range = range
        self.attack_behavior = attack_behavior

    def attack(self):
        self.attack_behavior.attack()

    def move(self):
        print(f'{self.name} moves slowly.')
```
خب بذارید بریم و ببینیم چطوری باید از این استفاده کنیم:

```
range_behavior = RangeAttack(10, 100, 0.5)
archer = Archer('Sina', 1, range_behavior)

archer.attack()
```

و خروجی ما:
```
Attacks with a bow. Range: 10, Accuracy: 100 with the weather influence factor of 0.5
```

به جای اینکه ما مستقیم ارث بری رو انجام بدیم و مجبور بشیم تغییرات اساسی رو توی مدل های کانکریتمون اعمال کنیم، هندل کردن این خصوصیت رو به کلاس دیگه واگذار کردیم و از خصوصیت به نام پولیمورفیزم در شی گرایی استفاده کردیم.


حالا دیگه نوبت شماست. با استفاده از مطالبی که گفته شد:

با این ها یک برنامه مشابه بسازید

![Archer](/images/your_turn_strategy.png)


# فصل دوم: الگو مشاهده کننده

خب عملا از اسم این الگو هیچی نمیشه فهمید، ما هم قرار نیست اینجا به مغز شما فشار بیاریم تا چیزی رو متوجه بشدی پس بدون فوت وقت بریم سراغ برنامه نویسی بازی ای که داشتیم میساختیم.

بعد از اینکه ما کارکتر هارو ساختیم و یک موتور گرافیکی قوی هم براش اوردیم بالا، حالا وقت اینه که بیست تا بازیکن رو بفرستیم توی یک زمین تا با هم مبارزه کنن.

## جنگ بزرگ

![Archer](/images/observer-fight.jpg)

یکی از اولین نیاز ها برای هر بازی گروهی امکان چت کردن با هم تیمی هاست تا بتونیم خیلی راحت تاکتیک های مختلف رو پیش بگیریم و به دژ دشمن نفوذ کنیم. خب به نظرم که کاری نداری، بیایید برای هر بازی یک شی بسازیم تا ببینیم چی کار می تونیم باهاش بکنیم.

```angular2html
class War:
    team1 = []
    team2 = []

    def __init__(self, map_name, weather):
        self.map_name = map_name
        self.weather = weather

    @staticmethod
    def join_players(player):
        if len(War.team1) >= len(War.team2):
            War.team2.append(player)
            player.team = 2
        else:
            War.team1.append(player)
            player.team = 1
```

با این کلاس خیلی راحت هر کسی که وارد مپ ما میشه به طور مساوی توی گروه های مختلف پخش میشه، حالا برای ارسال پیام به هم تیمی هاش کافیه روی تیم خودش یک حلقه بزنیم و پیام رو براشون ارسال کنیم. بریم ببینیم یعنی چی

```angular2html
class Player:
    def __init__(self, hero):
        self.hero = hero
        self.team = None

    def send_message(self, message):
        if self.team == 1:
            for player in War.team1:
                player.get_message(self, message)
        else:
            for player in War.team2:
                player.get_message(self, message)

    def get_message(self, sender, message):
        print(f"this is {self.hero} message tab, {sender.hero}: {message}")
```

خیلی آسون بود، نه؟ بریم ببینیم چطوری باید این کد رو اجرا کنیم؟

```angular2html
sina = Player('Sina')
ali = Player('Ali')
reza = Player('Reza')
mohammad = Player('Mohammad')

war = War('map1', 'rainy')
war.join_players(sina)
war.join_players(ali)
war.join_players(reza)
war.join_players(mohammad)


sina.send_message('Hello to all')
```

و نتیجه نهایی:

```angular2html
this is Ali message tab, Sina: Hello to all
this is Mohammad message tab, Sina: Hello to all
```

حالا سوالی که اینجا پیش میاد اینه که اگر یکی بخواد پیام هارو دریافت نکنه چی؟ خب شاید اولین جواب این باشه که توی یو آی نمایشش نمیدیم. مساله بعدی که پیش میاد اینه که اینجا ما داریم پیام رو توی کانال عمومی میفرستیم. شاید ما بخواییم بازیکن های اطراف ما پیام مارو ببینن.

## قابلیت تشخیص مکان بازیکن

بسیار خب، لازمه یکم توی کلاس جنگمون تغییر ایجاد کنیم.

```angular2html
class War:
    team1 = []
    team2 = []

    def __init__(self, map_name, weather):
        self.map_name = map_name
        self.weather = weather

    @staticmethod
    def join_players(player):
        if len(War.team1) >= len(War.team2):
            War.team2.append(player)
            player.team = 2
        else:
            War.team1.append(player)
            player.team = 1

    @staticmethod
    def player_moves(player):
        print(f'{player.hero} moves to {player.position}')
        for team1_player in War.team1:
            team1_player.process_nearby_players(player)
        for team2_player in War.team2:
            team2_player.process_nearby_players(player)
```

متد استاتیکی که اینجا اضافه کردیم وظیفش اینه که هر زمان هر کاربری تکون خورد، این جا به جایی رو به همه کاربرهای دیگه اطلاع بده تا بتونن بر اساس اون تصمیم گیری کنند. و حالا لازمه که کلاس پلیر رو هم یه تغییری بدیم تا بتونه با ساختار جدید کار کنه و به اطرافیانش پیام بده.

```angular2html
class Player:
    def __init__(self, hero):
        self.hero = hero
        self.team = None
        self.position = [0, 0]
        self.nearby_players = []

    def send_chanel_message(self, message):
        if self.team == 1:
            for player in War.team1:
                player.get_message(self, message)
        else:
            for player in War.team2:
                player.get_message(self, message)

    def send_nearby_message(self, message):
        for player in self.nearby_players:
            player.get_message(self, message)

    def get_message(self, sender, message):
        print(f"this is {self.hero} message tab, {sender.hero}: {message}")

    def move(self, position):
        self.position = position
        War.player_moves(self)

    @staticmethod
    def calculation_distance(position1, position2):
        return math.sqrt((position1[0] - position2[0]) ** 2 + (position1[1] - position2[1]) ** 2)

    def process_nearby_players(self, player):
        if self.calculation_distance(self.position, player.position) < 5:
            self.nearby_players.append(player)
        else:
            try:
                self.nearby_players.remove(player)
            except ValueError:
                pass
```

سه تا متد جدید به کلاس قبلیمون اضافه شده و یک متد هم اسمش عوض شده، ارسال پیام رو به ارسال پیام در کانال تبدیل کردیم و یک متد برای ارسال پیام به اطرافیان اضافه کردیم.

یک متد وظیفه اش اینه که فاصله دو نقطه رو به ما بده و یک متد هم وظیفه اش اینه که اگر کاربر در شعاع ده متری ما قرار گرفت اون رو به عنوان کاربر نزدیک ثبت کنه و اگر از دایره ما خارج شد اون رو حذف کنه.

بریم ببینیم چطوری باید از این ساختار جدید استفاده کنیم.

```angular2html
sina = Player('Sina')
ali = Player('Ali')
reza = Player('Reza')
mohammad = Player('Mohammad')
sara = Player('Sara')
mahnaz = Player('Mahnaz')
samira = Player('Samira')
maryam = Player('Maryam')


war = War('map1', 'rainy')
war.join_players(sina)
war.join_players(ali)
war.join_players(reza)
war.join_players(mohammad)
war.join_players(sara)
war.join_players(mahnaz)
war.join_players(samira)
war.join_players(maryam)

sina.move([100, 100])
ali.move([20, 20])
reza.move([3, 3])
mohammad.move([4, 4])
sara.move([5, 5])
mahnaz.move([6, 6])
samira.move([7, 7])
maryam.move([8, 8])


maryam.send_nearby_message('Hello to all')
```

همینجا جا داره از دوستان بابت عدم جداسازی جنسیتی معذرت خواهی کنم. طبق روال باید خانم ها در یک سرور باشن و آقایان در یک سرور دیگه ولی خب دیگه ببخشید ما یکم از نظر ذهنی عقب مونده هستیم و این دوستان رو کنار هم قرار دادیم.

خب حالا اگر این کد رو اجرا کنیم میبینیم که پیام هایی که مریم به اطرافیانش ارسال میکنه به همه ارسال میشه.

```angular2html
Sina moves to [100, 100]
Ali moves to [20, 20]
Reza moves to [3, 3]
Mohammad moves to [4, 4]
Sara moves to [5, 5]
Mahnaz moves to [6, 6]
Samira moves to [7, 7]
Maryam moves to [8, 8]
this is Reza message tab, Maryam: Hello to all
this is Maryam message tab, Maryam: Hello to all
```

تبریک می گم، بدون اینکه متوجه بشید چی شد از الگو طراحی مشاهده کننده استفاده کردیم. در این الگو طراحی ما یک شنونده داریم و یک پیام دهنده. شنونده ها برای شنیده شدن اعلان آمادگی می کنند و اسم خودشون رو در لیست فرستنده قرار میدن، فرستنده هم هر لحظه که نیاز باشه به تمام افراد لیست پیامشو ارسال می کنه. به همین راحتی.