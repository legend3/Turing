-- 系统属性
    -- 包或任何生成的/中间字符串的最大大小
show variables like 'max_allowed%';
select 4194304/1024/1024;-- 转换单位为MB
        -- max_allowed_packet修改为20MB
        -- 重新登录数据库连接，再次查询生效.(此方式重启数据库后，回到默认值)
set global max_allowed_packet = 2*1024*1024*10;

-- 查看数据库(现有)总数据大小
select sum(data_length)/1024/1024 as data_length,sum(index_length)/1024/1024 as index_length,sum(data_length+index_length)/1024/1024 as sum from information_schema.tables;

--查看数据库中各库大小
select table_schema, sum(data_length+index_length)/1024/1024 as total_mb, 
sum(data_length)/1024/1024 as data_mb, sum(index_length)/1024/1024 as index_mb, 
count(*) as tables, curdate() as today from information_schema.tables group by table_schema order by 2 desc;


--查看单个库的大小
select concat(truncate(sum(data_length)/1024/1024,2),'mb') as data_size, 
concat(truncate(sum(max_data_length)/1024/1024,2),'mb') as max_data_size, 
concat(truncate(sum(data_free)/1024/1024,2),'mb') as data_free, 
concat(truncate(sum(index_length)/1024/1024,2),'mb') as index_size 
from information_schema.tables where table_schema = 'mydata';

--单个表状态
show table status from mydata where name = 'maptable1';


-- 查看单库下所有表的状态
select table_name, (data_length/1024/1024) as data_mb , (index_length/1024/1024) 
as index_mb, ((data_length+index_length)/1024/1024) as all_mb, table_rows 
from tables;



-- load_file()函数
  -- secure_file_priv 这个参数用于限制数据的导入和导出
    -- secure_file_priv可以设置为如下：
    -- 如果为空，则此参数没有作用，即不做限制
    -- 如果设置为目录，则数据的导入导出就只会限制在此目录中，并且这个目录必须事先存在，服务器并不会创建它
    -- 如果设为NULL，服务器会禁止数据的导入导出操作
show global variables like '%secure%';-- 查看secure_file_priv变量指向的允许上传文件的位置
    -- 这是一个只读参数，不能使用set global来修改
    在mysql配置文件/etc/my.cnf中[mysqld]配置段添加如下配置
      [mysqld]
      # 只允许在C:\Users\Administrator\Desktop目录下导入、导出
      secure_file_priv=C:\Users\Administrator\Desktop
--案例：
select load_file('C:\\Users\\Administrator\\Desktop\\contents.txt');-- 二进制数字
    -- jdbc下路径不识别“\”或“\\”,要用“/”!!!

USE mydata;
create table test(
  tt TEXT NOT NULL
);
insert into test(tt) values(load_file('C:\\Users\\Administrator\\Desktop\\contents.txt'));
-- drop table test;

select tt from mydata.test;



show databases;
use mydata;
show tables;
select summary from mydata.maptable1;

-- 创建数据库
CREATE DATABASE IF NOT EXISTS mydata DEFAULT CHARACTER SET 'utf8mb4' DEFAULT COLLATE 'utf8mb4_general_ci';-- 创建数据库(MySQL 的数据存储区将以目录方式表示 MySQL 数据库)

-- information_schema：主要存储了系统中的一些数据库对象信息，比如用户表信息、列信息、权限信息、字符集信息和分区信息等。
-- mysql：MySQL 的核心数据库，类似于 SQL Server 中的 master 表，主要负责存储数据库用户、用户访问权限等 MySQL 自己需要使用的控制和管理信息。常用的比如在 mysql 数据库的 user 表中修改 root 用户密码。
-- performance_schema：主要用于收集数据库服务器性能参数。
-- sakila：MySQL 提供的样例数据库，该数据库共有 16 张表，这些数据表都是比较常见的，在设计数据库时，可以参照这些样例数据表来快速完成所需的数据表。
-- sys：MySQL 5.7 安装完成后会多一个 sys 数据库。sys 数据库主要提供了一些视图，数据都来自于 performation_schema，主要是让开发者和使用者更方便地查看性能问题。
-- world：world 数据库是 MySQL 自动创建的数据库，该数据库中只包括 3 张数据表，分别保存城市，国家和国家使用的语言等内容。

