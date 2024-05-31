# Przykładowa lista studentów
students = [
    {"name": "Alice", "age": 23, "grades": [85, 90, 78]},
    {"name": "Bob", "age": 22, "grades": [70, 65, 68]},
    {"name": "Charlie", "age": 24, "grades": [50, 45, 40]},
    {"name": "David", "age": 21, "grades": [95, 92, 88]},
    {"name": "Eve", "age": 23, "grades": [55, 60, 58]},
]

# Funkcja pomocnicza do obliczania średniej ocen
def calculate_average(grades):
    return sum(grades) / len(grades)

# Programowanie funkcyjne

# Używamy funkcji wyższego rzędu 'filter' z funkcją lambda do wybrania studentów, którzy zdali
passing_students = filter(lambda student: calculate_average(student['grades']) >= 60, students)

# Używamy funkcji wyższego rzędu 'map' z funkcją lambda do przekształcenia studentów na słowniki z imieniem i średnią ocen
students_with_averages = map(lambda student: {
    "name": student["name"],
    "average": calculate_average(student["grades"])
}, passing_students)

# Funkcja do sortowania studentów po średniej ocen (malejąco)
def sort_by_average(student):
    return student['average']

# Używamy funkcji 'sorted' z kluczem sortującym do posortowania studentów po średniej ocen w kolejności malejącej
sorted_students = sorted(students_with_averages, key=sort_by_average, reverse=True)

# Wyświetlenie wyników
for student in sorted_students:
    # Wykorzystujemy funkcję formatowania stringów do wyświetlenia imienia i średniej ocen studenta
    print(f"Name: {student['name']}, Average Grade: {student['average']:.2f}")

# Wyjaśnienie, gdzie wykorzystujemy programowanie funkcyjne:

# 1. Funkcje wyższego rzędu:
#    - 'filter' jest funkcją wyższego rzędu, która przyjmuje funkcję lambda i listę 'students',
#      zwracając iterator z elementami, które spełniają warunek funkcji lambda.
#    - 'map' jest funkcją wyższego rzędu, która przyjmuje funkcję lambda i iterator 'passing_students',
#      zwracając nowy iterator z przekształconymi elementami.

# 2. Funkcje anonimowe (lambda):
#    - Używamy funkcji lambda w 'filter' i 'map' do zdefiniowania logiki przekształceń i warunków bez konieczności
#      definiowania osobnych nazwanych funkcji.

# 3. Niezmienność i brak efektów ubocznych:
#    - Wszystkie funkcje są czyste, tzn. nie modyfikują stanu zewnętrznego i zawsze zwracają ten sam wynik dla tych samych danych wejściowych.

# 4. Kompozycja funkcji:
#    - Wyniki funkcji 'filter' są bezpośrednio używane jako dane wejściowe dla funkcji 'map', a wyniki 'map' dla 'sorted',
#      co pokazuje, jak możemy komponować funkcje razem w stylu funkcyjnym.
