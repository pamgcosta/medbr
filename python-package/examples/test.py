import webbrowser
from medbr import facilities, mortality, birth


facilities(city=355030).save('facilities.html')
webbrowser.open('facilities.html')

beds(city=355030).save('beds.html')
webbrowser.open('beds.html')

beneficiaries(city=355030).save('beneficiaries.html')
webbrowser.open('beneficiaries.html')

birth(start_at='2021-01-01', end_at='2022-01-01').save('birth.html')
webbrowser.open('birth.html')

covid_machine(city=355030).save('covid_machine.html')
webbrowser.open('covid_machine.html')

mortality(start_at='2021-01-01', end_at='2022-01-01').save('mortality.html')
webbrowser.open('mortality.html')

plancoverage(city=355030).save('plancoverage.html')
webbrowser.open('plancoverage.html')