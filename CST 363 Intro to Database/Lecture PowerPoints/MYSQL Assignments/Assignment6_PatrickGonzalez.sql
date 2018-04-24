#Question 1

#Case 1
select id
from city 
where id between 100 and 110 and population > 8000000;

#Case 2
select id 
from city 
where id between 100 and 2000 and population > 8000000;


#Question 2

# largest city for each country

select countrycode, max(population) 
from city
group by countrycode;

/* finding the largest city population for each country can be done with 
but we also want to return the city name from the query and sql grouping allows 
for returning an aggregate value such as max(population), or the grouping column 
such as countrycode but other column values from the row with maximum value. */

select country.name, city.name, f.population
from country 
     inner join city on country.code=city.countrycode 
     inner join ( select countrycode, 
                          max(population) population
                  from city
                  group by countrycode) as f 
         on city.countrycode=f.countrycode 
            and city.population=f.population 
order by 1;

#Question 3
#An alternative way uses a correlated sub-select and the  limit keyword to get the most populous city for each country.

select country.name, city.name as cityname, city.population 
from country inner join city on country.code=city.countrycode 
where city.id = (select id from city city1
                 where city1.countrycode = country.Code           
		      order by city1.population desc limit 1)
order by 1;

#Question 4 
create index  citypop  on city (population); 
Drop index  citypop  on city; 

#Question 5.c Other indexing options
create index  citycode  on city (countrycode); 
Drop index  citycode  on city; 