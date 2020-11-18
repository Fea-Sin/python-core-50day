
-- 查询所有学生信息
select * from tb_student;

-- 查询所有课程名称及学分（投影和别名）
select couname, coucredit from tb_course;
select couname as 课程名称, coucredit as 学分 from tb_course;

-- 查询所有学生的姓名和性别（条件运算）
select stuname as 姓名, case stusex when 1 then '男' else '女' end as 性别 from tb_student;
select stuname as 姓名, if (stusex, '男', '女') as 性别 from tb_student;

-- 查询所有女学生的姓名和出生日期（筛选）
select stuname, stubirth from tb_student where stusex=0;

-- 查询所有80后学生的姓名、性别和出生日期（筛选）
select stuname, stusex, stubirth from tb_student where stubirth>='1980-1-1' and stubirth<='1989-12-31';
select stuname, stusex, stubirth from tb_student where stubirth between '1980-1-1' and '1989-12-31';

-- 查询姓'杨'的学生姓名和性别（模糊）
select stuname, stusex from tb_student where stuname like '杨%';

-- 查询姓'杨'名字两个字的学生姓名和性别（模糊）
select stuname, stusex from tb_student where stuname like '杨_';

-- 查询姓'杨'名字三个字的学生姓名和性别（模糊）
select stuname, stusex from tb_student where stuname like '杨__';

-- 查询名字中有 '不' 字或 '嫣' 字的学生姓名（模糊）
select stuname, stusex from tb_student where stuname like '%不%' or stuname like '%嫣%';

-- 查询没有录入家庭住址的学生姓名（空值）
select stuname from tb_student where stuaddr is null ;

-- 查询录入了家庭住址的学生姓名（空值）
select stuname from tb_student where stuaddr is not null;

-- 查询选课的所有日期（去重）
select distinct seldate from tb_record;

-- 查询学生的家庭住址（去重）
select distinct  stuaddr from tb_student where stuaddr is not null;

-- 查询男学生的姓名和生日年龄从大到小排序（排序）
select stuname as 姓名, datediff(curdate(), stubirth) div 365 as 年龄 from tb_student where stusex=1 order by 年龄 desc;

-- 查询年龄最大的学生的出生日期（聚合函数）
select min(stubirth) from tb_student;

-- 查询年龄最小的学生的出生日期（聚合函数）
select max(stubirth) from tb_student;

-- 查询男女学生的人数（分组和聚合函数）
select stusex, count(*) from tb_student group by stusex;

-- 查询课程编号为1111的课程的平均成绩（筛选和聚合）
select avg(score) from tb_record where cid=1111;

-- 查询学号为1001的学生所有课程的平均分（筛选和聚合函数）
select avg(score) from tb_record where sid=1001;

-- 查询每个学生的学号和平均成绩（分组和聚合函数）
select sid as 学号, avg(score) from tb_record group by sid;

-- 查询平均成绩大于等于90分的学号和平均成绩
select sid as 学号 , avg(score) as 平均分 from tb_record group by sid having 平均分>=90;

-- 查询年龄最大的学生的姓名（子查询/嵌套查询）
select stuname from tb_student where stubirth=( select min(stubirth) from tb_student );

-- 查询年龄最大的学生姓名和年龄（子查询+运算）
select stuname as 姓名, datediff( curdate(), stubirth ) div 365 as 年龄 from tb_student where stubirth=( select min(stubirth) from tb_student );

-- 查询选了两门以上的课程的学生姓名（子查询/分组条件/集合运算）
select stuname from tb_student where stuid in ( select sid from tb_record group by sid having count(sid)>2 );

-- 查询学生姓名、课程名称以及成绩（连接查询）
select stuname, couname, score from tb_student t1, tb_course t2, tb_record t3 where stuid=sid and couid=cid and score is not null;

-- 查询选课学生的姓名和平均成绩（子查询和连接查询）
select stuname, avgmark from tb_student, ( select sid, avg(score) as avgmark from tb_record group by sid ) temp where stuid=sid;

-- 查询每个学生的姓名和选课数量（左外连接和子查询）
select stuname, ifnull(total, 0) from tb_student left outer join ( select sid, count(sid) as total from tb_record group by sid ) temp on stuid=sid;





















