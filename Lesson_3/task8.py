# Три друга взяли вещи в поход. Сформируйте
# словарь, где ключ — имя друга, а значение —
# кортеж вещей. Ответьте на вопросы:
# Какие вещи есть у всех друзей кроме одного
# и имя того, у кого данная вещь отсутствует
# Для решения используйте операции
# с множествами. Код должен расширяться
# на любое большее количество друзей.

hike = {
    'Aaz': ("спички", "спальник", "дрова", "топор"),
    'Skeeve': ("спальник", "спички", "вода", "еда"),
    'Tananda': ("вода", "спички", "косметичка"),
}

# Какие вещи уникальны,
all_things = set()
for friend in hike:
    all_things.update(hike[friend])

hike_copy = hike.copy()
# Какие вещи взяли все три друга
common_things = set(hike_copy.popitem()[1])
for friend in hike_copy:
    common_things &= set(hike_copy[friend])

# things have all not common
not_common_things = dict()
for name in hike:
    not_common_things[name] = set(hike[name]) - common_things

# things have
# diff_things = None
# name = None
# for friend, things in hike.items():
#     diff_things = not_common_things - set(things)

# TODO: find another solution
standalone_things = dict()
for master_key, master_value in hike.items():
    for slave_key, slave_value in hike.items():
        if master_key != slave_key:
            if not standalone_things.get(master_key):
                standalone_things[master_key] = set(master_value)
            else:
                standalone_things[master_key] -= set(slave_value)

# some reason
# TODO: find another solution
dublicates = set(all_things)
for value in standalone_things.values():
    dublicates -= value

not_have_things = {}
for key, value in hike.items():
    other = (set(value) ^ dublicates) - set(standalone_things[key])
    not_have_things[key] = other

print(f"list of all things: {all_things}")
print(f"common things: {common_things}")
print(f"not common things: {not_common_things}")
print(f"have only one friend: {standalone_things}")
print(f"friend not have thing like another: {not_have_things}")
