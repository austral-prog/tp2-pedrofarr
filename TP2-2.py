The result of X comes first in the dictionary than Y is True/False.
The result of Y comes first in the dictionary than X is True/False.

country_x = "Bangladesh"
country_y = "Barbados"

result_x = country_x < country_y
result_y = country_y < country_x

print(f"The result of {country_x} comes first in the dictionary than {country_y} is {result_x}.")
print(f"The result of {country_y} comes first in the dictionary than {country_x} is {result_y}.")