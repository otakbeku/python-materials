# Introduction to Python



**Note**: Jika tidak memungkinkan untuk menginstall Anaconda/Miniconda, silahkan menggunakan [Repl.it](https://Repl.it)

## Install python using Anaconda

Anaconda merupakan package manager khusus untuk Python. Perubahan versi dari package diatur oleh Conda. Anaconda umum digunakan untuk kebutuhan projek yang dibentuk dengan Python yang kebanyakan berkaitan dengan data. Anaconda dapat diunduh di laman [berikut](https://www.anaconda.com/download/). Unduh versi 3.

[Video install di Windows](https://www.youtube.com/watch?v=5mDYijMfSzs)

[Video install di Linux](https://www.youtube.com/watch?v=DY0DB_NwEu0)

[Video install di Max](https://www.youtube.com/watch?v=daVgEXjv6DE)

## Install python using Miniconda

Miniconda merupakan opsi dari Anaconda yang merupakan package manager untuk Python. Untuk menginstallnya, silahkan diunduh di laman [berikut](https://docs.conda.io/en/latest/miniconda.html). Unduh versi 3.

## Pilih Anaconda atau Miniconda?

Dikutip dari laman dokumentasinya

*Choose Anaconda if you:*

- *Are new to conda or Python.*
- *Like the convenience of having Python and over 150 scientific packages automatically installed at once.*
- *Have the time and disk space---a few minutes and 300 MB.*
- *Do not want to individually install each of the packages you want to use.*

*Choose Miniconda if you:*

- *Do not mind installing each of the packages you want to use individually.*
- *Do not have time or disk space to install over 150 packages at once.*
- *Want fast access to Python and the conda commands and you wish to sort out the other programs later.*

Dalam sesi ini, jika memungkinkan gunakan Anaconda karena ada beberapa package yang sudah terinstal dengan baik. Namun jika ada kendala seperti tidak ada ruang untuk menggunakan Anaconda, opsi Miniconda dapat digunakan.

Pastikan Conda terdaftar di path agar dapat diakses langsung dari terminal atau command prompt.

Jika sudah terinstall, buka terminal/command prompt, ketik perintah berikut

Linux/Mac:

`conda list | grep python`

Windows:

`conda list | findstr python`

Pastikan versi yang terinstall adalah versi 3.7. Untuk sesi ini versi yang digunakan adalah versi 3.6. Jalankan perintah berikut

`conda install python=3.6 pip numpy matplotlib pandas -y`

Ketika proses instalasinya sudah selesai, ketik `python`, maka akan muncul interactive REPL. Untuk mengecek library tersebut sudah terinstall, ketik

`import pandas`

`import maptlotlib`

`import numpy`

Jika tidak ada galat yang muncul, maka library tersebut sudah terinstal dengan baik.



## Data Types and Built-in Functions

Layaknya bahasa pemograman pada umum, Python memiliki beberapa tipe data yang umum digunakan, antara lain:

1.  `int`: Integer. Semua angka tanpa koma
2.  `float`: float. Semua angka dengan koma
3.  `Complex`: complex number, kombinasi dari bilangan riil dan imaginer. (`1+2j`)
4.  `str`: String. Penulisannya menggunakan single-quote, double-quote and triple-quote
5.  `Boolean`: `True` or `False`

Built-in functions yang umum digunakan, antara lain:

1.  `abs()`: mengembalikan nilai absolut
2.  `max()`: mengembalikan nilai maksimal dari argument
3.  `min()`: mengembalikan nilai minimum dari argument
4.  `pow()`: fungsi pangkat
5.  `sum()`: fungsi penjumlahan
6.  `float()`: parsing ke tipe data float
7.  `str()`: parsing ke string
8.  `type()`: mengembalikan tipe data yang digunakan
9.  `list()`: membuat objek lsit
10.   `dict()`: membuat objek dict
11.   `set()`: membuat objek set
12.   `print()`: untuk mencetak teks
13.   `dir()`: mengembalikan seluruh fungsi atau variabel yang bisa diakses
14.   `len()`: mengembalikan panjang atau jumlah item dalam suatu kontainer
15.   `help()`: Mengembalikan dokumentasi

## Variables

Python dibentuk secara dinamis, dimana variabelnya bisa berubah tipe datanya pada baris mana saja. Bagian ini dapat dicoba di halaman [berikut](https://repl.it/@otakbeku/variables).

Penulisan nama variabel di Python:

1.  Camel Case: huruf pertama di kata pertama tidak kapital. Contoh: `fungsiFaktorPersekutuanTerbesar`
2.  Pascal Case: Seluruh huruf pertama dari setiap kata kapital. Contoh: `FungsiFaktorPersekutuanTerbesar`
3.  Snake Case: setiap kata disambung menggunakan *underscore*. Contoh: `fungsi_faktor_persekutuan_terbesar`

## Operators and Expressions

Bagian ini dapat dicoba di halaman [berikut](https://repl.it/@otakbeku/operators). Operator aritmatika yang tersedia antara lain adalah:

1.  `+`(unary/binary)
2.  `-`(unary/binary)
3.  `*`: operator perkalian
4.  `/`: operator pembagian
5.  `%`: operator modulo
6.  `//` : pembagian kebawah
7.  `**` : operator eksponen

Operator pembanding yang tersedia antara lain adalah:

1.  `==`
2.  `!=`
3.  `<`
4.  `<=`
5.  `>`
6.  `>=`

Operator logik yang tersedia antara lain adalah:

1.  not
2.  or
3.  and

Operator logik digunakan sebagai penghubung pada operasi *chained comparisons*. Selain itu Python juga menyediakan operator `augmented assignment`.

## Strings and Characters

Python memiliki built-in function yang bekerja untuk tipe data String, antara lain:

1.  `chr()`: Mengubah integer ke karakter
2.  `ord()`: kebalikan dari fungsi `chr()`
3.  `len()`
4.  `str()`

String, seperti di bahasa pemograman lainnya, merupakan orderet set yang bersifat immutable. Artinya tidak dapat diubah langsung berdasarkan indeks, melainkan perlu menggunakan fungsi lain. String, menyediakan indexing yang memudahkan untuk melakukan operasi *substring* atau *slicing*. Dari string sendiri, ada fungsi built-in antara lain:

1.  `capitalize()`
2.  `lower()`
3.  `swapcase()`
4.  `title()`
5.  `upper()`
6.  `count()`
7.  `endswith()`
8.  `find()`
9.  `index()`
10.   `startswith()`
11.   `isalnum()`
12.   `isalpha()`
13.   `isdigit()`
14.   `isidentifier()`
15.   `islower()`
16.   `isprintable()`
17.   `isspace()`
18.   `istitle()`
19.   `isupper()`
20.   `center()`
21.   `expandtabs()`
22.   `ljust()`
23.   `lstrip()` 
24.   `replace()`
25.   `rjust()`
26.   `rstrip()`
27.   `strip()`
28.   `zfill()`
29.   `join()`
30.   `partition()`
31.   `split()`
32.   `splitlines()`

Eksplorasi lebih jauh dengan operasi string menggunakan bytes.

## Lists and Tuples

## Dictionaries

## Sets

## Conditional Statements

## "While" Loops

## "For" Loops

## Basic Input, Output and String Formatting

## Reading and Writing Files

## Referensi

Bahan untuk belajar lebih lanjut:

1.  [Python for visual code](https://code.visualstudio.com/docs/languages/python)
2.  [Python Wiki](https://wiki.python.org/moin/BeginnersGuide/Programmers)
3.  [Real Python](https://realpython.com/learning-paths/python3-introduction/)
4.  [Sentdex (direkomendasikan)](https://www.youtube.com/user/sentdex) 
5.  [PEP 8](https://www.python.org/dev/peps/pep-0008/)

Komunitas: [Telegram](https://telegram.me/pythonID)

