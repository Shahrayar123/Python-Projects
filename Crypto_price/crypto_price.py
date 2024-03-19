import requests
from bs4 import BeautifulSoup
from tabulate import tabulate

url = 'https://coinranking.com/'
r = requests.get(url)

soup = BeautifulSoup(r.text, 'html.parser')

translation_table = str.maketrans({'\n': None, '$': None})

table = soup.select('tr.table__row')
result_list = []

for i in table:
    row_data = []

    subtitle = i.select_one('span.profile__subtitle')
    if subtitle:
        subtitle_text = subtitle.text.replace('Top loser', '').replace('Top gainer', '').translate(translation_table).strip()
        row_data.append(subtitle_text if subtitle_text not in ['Top loser', 'Top gainer'] else '')

    valuta_list = i.select('div.valuta')
    for valuta in valuta_list:
        valuta_text = valuta.text.translate(translation_table).strip()
        row_data.append(valuta_text)

    change = i.select_one('div.change')
    if change:
        change_text = change.text.translate(translation_table).strip()
        row_data.append(change_text)
    else:
        row_data.append('Change not found')

    result_list.append(row_data)

print(tabulate(result_list[1:]))