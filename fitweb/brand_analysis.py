from fuzzywuzzy import fuzz

# Example list of brand names
brand_names = [
    "Adidas",
    "Adidaz",
    "Adidus",
    "Nike",
    "Nik",
    "Puma",
    "Pumma",
    "Reebok",
    "Rebok",
    "Rebuk"
]

# Function to find similar brand names
def find_similar_brands(brand_list):
    similar_brands = {}
    for brand in brand_list:
        similar_brands[brand] = [other_brand for other_brand in brand_list if brand != other_brand and fuzz.ratio(brand, other_brand) > 80]
    return similar_brands

similar_brands = find_similar_brands(brand_names)

# Print similar brand names
for brand, similar in similar_brands.items():
    if similar:
        print(f"Similar brands to '{brand}': {', '.join(similar)}")
