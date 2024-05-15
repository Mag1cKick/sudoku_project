# sudoku_project
розподіл:
1)Багатир-Захарченко Вероніка судоку і бек
2)Діжак Назар лабіринт і фронт
3)Кравчук Андрій розфарбовку і фронт
4)Слаблюк Назар кросворд і бек

Судоку
Наша задача полягає у вирішенні судоку, застосовуючи алгоритм зворотного відстеження. Судоку - це гра, в якій гравець має заповнити сітку 9x9 числами від 1 до 9 так, щоб кожне число з'являлося лише раз у кожному рядку, кожному стовпці та кожному квадраті 3x3. Алгоритм зворотного відстеження - це метод, який систематично перебирає всі можливі комбінації до досягнення розв'язку. За допомогою Фласку ми передаємо значення з клітинок головоломки в функцію пайтон, де перетворюєио один великий список значень на список списків, щоб було зручно працювати, а потім викликаємо функцію solve_sudoku. Якщо розв'язок існує, результат відображається як рядок чисел, в іншому випадку повідомляється про відсутність розв'язку.

Функція solve_sudoku(board):
Основна функція для розв'язання судоку. Вона рекурсивно викликається, пробуючи вставити числа в порожні комірки до досягнення повного розв'язку. Кожен раз, коли вона викликається, вона шукає порожню комірку за допомогою find_empty_location, а потім використовує is_safe, щоб перевірити, чи можна вставити число. Якщо можна, воно вставляється, і рекурсивно викликається для наступної комірки. Якщо не можна вставити жодне число, функція повертає False, і цикл розгортається назад, спробовавши інші варіанти.

Функція find_empty_location(board):
Шукає порожню комірку у судоку (комірку зі значенням 0) і повертає її координати (row, col). Якщо такої немає, то повертається None.

Функція is_safe(board, row, col, num):
Перевіряє, чи можна вставити число num у комірку board[row][col] без порушення правил гри. Вона перевіряє рядок, стовпець та квадрат 3x3, щоб упевнитися, що число не з'являється вже у цих областях. Для перевірки рядка функція просто переглядає всі комірки вказаного рядка row. Аналогічно, для перевірки стовпця функція просто переглядає всі комірки вказаного стовпця col. Блокова перевірка трохи складніша. Спочатку функція визначає координати верхнього лівого кута квадрату 3x3, до якого належить комірка (row, col). Після цього вона переглядає всі комірки у визначеному квадраті. Якщо ж усі три перевірки пройшли успішно для даного числа num у комірці board[row][col], це означає, що дане число можна вставити у вказану комірку без порушення правил судоку, і функція повертає True.

Лабіринт
Мета завдання - написати програму, яка вирішуватиме лабіринти за допомогою бектрекінгу. 

def exploreMaze(self, row, col):
Суть роботи алгоритму дуже проста - стіни позначені цифрою 1, вільні території - 0, а кінець - 2. Під час проходу лабіринту, шлях, який ми обрали стає числом 3, якщо ми зайшлм у глухий кут, то починається бектрекінг, який триває доти, доки навколо "голови" нашої "змійки" не з'явиться хоча б одна клітинка, в яку можливо зайти (шлях, на якому ми використовували бектрекінг заміняється числом 4, щоб не заходити у нього знову). Ця схема триває доти, доки не знайдеться вихід, або не залишиться жодного шляху, у який можна зайти.

візуалізація:

function createMaze():
Ця функція ітеративно створює мапу з кнопок заданого розміру і присвоює кожній кнопці дію "ToggleCell" та ідентифікатор, що згодом буде використовуватись для того, щоб показати рішення лабіринту користувачу. Також, для більш естетичного вигляду, зовнішня лінія завжди буде стінами, які неможливо прибрати. При створенні кожної кнопки, до списку maze додається новий елемент, який відображає колір створеної клітинки. У кінці ми отримуємо двовимірний масив, перша та остання лінія якого по вертикалі і горизонталі - це одинички, а всередині песта територія - нулі.