-- 查询数据库
SHOW DATABASES;-- 查询所有数据库
SHOW DATABASES LIKE 'm%';-- 查询m开头的数据库
SHOW DATABASES LIKE '%cloud%';-- 查询包含cloud的数据库
SHOW DATABASES LIKE '%schema';-- 查询以shema结尾的数据库

-- 修改数据库
SHOW CREATE DATABASE mydata;-- 查看cloud_note数据库的定义声明
SHOW VARIABLES LIKE 'character%';-- 查看当前数据库字符集
SHOW VARIABLES LIKE 'collation_%';-- 查看当前数据库的校验规则(数据库排序规则)
ALTER DATABASE mydata CHARACTER SET 'utf8mb4';-- 修改cloud_note数据库字符集
ALTER DATABASE mydata COLLATE 'utf8mb4_general_ci';-- 修改cloud_note数据库校验规则(数据库排序规则)

-- 删除数据库
DROP DATABASE IF EXISTS mydata;-- 删除mydata库

-- 选择数据库
USE mydata;

-- 存储引擎
	-- InnoDB 事务型数据库的首选引擎，支持事务安全表（ACID），支持行锁定和外键。MySQL 5.5.5 之后，InnoDB 作为默认存储引擎。
	-- MyISAM 是基于 ISAM 的存储引擎，并对其进行扩展，是在 Web、数据仓储和其他应用环境下最常使用的存储引擎之一。MyISAM 拥有较高的插入、查询速度，但不支持事务。
	-- MEMORY 存储引擎将表中的数据存储到内存中，为查询和引用其他数据提供快速访问。

SHOW ENGINES;-- 查询可用存储引擎
SET default_storage_engine='InnoDB'-- 设置存储引擎

-- 创建表
USE mydata;-- 指定库
 CREATE TABLE emp (
  EMPNO INT PRIMARY KEY AUTO_INCREMENT,
  ENAME    VARCHAR(10),
  JOB      VARCHAR(9),
  MGR      INT,
  HIREDATE DATETIME,
  SAL      DECIMAL(7,2),
  COMM     DECIMAL(7,2),
  DEPTNO   DECIMAL(2)
);
CREATE TABLE dept (
  DEPTNO DECIMAL (2) PRIMARY KEY,
  DNAME VARCHAR (14),
  LOC VARCHAR (13)
) ENGINE = INNODB DEFAULT CHARSET = "UTF8mb4";

SHOW CREATE TABLE dept;-- 显示创建表时的CREATE TABLE语句（加上“\G”参数之后，可使显示的结果更加直观，易于查看。）

SHOW TABLES;-- 查询表


-- 修改数据表
	-- ADD COLUMN <列名> <类型>
	-- CHANGE <旧列名> <新列名> <新列类型>
	-- MODIFY <列名> <新类型>
	-- DROP COLUMN <列名>
	-- RENAME TO <新表名>
ALTER TABLE dept ADD COLUMN pid INT FIRST;-- 增加列
ALTER TABLE dept CHANGE pid dip VARCHAR(255);-- 修改字段名称
ALTER TABLE dept MODIFY dip INT;-- 修改字段类型
ALTER TABLE dept DROP dip;-- 删除字段
ALTER TABLE dept RENAME TO deptno;-- 修改表名

SELECT * FROM dept;
SHOW TABLES;

-- 删除表
DROP TABLE dept;

DESC emp;

SELECT * FROM emp;

-- 分区
SHOW VARIABLES LIKE '%partition%';-- 查询分区（mysql5.6以下版本）
SHOW PLUGINS;-- 查询分区（mysql5.6以上版本）

当有主键/唯一约束字段时，不能使用主键/唯一字段之外的其他字段分区！！！
 CREATE TABLE emp1 (-- 创建（没有主键/唯一约束）分区
  empid INT,
  salary DECIMAL (7, 2),
  birth_date DATE
) ENGINE = INNODB PARTITION BY HASH(MONTH(birth_date)) PARTITIONS 6;-- 通过birth_date字段分区

