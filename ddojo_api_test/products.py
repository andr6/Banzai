#!/usr/bin/python3

# import the package
from defectdojo_api import defectdojo

# setup DefectDojo connection information
host = 'http://localhost:8000'
api_key = '8cbde70ff6d1b7cbad4d0e2bada5ec270f2725f8'
user = 'admin'

# instantiate the DefectDojo api wrapper
dd = defectdojo.DefectDojoAPI(host, api_key, user, debug=True)

# If you need to disable certificate verification, set verify_ssl to False.
# dd = defectdojo.DefectDojoAPI(host, api_key, user, verify_ssl=False)

'''
PRODUCTS API
'''

# Create a product
prod_type = 1 #1 - Research and Development, product type
product = dd.create_product("API Product Test", "This is a detailed product description.", prod_type)

if product.success:
    # Get the product id
    product_id = product.id()
    print "Product successfully created with an id: " + str(product_id)

#List Products
products = dd.list_products()

if products.success:
    print(products.data_json(pretty=True))  # Decoded JSON object

    for product in products.data["objects"]:
        print(product['name'])  # Print the name of each product
else:
    print products.message