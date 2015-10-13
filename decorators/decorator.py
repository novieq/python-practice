from functools import wraps
#One problem (easily solved) is that wrapping price_with_tax with currency changes its .__name__ and .__doc__ to that of
#  currency, which is certainly not what we want. The functools modules contains a useful tool, wraps, which will restore
# these values to what we would expect them to be.

__author__ = 'meramac'

def currency(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            return '$' + str(f(*args, **kwargs))

        return wrapper

class Product():

    #price = _price
    @currency
    def price_with_tax(self, tax_rate_percentage):
        """Return the price with *tax_rate_percentage* applied.
        *tax_rate_percentage* is the tax rate expressed as a float, like
        "7.0" for a 7% tax rate."""
        return 100 * (1 + (tax_rate_percentage * .01))

    #To create a decorator, we create a function which takes a function(the function to be decorated) and returns a
    # function(the decorated function) - the original function with the decoration applied


product = Product()
print(product.price_with_tax(10))