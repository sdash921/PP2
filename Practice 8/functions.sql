-- Удаляем старые версии, чтобы не было конфликтов
DROP FUNCTION IF EXISTS get_contacts_by_pattern(text);
DROP FUNCTION IF EXISTS get_contacts_paginated(int, int);

-- Функция поиска по шаблону
CREATE OR REPLACE FUNCTION get_contacts_by_pattern(p text)
RETURNS TABLE(name VARCHAR, phone VARCHAR) AS $$
BEGIN
    RETURN QUERY 
    SELECT c.name, c.phone 
    FROM contacts c
    WHERE c.name ILIKE '%' || p || '%'
       OR c.phone ILIKE '%' || p || '%';
END;
$$ LANGUAGE plpgsql;

-- Функция пагинации
CREATE OR REPLACE FUNCTION get_contacts_paginated(limit_val int, offset_val int)
RETURNS TABLE(id INT, name VARCHAR, phone VARCHAR) AS $$
BEGIN
    RETURN QUERY 
    SELECT c.id, c.name, c.phone 
    FROM contacts c
    ORDER BY id
    LIMIT limit_val OFFSET offset_val;
END;
$$ LANGUAGE plpgsql;