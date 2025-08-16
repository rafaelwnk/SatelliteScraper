import pandas as pd

from services.scraper import Scraper

while True:
    user_input = input("Digite a quantidade de páginas que deseja coletar: ")

    if not user_input.isdigit():
        print("Você deve digitar um número inteiro. Tente novamente.")
        continue
    
    pages = int(user_input)
    break

scraper = Scraper()
satellites = scraper.get_data(pages)

df = pd.DataFrame([{'Nome': satellite.name, 'Estado Orbital': satellite.orbital_status, 'Designação': satellite.designation, 'Órbita': satellite.orbit} for satellite in satellites])
df.to_csv('satellites.csv', index=False)

print(f"Coleta concluída com sucesso! {len(satellites)} satélites coletados.")