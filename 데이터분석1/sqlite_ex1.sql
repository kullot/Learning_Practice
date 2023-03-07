-- SELECT 필드명 FROM 테이블명 (WHERE 조건절 LIMIT 숫자);
-- albums 테이블 모두 출력하기기
SELECT * FROM albums;
-- albums 테이블에서 Title, AlbumId 필드만 출력하기(5개)
--LIMIT 갯수만 표시시
SELECT Title, AlbumId FROM albums LIMIT 5;
--WHERE절 이용하기
--SELECT 필드명|* FROM 테이블명 WHERE 조건식 LIMIT 갯수;

--AlbumId가 3인 레코드만 출력하기
SELECT * FROM Albums WHERE AlbumId == 3;

--AlbumId가 5보다 작은 레코드만 출력하기
SELECT * FROM Albums WHERE AlbumId < 5;

--논리연산자 AND, OR, NOT
--AlbumId가 10~19보다 작은 레코드만 출력하기
SELECT * FROM Albums 
	WHERE AlbumId >= 10 AND AlbumId <= 19;
	
--employees 테이블에서 LastName, FirstName, Email
SELECT LastName, FirstName, Email FROM employees;
SELECT  LastName, FirstName, Email  FROM  employees;