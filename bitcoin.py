import requests
import sys

try:
    if len(sys.argv) == 2:
        cash = float(sys.argv[1])
        response = requests.get(
            "https://rest.coincap.io/v3/assets/bitcoin?apiKey=0281e502a58239efd9f5c93ebeebfd9cd3dd1866e38bb9b6d8f6e60f70f87f83"
        )
    else:
        raise requests.RequestException
except (requests.RequestException, ValueError):
    sys.exit("Invalid Input!.Enter a Number Please.")

else:
    information = response.json()
    # print(information)

    for result in information.keys():
        if result == "data":
            words = information[result]
            for word in words.keys():
                if word == "priceUsd":
                    amount = float(words[word])
                    amount = cash * amount
                    print(f"${amount:,.4f}")
