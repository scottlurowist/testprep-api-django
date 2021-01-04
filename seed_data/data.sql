--------------------------------------------------------------------------------
--
-- data.psql
--
-- This file is a simple script to load some seed data in order to test the 
-- testprep API.
--
--------------------------------------------------------------------------------



DO $$

-- Stores the IDs for the "Grammar" and "Russian Language" categories.
DECLARE grammar_cat_id integer;
DECLARE russian_language_cat_id integer;

-- Stores the ID for the "Russian Grammar 1" test.
DECLARE russian_grammar_test_id integer;

BEGIN

    -- Truncates the many-to-many table that resolves the categories
    -- and tests as well as the category and test tables themselves,
    -- and resets the surrogate primary keys.
    TRUNCATE api_category RESTART IDENTITY CASCADE;
    TRUNCATE api_test RESTART IDENTITY CASCADE;


    -- Insert some categories
    INSERT INTO
        api_category (name, created_at, updated_at)
    VALUES
        ('Trivia', current_timestamp, current_timestamp); 

    INSERT INTO
        api_category (name, created_at, updated_at)    
    VALUES
        ('Grammar', current_timestamp, current_timestamp)
        RETURNING id INTO grammar_cat_id;

    INSERT INTO
        api_category (name, created_at, updated_at)    
    VALUES
        ('Russian Language', current_timestamp, current_timestamp)
        RETURNING id INTO russian_language_cat_id;
            

    -- Insert some tests
    INSERT INTO
        api_test (name, description, is_published, created_at, updated_at)
    VALUES
        ('Russian Grammar 1', 'Basic Russian Grammar', false, current_timestamp,
         current_timestamp)
    RETURNING id INTO russian_grammar_test_id;  
     

    -- Insert the primary keys as foreign keys in the many-to-many table.
    INSERT INTO
         api_test_categories (test_id, category_id)
    VALUES
         (russian_grammar_test_id, grammar_cat_id),
         (russian_grammar_test_id, russian_language_cat_id);

    -- Insert a few questions.
    INSERT INTO
         api_question(question_text, question_type, created_at, updated_at, test_id)
    VALUES
         ('What is the accusative case?', 'selectBest', current_timestamp, current_timestamp, russian_grammar_test_id),
         ('What is the dative case?', 'selectBest', current_timestamp, current_timestamp, russian_grammar_test_id);         


END $$;

