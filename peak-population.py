class Person:
    def __init__(self, name, birth_year, death_year):
        self.name = name
        self.birth_year = birth_year
        self.death_year = death_year

def find_peak_population(people:list) -> int:
    min_birth_year = min([p.birth_year for p in people])
    max_birth_year = max([p.birth_year for p in people])
    deltas = get_deltas_per_year(people, min_birth_year, max_birth_year)
    return get_peak_year(deltas)+min_birth_year

def get_deltas_per_year(people, min_birth_year, max_birth_year):
    deltas_list = [0]*(max_birth_year-min_birth_year+1)
    for p in people:
        add_delta(deltas_list, p.birth_year-min_birth_year, 1)
        add_delta(deltas_list, p.death_year-min_birth_year+1, -1)
    return deltas_list

def add_delta(deltas_list, year_idx, value):
    if year_idx < len(deltas_list):
        deltas_list[year_idx] += value

def get_peak_year(deltas):
    print(deltas)
    peak_year_idx = 0
    running_max = 0
    max_population = 0
    for idx, pop_delta in enumerate(deltas):
        running_max += pop_delta
        if running_max > max_population:
            max_population = running_max
            peak_year_idx = idx
    return peak_year_idx

if __name__ == "__main__":
    people = [ 
        Person('a', 2010, 2050),
        Person('a', 1959, 1999),
        Person('a', 1850, 1900),
        Person('a', 1920, 2000),
        Person('a', 1890, 1959),
        Person('a', 2010, 2070),
        Person('a', 1700, 1750),
        Person('a', 1870, 1900)
    ]

    print(find_peak_population(people=people))