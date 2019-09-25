# Introduction to Python

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



## Variables

## Operators and Expressions

## Strings and Characters

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

Komunitas: [Telegram](https://telegram.me/pythonID)

