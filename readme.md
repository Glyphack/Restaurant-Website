# Restaurant Website

A website for restaurants which can handle menu and customer orders(more features will be added soon)

## Getting Started

Follow these steps to clone the repository and getting started with running website on your local machine.

### Prerequisites

this website is made with django and python3 so you need to install them.It's a beter approach if you use these with vitual enviroment.

```
virtualenv venv
source venv/bin/activate
pip install Django
git clone https://github.com/Glyphack/restaurant-website.git
cd restaurant-website
```
### Installing

A step by step series of examples that tell you how to get a development env running

After cloning the repository you need to put a SECRET_KEY in setting,py under the RestaurantApp
like this
```
SECRET_KEY = 'blah#blah#blah'
```
in the root folder of application you can run django commands with manage.py(I've done the migration but feel free to do it on your own, https://docs.djangoproject.com/en/2.0/topics/migrations).
```
python manage.py runserver
```
enter your localhost you can browse website see menu and index and order the food(for now).

p.s: because of some prohibition issue I couldn't implement a foreign payment method (eg.PayPal).I can only use payment methods of my own country, I'll be looking to find a way to implement a good payment method.
## Running the tests

each test is under the app directory eg.foodsapp/test.py you can run tests using command
```
./manage.py test
```
or
```
python manage.py test appname
```

## Built With

* [Django](https://www.djangoproject.com/) - The web framework used

## Contributing
will be added soon.
<!-- Please read [CONTRIBUTING.md]() for details on our code of conduct, and the process for submitting pull requests to us. -->

## Authors

* **Shaygan** - *Initial work* - [Glyphack](https://github.com/Glyphack)

list of contributers will be added too.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
