from src.die_table import DieTable

if __name__ == '__main__':
    die_table = DieTable('imgs/IMG_2834.jpg')
    die_table.find_die()
    print(die_table.die_col, die_table.die_row)
