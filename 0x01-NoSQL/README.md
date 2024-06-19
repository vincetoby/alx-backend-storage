# READ ME

## [100-find](./100-find)
a script that lists all documents with name starting by Holberton in the collection school:

    The database name will be passed as option of mongo command
<pre><code>
guillaume@ubuntu:~/0x01$ cat 100-find | mongo my_db
MongoDB shell version v3.6.3
connecting to: mongodb://127.0.0.1:27017/my_db
MongoDB server version: 3.6.3
{ "_id" : ObjectId("5a90731fd4321e1e5a3f53e3"), "name" : "Holberton school" }
{ "_id" : ObjectId("5a90731fd4321e1e5a3f53e3"), "name" : "Holberton School" }
{ "_id" : ObjectId("5a90731fd4321e1e5a3f53e3"), "name" : "Holberton-school" }
bye
guillaume@ubuntu:~/0x01$

</pre></code>

### explanation of the [code](./100-find)
db.school:

    This part of the code accesses the school collection within the current database. db refers to the current database context you are working in.

.find():

    This is a method that retrieves documents from the specified collection that match the given query criteria. In this case, it will return documents from the school collection.

{"name": { $regex: /^Holberton/ }}:

    This is the query criteria passed to the .find() method.
    "name": This specifies the field that the query is targeting. In this case, it is the name field of the documents within the school collection.
    { $regex: /^Holberton/ }: This is a regular expression (regex) query operator.
        $regex: This operator allows you to perform pattern matching on strings using regular expressions.
        /^Holberton/: This is the regular expression pattern.
            ^: This symbol denotes the start of the string. It means that the pattern must match from the beginning of the string.
            Holberton: This is the specific string pattern that the query is looking for.

So, the entire regex pattern ^Holberton means that the name field must start with the string "Holberton".
