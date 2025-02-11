## WeHelp Week 5 Assignment MySQL

### Task 2

```
create database webiste;

use website;

create table member(
id bigint PRIMARY KEY auto_increment,
name VARCHAR(255) NOT NULL,
username VARCHAR(255) NOT NULL,
password VARCHAR(255) NOT NULL,
follower_count INT UNSIGNED NOT NULL DEFAULT 0,
time datetime NOT NULL DEFAULT current_timestamp
);

```

![alt text](<Screenshot 2025-02-10 at 4.16.18 PM.png>)

### Task 3


```
use website;

insert into member (name, username, password) values('test', 'test, 'test');
```
![alt text](<Screenshot 2025-02-10 at 5.14.59 PM.png>)

```
insert into member (name, username, password, follower_count, time)
VALUES
('Frodo', 'frodo_baggins', 'mr.underhill', 298, '1995-02-12'),
('Samwise', 'sam_gamgee', 'shire_mayor', 12947, '1995-09-20'),
('Pippin', 'took_pippin', 'took_my_password', 7878, '1996-04-01'),
('Merry', 'just_merry', 'merry1234', 487, '1997-12-24');

SELECT * FROM member;

SELECT * FROM member
ORDER BY time DESC;

```
![alt text](<Screenshot 2025-02-10 at 6.04.47 PM.png>)

```
SELECT * FROM member
ORDER BY time DESC
LIMIT 3 OFFSET 1;

SELECT * FROM member
WHERE username = 'test';

SELECT * FROM member
WHERE name LIKE '%es%';

SELECT * FROM member
WHERE username = 'test' AND password = 'test';
```
![alt text](<Screenshot 2025-02-10 at 8.33.25 PM.png>)

```
UPDATE member
SET name = 'test2'
WHERE username = 'test';

```

![alt text](<Screenshot 2025-02-10 at 8.40.16 PM.png>)

### Task 4

```
SELECT COUNT(*) FROM member;

SELECT SUM(follower_count) FROM member;

SELECT AVG(follower_count) FROM member;

SELECT AVG(follower_count) AS AverageFollower
FROM (
    SELECT follower_count
    FROM member
    ORDER BY follower_count DESC
    LIMIT 2
) AS FirstTwoRows;
```

![alt text](<Screenshot 2025-02-10 at 10.01.10 PM.png>)

### Task 5