import requests

def date():
    url = 'https://russianwarship.rip/api/v2/statistics/latest'
    r = requests.get(url).json()
    date_ = r['data']['date']
    return date_

def day():
    url = 'https://russianwarship.rip/api/v2/statistics/latest'
    r = requests.get(url).json()
    day_ = r['data']['day']
    return day_

def personnel(item):
    url = 'https://russianwarship.rip/api/v2/statistics/latest'
    r = requests.get(url).json()
    if item == 'total':
        total = r['data']['stats']['personnel_units']
        return total
    elif item == 'quantity':
        quantity = r['data']['increase']['personnel_units']
        return quantity
    else:
        error = 'error: invalid argument'
        return error

def tanks(item):
    url = 'https://russianwarship.rip/api/v2/statistics/latest'
    r = requests.get(url).json()
    if item == 'total':
        total = r['data']['stats']['tanks']
        return total
    elif item == 'quantity':
        quantity = r['data']['increase']['tanks']
        return quantity
    else:
        error = 'error: invalid argument'
        return error

def armoured_fighting_vehicles(item):
    url = 'https://russianwarship.rip/api/v2/statistics/latest'
    r = requests.get(url).json()
    if item == 'total':
        total = r['data']['stats']['armoured_fighting_vehicles']
        return total
    elif item == 'quantity':
        quantity = r['data']['increase']['armoured_fighting_vehicles']
        return quantity
    else:
        error = 'error: invalid argument'
        return error
    
def artillery_systems(item):
    url = 'https://russianwarship.rip/api/v2/statistics/latest'
    r = requests.get(url).json()
    if item == 'total':
        total = r['data']['stats']['artillery_systems']
        return total
    elif item == 'quantity':
        quantity = r['data']['increase']['artillery_systems']
        return quantity
    else:
        error = 'error: invalid argument'
        return error
    
def mlrs(item):
    url = 'https://russianwarship.rip/api/v2/statistics/latest'
    r = requests.get(url).json()
    if item == 'total':
        total = r['data']['stats']['mlrs']
        return total
    elif item == 'quantity':
        quantity = r['data']['increase']['mlrs']
        return quantity
    else:
        error = 'error: invalid argument'
        return error
    
def aa_warfare_systems(item):
    url = 'https://russianwarship.rip/api/v2/statistics/latest'
    r = requests.get(url).json()
    if item == 'total':
        total = r['data']['stats']['aa_warfare_systems']
        return total
    elif item == 'quantity':
        quantity = r['data']['increase']['aa_warfare_systems']
        return quantity
    else:
        error = 'error: invalid argument'
        return error
    
def planes(item):
    url = 'https://russianwarship.rip/api/v2/statistics/latest'
    r = requests.get(url).json()
    if item == 'total':
        total = r['data']['stats']['planes']
        return total
    elif item == 'quantity':
        quantity = r['data']['increase']['planes']
        return quantity
    else:
        error = 'error: invalid argument'
        return error

def helicopters(item):
    url = 'https://russianwarship.rip/api/v2/statistics/latest'
    r = requests.get(url).json()
    if item == 'total':
        total = r['data']['stats']['helicopters']
        return total
    elif item == 'quantity':
        quantity = r['data']['increase']['helicopters']
        return quantity
    else:
        error = 'error: invalid argument'
        return error
    
def vehicles(item):
    url = 'https://russianwarship.rip/api/v2/statistics/latest'
    r = requests.get(url).json()
    if item == 'total':
        total = r['data']['stats']['vehicles_fuel_tanks']
        return total
    elif item == 'quantity':
        quantity = r['data']['increase']['vehicles_fuel_tanks']
        return quantity
    else:
        error = 'error: invalid argument'
        return error

def warships(item):
    url = 'https://russianwarship.rip/api/v2/statistics/latest'
    r = requests.get(url).json()
    if item == 'total':
        total = r['data']['stats']['warships_cutters']
        return total
    elif item == 'quantity':
        quantity = r['data']['increase']['warships_cutters']
        return quantity
    else:
        error = 'error: invalid argument'
        return error
    
def cruise_missiles(item):
    url = 'https://russianwarship.rip/api/v2/statistics/latest'
    r = requests.get(url).json()
    if item == 'total':
        total = r['data']['stats']['cruise_missiles']
        return total
    elif item == 'quantity':
        quantity = r['data']['increase']['cruise_missiles']
        return quantity
    else:
        error = 'error: invalid argument'
        return error
    
def uav_systems(item):
    url = 'https://russianwarship.rip/api/v2/statistics/latest'
    r = requests.get(url).json()
    if item == 'total':
        total = r['data']['stats']['uav_systems']
        return total
    elif item == 'quantity':
        quantity = r['data']['increase']['uav_systems']
        return quantity
    else:
        error = 'error: invalid argument'
        return error

def special_military_equip(item):
    url = 'https://russianwarship.rip/api/v2/statistics/latest'
    r = requests.get(url).json()
    if item == 'total':
        total = r['data']['stats']['special_military_equip']
        return total
    elif item == 'quantity':
        quantity = r['data']['increase']['special_military_equip']
        return quantity
    else:
        error = 'error: invalid argument'
        return error
    
def atgm_srbm_systems(item):
    url = 'https://russianwarship.rip/api/v2/statistics/latest'
    r = requests.get(url).json()
    if item == 'total':
        total = r['data']['stats']['atgm_srbm_systems']
        return total
    elif item == 'quantity':
        quantity = r['data']['increase']['atgm_srbm_systems']
        return quantity
    else:
        error = 'error: invalid argument'
        return error