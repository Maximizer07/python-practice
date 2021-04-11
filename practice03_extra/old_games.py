import csv
import matplotlib.pyplot as plt

with open('source/GAMES.csv', encoding='utf-8') as f:
    reader = csv.reader(f, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    games_by_year = [[]]
    game_genres_year = []
    game_genres_count = [[]]
    genres = []
    for row in reader:
        if row[1] not in genres:
            genres.append(row[1])
        if row[3].isdigit():
            # 1 график
            if len(games_by_year) == 1:
                games_by_year[0].append(row[3])
                games_by_year.append([1])
            else:
                if row[3] in games_by_year[0]:
                    games_by_year[1][games_by_year[0].index(row[3])] += 1
                else:
                    games_by_year[0].append(row[3])
                    games_by_year[1].append(1)

            # 2 график
            if len(game_genres_year) == 0:
                game_genres_year.append(row[3])
                game_genres_count[0].append([row[1]])
                game_genres_count[0].append([1])
            else:
                if row[3] in game_genres_year:
                    index = game_genres_year.index(row[3])
                    if row[1] in game_genres_count[index][0]:
                        game_genres_count[index][1][game_genres_count[index][0].index(row[1])] += 1
                    else:
                        game_genres_count[index][0].append(row[1])
                        game_genres_count[index][1].append(1)
                else:
                    # print(game_genres_year, game_genres_count)
                    game_genres_year.append(row[3])
                    game_genres_count.append([[row[1]], [1]])

    # Парная сортировка по убыванию
    x = zip(games_by_year[1], games_by_year[0])
    xs = sorted(x, key=lambda tup: tup[0], reverse=True)
    game_count = [x[0] for x in xs][:10]
    year = [x[1] for x in xs][:10]

    plt.figure(1)
    plt.title('Какие годы были самыми популярными с точки зрения выхода игр')
    plt.xlabel('Год')
    plt.ylabel('Количество игр')
    plt.bar(year, game_count)

    plt.figure(2)
    plt.figure(figsize=(15, 15))
    for genre in genres:
        lst = []
        for i in range(len(game_genres_year)):
            if genre in game_genres_count[i][0]:
                lst.append(game_genres_count[i][1][game_genres_count[i][0].index(genre)])
            else:
                lst.append(0)
        plt.plot(game_genres_year, lst, label=genre)
    plt.title('Какие жанры были популярны в различные периоды времени')
    plt.xlabel('Год')
    plt.ylabel('Количество игр')
    plt.legend(loc=0)
    plt.show()
