select distinct v.author_id as id 
from views v
where v.viewer_id = v.author_id
order by v.author_id  ASC