function toggleCell(event):
При натисканні на будь-яку кнопку у лабіринці викликається ця функція. Спочатку ми отримуємо координати кнопки у масиві, потім перевіряємо, чи не було натиснуто перед цим "SetStart" або "SetEnd" (про це згодом). Якщо ні, то ми зберігаємо поточний колір у savedColors, заміняємо колір кнопки на протилежний і зберігаємо зміну у maze. Збереження у savedColors зроблено для того, щоб можна було повернутися до попереднього кольору при подвійному натиску або розставлянні старту та кінця.
Якщо все ж треба поставити старт чи кінець, то спочатку перевіряємо, чи немає їх уже на мапі, якщо є - то ми заміняємо колір кнопки на їх місці на попередній(savedColors) і міняємо значення у maze, якщо ми поставили кінець, або зберігаємо координати початку для ініціаціїї алгоритму у Flask.

Функції setStart, setEnd та setPoint зроблені для кращої роботи з кнопками, вони блокують кнопку яку ви натиснули, доки не буде зроблений вибір точки та дбають про те, щоб старт/фініш не можна було закрити стіною (теж блокують їх)

function solveMaze():
Спочатку функція перевіряє чи стоять на лабіринті і початок, і кінець, якщо ні, то користувачу виводить повідомлення alert("Please set both start and end points."). Якщо стоять, то ми передаємо maze та startCoords і надсилаємо їх у фласк для запуску алгоритму, після обробки ми отримуємо відповідь і обробляємо її в залежності від того, чи лабіринт вирішується чи ні.
Якщо не вирішується - alert("There is no solution!"), якщо є вирішення - викликається updateMazeDisplay()

function updateMazeDisplay(newMaze):
Функція ітеративно проходиться по всіх кнопках на екрані по ідентифікатору та перефарбовує їх в залежності від newMaze, (0: free space, 1: wall, 2: start, 3: end, 4: backtrack)

Граф
Суть цієї задачі у розфарбуванні графу, тобто потрібно розфарбувати даний граф так, щоб інцидентні вершини не були одного кольору. Для початку потрібно задати граф, тому створюємо власний клас Graph з атрибутами num_vertices(кількість вершин), adjacency_matrix(матриця суміжності) та node_colors(кольори для вузлів). Створюємо функцію color_graph для вирішення задачі. Спершу робимо список colors і призначаємо кожній вершині графа значення -1, тобто вершина не зафарбована. Визначаємо допоміжну функцію is_safe(vertex, color) для перевірки чи можна зафарбувати вершину vertex у колір color без порушення умови: перевіряється чи не забарвлені сусідні вершини у колір color. Далі визначаєм ще одну допоміжну функцію get_available_color(vertex), яка використовує раніше визначену функцію is_safe() для пошуку доступного кольору. Потім проходимся по всім вершинам графа і використовуємо get_available_color() для знаходження досутпного кольору. Одразу після цього створюється список available_colors, який містить рядки з кольорами у форматі RGB, також ці кольори генеруються рандомно. Потім зі списку available_colors присвоюємл кольори для раніше створеного colors. Після всіх операцій зберігаємо colors у node_colors. Для вирішення задачі використано алгоритм бектрекінгу.

Для візуалізації визначаємо допоміжну функцію add_edge(src, dest) яка додає ребро, а потім використовуємо цю функцію в add_random_edges(num_edges) яка створює кількість рандомних ребер задану користувачем. Далі використовуємо color_graph() для вирішення задачі. Визначаємо функцію to_dot(), яка конвертує граф у .dot формат, який використовується для бібліотеки graphviz. Далі створюємо png-файл з нашим графом і можемо його розглянути.

