import requests

response = requests.get('https://coinmarketcap.com/')

response_text = response.text

response_parse = response_text.split("<span>")
bitcoin_list = []

for parse in response_parse:
    if parse.startswith("$"):
        for parse_2 in parse.split("</span>"):
            if parse_2.startswith("$"):
                print(parse_2)
                bitcoin_list.append(parse_2)

bitcoin_exchange = bitcoin_list[0]
print(bitcoin_exchange)

