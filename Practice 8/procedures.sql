-- Удаляем старые версии процедур
DROP PROCEDURE IF EXISTS upsert_contact(varchar, varchar);
DROP PROCEDURE IF EXISTS delete_contact(varchar);
DROP PROCEDURE IF EXISTS bulk_insert_contacts(text[], text[]);

-- Процедура: UPSERT (обновление или вставка)
CREATE OR REPLACE PROCEDURE upsert_contact(p_name VARCHAR, p_phone VARCHAR)
LANGUAGE plpgsql AS $$
BEGIN
    IF EXISTS (SELECT 1 FROM contacts WHERE name = p_name) THEN
        UPDATE contacts SET phone = p_phone WHERE name = p_name;
    ELSE
        INSERT INTO contacts(name, phone) VALUES(p_name, p_phone);
    END IF;
END;
$$;

-- Процедура: Удаление
CREATE OR REPLACE PROCEDURE delete_contact(target VARCHAR)
LANGUAGE plpgsql AS $$
BEGIN
    DELETE FROM contacts WHERE name = target OR phone = target;
END;
$$;

-- Процедура: Массовая вставка с проверкой
CREATE OR REPLACE PROCEDURE bulk_insert_contacts(names TEXT[], phones TEXT[])
LANGUAGE plpgsql AS $$
DECLARE
    i int;
BEGIN
    FOR i IN 1..array_length(names, 1) LOOP
        -- Простая валидация: телефон должен быть длиннее 5 символов
        IF length(phones[i]) >= 6 THEN
            INSERT INTO contacts(name, phone) VALUES (names[i], phones[i]);
        ELSE
            RAISE NOTICE 'Skipping invalid contact: % with phone %', names[i], phones[i];
        END IF;
    END LOOP;
END;
$$;