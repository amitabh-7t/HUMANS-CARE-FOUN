import pyshorteners
url = input("enter the url:")
shortener = pyshorteners.Shortener()
short_url = shortener.tinyurl.short(url)
print(f"Shortened URL: {short_url}")