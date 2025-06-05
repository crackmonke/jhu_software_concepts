CREATE TABLE [dbo].[ApplicationData] (
  [Id] INT IDENTITY(1,1) PRIMARY KEY,
  program TEXT NOT NULL, -- Combined school_name and program
  degree TEXT NOT NULL,
  date_added DATE NOT NULL,
  status TEXT NOT NULL, -- was decision
  url TEXT NOT NULL, -- was result_url
  term TEXT NOT NULL, -- was semester_year
  us_or_international TEXT NOT NULL, -- was international_american
  gpa FLOAT NULL,
  gre_v FLOAT NULL,
  gre_aw FLOAT NULL,
  gre_ FLOAT NULL,
  comments TEXT NULL -- was comment
)
