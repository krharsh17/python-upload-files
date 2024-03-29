import requests

# define the relative path of the sample file
file_path = "../samples/sample.pdf"

# store the target API URL
target_url = "https://httpbin.org/post"

# create a reference to the file
target_file = open(file_path, "rb")

# send the request
response = requests.post(target_url, files = {"form_field_name": target_file})

# check the result
if response.ok:
    print("Upload complete")
    print(response.text)
else:
    print("Something went wrong")