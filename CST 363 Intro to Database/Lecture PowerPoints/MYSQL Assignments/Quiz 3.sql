
#5
CREATE OR REPLACE VIEW CourseView AS
SELECT DISTINCT course, fee
FROM course;

select *
from courseview
ORDER BY course;
#6
CREATE OR REPLACE VIEW CatBReedView AS
SELECT PetID, PetName, PetBreed, PetDOB
FROM pet
WHERE PetType='cat';

select *
from CatBReedView
ORDER BY PetName;

UPDATE CatBReedView
SET petname = 'Cedro'
WHERE petid = 5;
#'Cedro'

INSERT INTO CatBReedView(PetID, PetName, PetBreed, PetDOB) VALUES(
    null,'Pat', 'Taby','2011-11-15');
