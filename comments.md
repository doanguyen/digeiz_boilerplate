**Comment on project structure**
- Enforce coding style (black, autopep8), static typing (i.e. mypy)
- Use dependency locking mechanism for separating dev/prod
- Consider using poetry instead of pipenv for faster deps resolve and library build
  
**Points can be improved** 
- For pagination: Limit-offset pagination/Cursor pagination
- Github CD/CI setup
- Add flask debug library, something like Django-Silk for debugging the SQL query
- Consider eager loading to remove the N+1 problem