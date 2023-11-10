import webbrowser
from medbr import facilities, mortality, birth, plancoverage, beds, beneficiaries


facilities(city=355030).save('facilities.html')
webbrowser.open('facilities.html')

# no filters allowed
beds().save('beds.html')
webbrowser.open('beds.html')

# no filters allowed
beneficiaries().save('beneficiaries.html')
webbrowser.open('beneficiaries.html')

birth(start_at='2021-01-01', end_at='2022-01-01').save('birth.html')
webbrowser.open('birth.html')

# covid_machine(city=355030).save('covid_machine.html')
# webbrowser.open('covid_machine.html')

# filters start_at and end_at
mortality(start_at='2021-01-01', end_at='2022-01-01').save('mortality.html')
webbrowser.open('mortality.html')

# filters by state or operator
plancoverage(ufs=['SP', 'RJ']).save('plancoverage.html')
webbrowser.open('plancoverage.html')