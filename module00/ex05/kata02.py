kata = (2019, 9, 25, 3, 30)

# On récupère les valeurs : la virgule transfert les valeurs d'un élément vers l'autre (tuple vers tuple)
(year, month, day, hour, minute) = kata
print(f"{month:02d}/{day:02d}/{year} {hour:02d}:{minute:02d}")