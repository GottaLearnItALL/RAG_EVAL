

# Learn how to go from SQL to NoSQL
<a name="SQLtoNoSQL"></a>

If you are an application developer, you might have some experience using a relational database management system (RDBMS) and Structured Query Language (SQL). As you begin working with Amazon DynamoDB, you will encounter many similarities, but also many things that are different. *NoSQL* is a term used to describe nonrelational database systems that are highly available, scalable, and optimized for high performance. Instead of the relational model, NoSQL databases (like DynamoDB) use alternate models for data management, such as key-value pairs or document storage. For more information, see [What is NoSQL?](http://aws.amazon.com/nosql).

Amazon DynamoDB supports [PartiQL](https://partiql.org/), an open-source, SQL-compatible query language that makes it easy for you to efficiently query data, regardless of where or in what format it is stored. With PartiQL, you can easily process structured data from relational databases, semi-structured and nested data in open data formats, and even schema-less data in NoSQL or document databases that allow different attributes for different rows. For more information, see [PartiQL query language](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/ql-reference.html).

The following sections describe common database tasks, comparing and contrasting SQL statements with their equivalent DynamoDB operations.

**Note**  
The SQL examples in this section are compatible with the MySQL RDBMS.  
The DynamoDB examples in this section show the name of the DynamoDB operation, along with the parameters for that operation in JSON format. 

**Topics**
+ [Choosing between relational (SQL) and NoSQL](SQLtoNoSQL.WhyDynamoDB.md)
+ [Differences in accessing a relational (SQL) database and DynamoDB](SQLtoNoSQL.Accessing.md)
+ [Differences between a relational (SQL) database and DynamoDB when creating a table](SQLtoNoSQL.CreateTable.md)
+ [Differences between getting table information from a relational (SQL) database and DynamoDB](SQLtoNoSQL.GetTableInfo.md)
+ [Differences between a relational (SQL) database and DynamoDB when writing data to a table](SQLtoNoSQL.WriteData.md)
+ [Differences between a relational (SQL) database and DynamoDB when reading data from a table](SQLtoNoSQL.ReadData.md)
+ [Differences between a relational (SQL) database and DynamoDB when managing indexes](SQLtoNoSQL.Indexes.md)
+ [Differences between a relational (SQL) database and DynamoDB when modifying data in a table](SQLtoNoSQL.UpdateData.md)
+ [Differences between a relational (SQL) database and DynamoDB when deleting data from a table](SQLtoNoSQL.DeleteData.md)
+ [Differences between a relational (SQL) database and DynamoDB when removing a table](SQLtoNoSQL.RemoveTable.md)