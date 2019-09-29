'''
>> Data types:
python | Java
--------------
int | int 
--------------
float | double
--------------
complex | complex
--------------
complex | complex
--------------
boolean | boolean


>> Data structure:
python | Java
--------------
list | arraylist (linked list)
--------------
dict | HashMap(key, value)
--------------
set | HashSet
--------------
tuple | tuple (beda penulisan)
--------------
string | string


>> Differences:
0. syntax
python -> no semicolon, but put attention to indentation (reason: improve readability of code)
Java -> need semicolon and curli braces

1. String
python -> string = single, double, triple quote
Java -> string = double

2. Data types
python -> dynamic typing (no fixed data type)
Java -> static typing (every variable has fixed data type)

3.0 String concatenation
python -> 
teks = 'langsung'
print('Teksnya bisa digabung',teks)
or
print('Teksnya bisa digabung '+teks)
or
print(f'Teksnya bisa digabung {teks}')

Java -> 
String teks = " langsung";
System.out.println("Teksnya bisa digabung" + teks);

3.1 If-Else-Condition
python -> If statement, put attention to identation
if x > 3:
    x -= 2
    print x
y = x

Else-If statement:
if x > 0:
   print 'positive'
elif x < 0:
   print 'negative'
else:
   print 'zero'

Java -> If statement, put attention to curli braces and semicolon
if (x > 3) {
    x -= 2;
    System.out.println(x);
}
y = x;

3.2 while condition
python ->
x = 11
while x != 0:
    print x
    x /= 2

Java ->
int x = 11;
while (x != 0) {
    System.out.println(x);
    x /= 2;
}

3.3 Boolean operators
python -> and, or, not
Java -> &&, ||, !

3.4 For-loops
python -> 
for i in range(10):
    print(i)

Java ->
for (int i=0;i<10; i++){
    System.out.println(Integer.toString(i));
}

3.5 Dictionaries/Mappings
python -> similar to Java HashMap. Works as switch-case. Cause exception when key is not exist

map = dict() # or map = {}
map['satu'] = 1
map['dua'] = 2
print(map['dua'])
for key in map.keys():
    print(key)
    print(map[key])

Java -> if key doesn't exist, then return none

Map<String, Integer> map = new HashMap<String, Integer>();
map.put("satu", 1);
map.put("dua", 2);
System.out.println(map.get("dua"));
for(String key: map.KeySet()){
    System.out.println(key);
    System.out.println(map.get(key));
}

4. Assignments and arithmathics, return values, function
python -> assignments and arithmathics same as Java, has multiple return value, 
    def give_me_3_number():
        return 1, 2, 3
    -> easy swapping using tuples
    y, x = x,y

Java -> swapping in Java, has void function
    temp = x
    x = y
    y = tmep

5. Interpreted vs compiled
python -> interpreted language; not in 'machine code' and translation occurs when executed
Java -> compiled language; translate (compiled) to 'byte code' and interpreted by JVM 

6. Databases
python -> databases access layers are weaker than Java. Not suite for enterprises
Java -> widely use to connect with database. Mostly use in enterprises

7. Usability
python: shorter code, dynamic programming, easy to understand, good readability
Java: No dynamic typing (static typing is good anw), longer codes, faster than python, has stronger IDE support

8. Practical
python: popular in data, small-to-medium project, DevOps (along with Go), large variety of library
Java: More catchy for Software Engineering, good for enterprises, fewer library but solid (+ hard to maintain), runs on mobile


'''
