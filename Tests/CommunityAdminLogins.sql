DECLARE @companyId INT, @communityId INT, @email VARCHAR(max), @password VARCHAR(max)
DECLARE @tempTable TABLE (
  CompanyId INT,
  CommunityId INT,
  Email VARCHAR(max),
  Password VARCHAR(max)
  )

DECLARE cur CURSOR for
SELECT DISTINCT
  c.CompanyId, 
  c1.CommunityId, 
  u.Email, 
  u.Password 
  FROM Company c
  JOIN Community c1 ON c.CompanyId = c1.CompanyId
  JOIN UserCommunity uc ON c1.CommunityId = uc.CommunityId
  JOIN Users u ON uc.UserId = u.UserId
  JOIN UserRole ur ON uc.UserId = ur.UserId
  JOIN Role r ON ur.RoleId = r.RoleId
  WHERE r.RoleId = 4
  
OPEN cur

  FETCH NEXT FROM cur INTO @companyId, @communityId, @email, @password
  WHILE @@FETCH_STATUS = 0
  BEGIN
    IF NOT EXISTS (SELECT top 1 * FROM @tempTable WHERE CompanyId = @companyId) BEGIN
      INSERT INTO @tempTable (CompanyId, CommunityId, Email, Password)
                  VALUES (@companyId, @communityId, @email, @password);
    END

    FETCH NEXT FROM cur INTO @companyId, @communityId, @email, @password
  END

CLOSE cur
DEALLOCATE cur

SELECT * FROM @tempTable