Кросворд
Всі алгоритми працюють через бектрекінг і кросворд не вийняток. Для початку ми робимо матрицю в якій будемо проводити наші пошуки місць для підстановки слів. Для того щоб працювала функція нам потрібно прийняти саму матрицю від користувача, за допомогою фласку та хтмл. Також нам потрібно отримати набір слів для розстановки, адже наша ціль не розвʼязати кросворд, а розставити у ньому слова так, щоб його потім можна було поставити на вітрини магазинів з запитаннями для вирішення. Тож ми беремо слова і нашу матрицю, матрицю попередньо потрібно ще перетворити в матрицю, адже воно приймає стрічку з ентерами, перероблюємо її в ліст за допомогою спліт і стріп. Потім ми передаємо їх у клас cross1, у якому ми маємо ініт з словами, бордою та шляхами, якими можна розвʼязати кросворд. Тож далі перейдемо до функцій, адже вони найважливіші.

Функція hor_ch(x, y, grid, word) приймає позиції, у які можна вставити слова за допомогою х, у а також ми передаємо дошку, на яку ми і будемо вставляти слово і ми потім записуємо його в дошку, якщо у нас не можливо це зробити то тоді 1 символ ми замінюємо на 1 і тоді просто повертаємо дошку. Так ми записуємо горизонтально наше слово, надіючись що воно не перетнеться з іншими словами і пройде заповнення. Також ми передаємо слово, яке і будемо записувати.

Функція ver_ch(x, y, grid, word) приймає позиції, у які можна вставити слова за допомогою х, у а також ми передаємо дошку, на яку ми і будемо вставляти слово і ми потім записуємо його в дошку, якщо у нас не можливо це зробити то тоді 1 символ ми замінюємо на 1 і тоді просто повертаємо дошку. Так ми записуємо вертикально наше слово, надіючись що воно не перетнеться з іншими словами і пройде заповнення. Також ми передаємо слово, яке і будемо записувати.

Функція placements(self, grid, index, v, h) приймає також дошку, це необхідно бо вона працює рекурсивно і потім буде потрібно закидати нову дошку і нову, тому ми не можемо просто використовувати селф грід, також ми передаємо індекс для зміни слів які ми беремо як на початку так і під кінець нашого алгоритму, передаємо вертикальну довжину і горизонтальну щоб ми могли зробити поле будь-якого розміру, прямокутного а то буде все дуже погано. Тож далі ми маємо знайти ту довжину, на яку ми можемо розраховувати при підстановці слова і далі ми намагаємося підставити його вертикально у всі можливі вертикальні позиції також використовуючи бектрекінг, адже якщо ми знаходимо можливу підстановку для слова, то тоді у нас спрацьовує алгоритм, адже ми беремо нове слово і намагаємося його всунути горизонтально потім ще повертаємось і беремо горизонтально інше, коли не можна то вертикально всі можливі варіанти, потім знову для інших підстановок і так далі за допомогою алгоритму бектрекінг. Потім, коли у нас завершаться слова, які ми можемо підставити ми будемо додавати цей варіант до селф вейс і потім вже виводити на сайті у новому вікні всі варіанти, попередньо називаючи їх за допомогою формул, прописаних у аштімлі.

Висновок
Наші коди розвʼязують все за допомогою алгоритму бектрекінгу, який точно знайде ровʼязок для лабіринту, судоку і інших головоломок якщо він існує, так, він не є найефективнішим і це ми можемо бачити на прикладі лабіринту якщо залишити дошку повністю пустою і лише десь поставити старт і кінець то тоді видно, що алгоритм і де дуже довго і використовує набагато більше клітинок ніж потрібно для розвʼязку, але таке було завдання тож алгоритм є робочим і корисним для простого врішення будь - яких задач, але при цьому це не є ефективний алгоритм для цього, тож якщо у вас великий проєкт, то краще витратити на 10 хв більше часу і знайти в гуглі нормальний алгоритм для розвʼязку задат, або у вас можуть виникати проблеми з памʼяттю та часом виконання, що не є добре. Тепер ми вміємо робити бектрекінг на високому рівні і зможемо на його основі писати кращі алгоритми розвʼязку задач.