此处设置id为主键；如果此时却用store_id字段进行分区，因此报错："A PRIMARY KEY must include all columns in the table's partitioning function"
 CREATE TABLE emp2 (
  -- 创建（有主键/唯一约束）分区
  id INT NOT NULL,
  ename VARCHAR (30),
  hired DATE NOT NULL DEFAULT '1970-01-01',
  separated DATE NOT NULL DEFAULT '9999-12-31',
  job VARCHAR (30) NOT NULL,
  store_id INT NOT NULL,
  PRIMARY KEY (id)-- id为主键
) ENGINE = INNODB PARTITION BY RANGE (id) (
  PARTITION p0 VALUES LESS THAN (10),
  PARTITION P1 VALUES LESS THAN (20),
  PARTITION P2 VALUES LESS THAN (30)
  );
 
DESC emp2;
DROP TABLE emp2;

-- 分区之Range：利用取值范围将数据分成分区，区间要连续并且不能互相重叠，使用VALUE LESS THAN操作符进行分区定义。
 CREATE TABLE emp3 (
  id INT NOT NULL,
  ename VARCHAR (30),
  hired DATE NOT NULL DEFAULT '1970-01-01',
  separated DATE NOT NULL DEFAULT '9999-12-31',
  job VARCHAR (30) NOT NULL,
  store_id INT NOT NULL
) PARTITION BY RANGE(store_id) (
PARTITION p0 VALUES LESS THAN (10),
PARTITION P1 VALUES LESS THAN (20),
PARTITION p2 VALUES LESS THAN (30)
  );

DESC emp3;

INSERT INTO emp3 (
  id,
  ename,
  hired,
  separated,
  job,
  store_id
) VALUE (7934, 'Mike', '1986-08-14', '9999-12-30', 'CLECK', 18);-- 如果插入的store_id不在区间值范围，则报错:Table has no partition for value 50

ALTER TABLE emp3 ADD PARTITION (PARTITION p3 VALUES LESS THAN MAXVALUE);-- 增加p3分区，满足p3分区的值为store_id小于最大值
增加p3分区后，再插入store_id大于30的数据(此类数据会被存入p3分区中)
INSERT INTO emp3 (
  id,
  ename,
  hired,
  separated,
  job,
  store_id
) VALUE (7934, 'Mike', '1986-08-14', '9999-12-30', 'CLECK', 50);

SELECT * FROM emp3;


mysql5.1仅仅支持整数列分区,(日期或者字符串列上进行分区，就得使用函数进行转换)
 CREATE TABLE emp4 (
  id INT NOT NULL,
  ename VARCHAR (30),
  hired DATE NOT NULL DEFAULT '1970-01-01',
  separated DATE NOT NULL DEFAULT '9999-12-31',
  job VARCHAR (30) NOT NULL,
  store_id INT NOT NULL
) PARTITION BY RANGE(YEAR(separated)) (-- 分区键separated如果是NULL值会被当作一个最小值来处理！
PARTITION p0 VALUES LESS THAN (1995),
PARTITION P1 VALUES LESS THAN (2000),
PARTITION p2 VALUES LESS THAN (2005)
  );
 
SELECT * FROM emp4;


mysql5.5以后提供了"RANGE COLUMNS"分区支持非整数分区
 CREATE TABLE emp5 (
  id INT NOT NULL,
  ename VARCHAR (30),
  hired DATE NOT NULL DEFAULT '1970-01-01',
  separated DATE NOT NULL DEFAULT '9999-12-31',
  job VARCHAR (30) NOT NULL,
  store_id INT NOT NULL
) PARTITION BY RANGE COLUMNS(separated) (-- 分区键separated如果是NULL值会被当作一个最小值来处理！
 PARTITION p0 VALUES LESS THAN ('1996-01-01'),
 PARTITION P1 VALUES LESS THAN ('2001-01-01'),
 PARTITION p2 VALUES LESS THAN ('2006-01-01')
);
ALTER TABLE emp5 ADD PARTITION (PARTITION p3 VALUES LESS THAN ('9999-12-31'));

