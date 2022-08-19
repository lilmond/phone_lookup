from bs4 import BeautifulSoup as htmlparser
import requests

def lookup(phone_number):
    http = requests.get(f"https://free-lookup.net/{phone_number}")
    html = htmlparser(http.text, "html.parser")
    infos = html.findChild("ul", {"class": "report-summary__list"}).findAll("div")

    return {k.text.strip(): infos[i+1].text.strip() if infos[i+1].text.strip() else "No informations" for i, k in enumerate(infos) if not i % 2}

def main():
    while True:
        try:
            phone_number = input("Phone number: ").strip().replace("-", "").replace(" ", "").replace("+", "")
        except KeyboardInterrupt:
            return

        try:
            infos = lookup(phone_number)
        except AttributeError:
            print("Error: Invalid phone number\n")
            continue

        [print(f"{info}: {infos[info]}") for info in infos]
        print("\n")

if __name__ == "__main__":
    main()
