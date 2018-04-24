
/*
USE exam1;

DELIMITER//

CREATE FUNCTION LastNameFirst

RETURNS STRING

BEGIN
	DELCARE fullName string;
    
    SELECT concat(lastname, ', ', firstname)
    INTO fullname
    FROM student
    ORDER BY lastname, firstname;
    
    return(fullname);
    

end//
DELIMITER;
*/
#deterministic lastname + ', '+ firstname

#/*
#USE quiz3;
DROP FUNCTION IF EXISTS LastNameFirst;
Delimiter //
CREATE FUNCTION LastNameFirst
(
	FirstName CHAR(25), 
	LastName CHAR(25)
)
Returns VARCHAR(60)

BEGIN
DECLARE FullName VARCHAR(60);
	
	SELECT concat(lastname , ', ', firstname)
    INTO fullname;
    
	RETURN FullName;
END //
#/*
select lastnamefirst(CustomerFirstName,CustomerLastName) AS fname
from customer;
#order by lastname, firstname;