from  models.rating import Rating
class Restaurant:

    restaurants = []
    
    def __init__(self,name, category) -> None:
        self._name = name.title()
        self._category = category.title()
        self._active = False
        self._rating = []
        Restaurant.restaurants.append(self)
        
    def __str__(self) -> str:
        return f'{self._name.ljust(20)} | {self._category.ljust(20)} | '

    @property
    def name(self) -> str:
        return self._name
    
    @name.setter
    def name(self, name: str) -> None:
        self._name = name.strip()

    @property
    def category(self) -> str:
        return self._category
    
    @category.setter
    def category(self, category: str) -> None:
        self._category = category.strip()

    @property
    def active(self) -> bool:
        return self._active
    
    @active.setter
    def active(self, active: bool) -> None:
        self._active = active

    @classmethod
    def list_restaurants(cls):
        print(f"{'Name'.ljust(20)} | {'Restaurants'.ljust(20)} | {'Average'.ljust(20)} |")
        for restaurant in cls.restaurants:
            print(f"{restaurant._name.ljust(20)} | {restaurant.category.ljust(20)} | {str(restaurant.avg_rating).ljust(20)} |")
    
    def receive_rating(self, customer, rating_number):
        if rating_number > 0 and rating_number <= 5:
            rating = Rating(customer, rating_number)
            self._rating.append(rating)

    def list_rating(self):
        for rating in self._rating:
            print(f'{rating._customer}: {rating._rating}')

    @property
    def avg_rating(self):
        total_rating = sum(rating._rating for rating in self._rating)
        avg_rating = total_rating / len(self._rating) if len(self._rating) != 0 else 0
        return round(avg_rating,1)
