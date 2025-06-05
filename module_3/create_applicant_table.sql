-- SQL script to create the applicant table for the GradCafe Data Analysis Project
CREATE TABLE applicant (
    p_id SERIAL PRIMARY KEY, -- Unique identifier
    program TEXT,           -- University and Department
    comments TEXT,          -- Comments
    date_added DATE,        -- Date Added
    url TEXT,               -- Link to Post on Grad Café
    status TEXT,            -- Admission Status
    term TEXT,              -- Start Term
    us_or_international TEXT, -- Student nationality
    gpa FLOAT,              -- Student GPA
    gre FLOAT,              -- Student GRE Quant
    gre_v FLOAT,            -- Student GRE Verbal
    gre_aw FLOAT,           -- Student Average Writing
    degree TEXT             -- Student Program Degree Type
);

-- Add column descriptions
COMMENT ON COLUMN applicant.p_id IS 'Unique identifier';
COMMENT ON COLUMN applicant.program IS 'University and Department';
COMMENT ON COLUMN applicant.comments IS 'Comments';
COMMENT ON COLUMN applicant.date_added IS 'Date Added';
COMMENT ON COLUMN applicant.url IS 'Link to Post on Grad Café';
COMMENT ON COLUMN applicant.status IS 'Admission Status';
COMMENT ON COLUMN applicant.term IS 'Start Term';
COMMENT ON COLUMN applicant.us_or_international IS 'Student nationality';
COMMENT ON COLUMN applicant.gpa IS 'Student GPA';
COMMENT ON COLUMN applicant.gre IS 'Student GRE Quant';
COMMENT ON COLUMN applicant.gre_v IS 'Student GRE Verbal';
COMMENT ON COLUMN applicant.gre_aw IS 'Student Average Writing';
COMMENT ON COLUMN applicant.degree IS 'Student Program Degree Type';