DESC emp5;

INSERT INTO emp5 (
  id,
  ename,
  hired,
  separated,
  job,
  store_id
) VALUE (7934, 'Mike', '1986-08-14', '2005-06-13', 'CLECK', 50);

SELECT YEAR(separated) FROM emp5;-- 取DATE的年
SELECT TO_DAYS(separated) FROM emp5;-- 将DATE转换成天
SELECT TO_SECONDS(separated) FROM emp5;-- 将DATE转换成秒

RANGE分区功能特别适用于一下两种情况：
	当需要删除过期的数据时(p0,1996-01-01的数据)
ALTER TABLE emp5 DROP PARTITION p0;
	经常运行包含分区键的查询(store_id > 25的数据);因此在也是设置RANGE分区的参考！
EXPLAIN PARTITIONS SELECT COUNT(1) FROM emp3 WHERE store_id >=25;

	统计(符合的字段的)结果(统计null与不统计null)
	SELECT COUNT(*) FROM emp5;-- 统计表所有字段的行数
	SELECT COUNT(*) FROM emp5 WHERE	ename IS NULL;-- 统计表所有字段中为空的行数
	SELECT COUNT(1) FROM emp5;-- <与count(*)时一个意思！>计算一共有多少符合条件的行（1并不是表示第一个字段，而是表示一个固定值。其实就可以想成表中有这么一个字段，这个字段就是固定值1，count(1)，就是计算一共有多少个1。）
	SELECT COUNT(1) FROM emp5 WHERE	ename IS NOT NULL;
	SELECT COUNT('ename') FROM emp5;-- 统计表中ename字段的行数；count(*) 跟 count(1) 的结果一样，都包括对NULL的统计，而count(column) 是不包括NULL的统计
	一般情况下，Select COUNT (*)和Select COUNT(1)两着返回结果是一样的，假如表没有主键(PRIMARY KEY), 那么count(1)比count(*)快，
	如果有主键的话，那主键作为count的条件时候count(主键)最快，如果你的表只有一个字段的话那count(*)就是最快的。


SELECT * FROM emp3;

-- List分区
List分区是从属于一个枚举列表的值的集合，RANGE分区是从属于一个连续区间值的集合；
List分区不存在类似VALUES LESS THAN MAXVALUE这样包含其他值在内的定义方式，将要匹配的任意值都必须在值列表(X,Y)中找到。

mysql5.5以下版本，仅支持partition BY LIST(INT类型)
 CREATE TABLE expenses1 (
  expense_date DATE NOT NULL,
  category INT,
  amount DECIMAL(10,3))
  PARTITION BY LIST(category) (
	PARTITION p0 VALUES IN(3,5),
	PARTITION p1 VALUES IN(1,10),
	PARTITION p2 VALUES IN(4,9),
	PARTITION p3 VALUES IN(2),
	PARTITION p4 VALUES IN(6)
);
ALTER TABLE expenses1 ADD PARTITION(PARTITION p5 VALUES IN(8));-- 建表后添加p7分区

EXPLAIN PARTITIONS SELECT COUNT(*) FROM expenses1;-- 查看表的分区信息

INSERT INTO expenses1 (expense_date, category, amount) VALUE ('2020-02-02', 100, 2020.23);-- 因为category字段为100，不满足各分区的条件，报错：Table has no partition for value 100

mysql5.5及以上版本通过'LIST COLUMNS'支持非整数分区！！！
 CREATE TABLE expenses2 (
  expense_date DATE NOT NULL,
  category VARCHAR(30),
  amount DECIMAL(10,3))
  PARTITION BY LIST COLUMNS(category) (
	PARTITION p0 VALUES IN('loding','food'),
	PARTITION p1 VALUES IN('flights','groud transportation','tarin'),
	PARTITION p2 VALUES IN('car','walk'),
	PARTITION p3 VALUES IN('apple'),
	PARTITION p4 VALUES IN('orage')
);
INSERT INTO expenses2(expense_date, category, amount) VALUES ('2020-02-02', 'fuck', 2020.23);-- 不满足分区，报错:Table has no partition for value from column_list
INSERT INTO expenses2(expense_date, category, amount) VALUES ('2020-02-02', 'orage', 2020.23);-- 满足分区！

