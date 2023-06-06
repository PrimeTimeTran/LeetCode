select name 
from customer c
where NOT c.referee_id = 2 or c.referee_id is null