SELECT * FROM expenses2;


-- Columns分区
	Mysql5.5后才引入)引入Columns分区解决了Mysql5.5版本之前RANGE和LIST分区只支持整数分区，从而导致需要额外的函数计算得到整数或者通过额外的转换表来转换为整数再分区的问题
	
	RANGE columns和LIST COLUMNS分区都支持整数、日算起时间、字符串三大数据类型
	所有整数类型：tinyint、smallint、mediumint、int和bigint；其他数据类型都不支持
	日期时间类型：date和datetime
	字符串类型：char、varchar、binary和varbinary；不支持text和blob类型作为分区键。

	注意：Columns仅支持一个或多个字段名作为分区键，不同与RANGE 和 LIST分区！！！
	
Columns支持多列分区！！！	
CREATE TABLE rc3(a INT,b INT) PARTITION BY RANGE COLUMNS(a,b) (
PARTITION p1 VALUES LESS THAN (0,10),-- a,b的组合分区
PARTITION p2 VALUES LESS THAN (10,10),
PARTITION p3 VALUES LESS THAN (10,20),
PARTITION p4 VALUES LESS THAN (10,35),
PARTITION p5 VALUES LESS THAN (10,MAXVALUE),
PARTITION p6 VALUES LESS THAN (MAXVALUE,MAXVALUE)
);

SELECT * FROM rc3;
	
	-- ？？？range COLUMNS分区键的比较是基于元组的比较！也就是基于字段组的比较，这和之前RANGE分区键的比较有些差异。
	
-- Hash分区，主要用来分散热点都，确保数据再预先确定个数的分区中尽可能平均分布。(对一个表的Hash分区时，mysql会对分区键应用一个散列函数，以此确定数据应当放在N个分区中的哪个分区中)
	MySQL支持两种HASH分区，常规HASH分区和线性HASH分区(LINEARHASH分区)
		常规HASH使用的是取模算法
		线性HASH分区使用的是一个线性的2的幂的运算法则
	
 CREATE TABLE emp6 (
  id INT NOT NULL,
  ename VARCHAR (30),
  hired DATE NOT NULL DEFAULT '1970-01-01',
  separated DATE NOT NULL DEFAULT '9999-12-31',
  job VARCHAR (30) NOT NULL,
  store_id INT NOT NULL
) PARTITION BY HASH(store_id) PARTITIONS 4;-- PARTITION BY HASH(expr) PARTITIONS num——expr：表示某列值或一个基于某列值返回一个整数住的表达式，num是一个非负整数，表示分割成区的数量，默认你num为1。

INSERT INTO emp6(id, ename, hired, separated, job, store_id) VALUE(1, 'tom', '2020-01-01', '9999-12-31', 'Cleck', 234);

根expr的值与num是可以计算出，此expr值的列数据会保存在哪个区的。"N=MOD(expr,num)"
SELECT MOD(234,4) FROM DUAL;-- 2
确认
EXPLAIN PARTITIONS SELECT * FROM emp6 WHERE store_id=234;-- p2




CREATE TABLE if not exists cba(
t INT NOT NULL PRIMARY KEY, 
v VARCHAR(20)
) PARTITION BY RANGE(t) (
PARTITION p0 VALUES LESS THAN (10),
PARTITION p1 VALUES LESS THAN (20)
);

desc cba;

CREATE TABLE IF NOT EXISTS nba(
t INT NOT NULL PRIMARY KEY, 
v VARCHAR(20)
) PARTITION BY RANGE(t) (
PARTITION p0 VALUES LESS THAN (MAXVALUE)
);
DESC nba;




set @n int default 1;
DROP DATABASE IF EXISTS concat('mydata', n);
CREATE DATABASE IF NOT EXISTS concat(`mydata`, n) DEFAULT CHARACTER SET 'utf8mb4' COLLATE 'utf8_general_ci';

