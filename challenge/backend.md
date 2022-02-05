# Alocai backend recruitment task

## Scenario

Year 2271.  
German territory is occupied by Aliens.  
Playing video games is strictly banned because of the Entertainment Limitation For Humans Law.  
Video games black market prices gone crazy.

You're a hacker who has physical access to the old-fashioned Alien PC containing all games that have ever been
developed.  
You're about to download games with your old-fashioned pen-drive and sell them to the rich game collectors.  
There is one issue though: you'll know what's the available space of your pen-drive just 5 minutes before the action.  
So you need to find a way to know which games to pick basing on the pen-drive space to make this risky operation as much
profitable as possible.  
You wanna create a service which will return a combination of games with the highest possible
total value for the given pen-drive space and steal returned games from the computer.

## Requirements

1. Create a Python (>= 3.8) web application using web framework you find appropriate (we use Flask)
   and implement endpoints presented below
2. The application is covered by unit and integration tests using pytest
3. Local deployment, tests and others are run using Docker/docker-compose
4. Repository contains README with local deployment and tests instruction
5. Application uses PostgreSQL as database
6. Codebase is typed and commented
7. Repository is pushed to Github and link is provided to the recruiter
8. Error handling and edge cases

## What we'll appreciate

* Easy to read codebase
* Typing everywhere with mypy
* Well documented both code and API
* Nice project structure
* Ease of setup
* OpenAPI for API docs
* Good Practices
* Any not mentioned valuable additional work

### Endpoints to implement

1. GET /api/v1/status
    * returns appropriate status code and {"database": "healthy"} when the database connection is healthy
    * returns appropriate status code and {"database": "unhealthy"} when the database connection isn't healthy

2. HEAD /api/v1/status
    * Returns appropriate status code when the database connection is healthy
    * Returns appropriate status code when the database connection isn't healthy

3. GET /docs
    * Opens HTML document with endpoint specification

4. POST /api/v1/games
    * Validates the payload and saves the game into the DB
    * Request payload schema:
    ```json
   {
       "name": "Diablo 112", // unique, not empty string 
       "price": 71.7,  // non-negative float
       "space": 1073741824 // positive (1 GB in bytes)
   }
   ```
    * Success sample response payload:
   ```json
   {
       "name": "Fortnite 43",
       "price": 71.7,
       "space": 1073741824
   }
   ```
    * For success and failure return appropriate status codes

5. POST /api/v1/best_value_games?pen_drive_space={POSITIVE_INTEGER}
    * Return a combination with the highest possible total value that fits given pen-drive space
    * Validate pen_drive_space query parameter
    * Success sample response payload:
   ```json
   {
       "games": [
           {
               "name": "Super Game",
               "price": 71.7,
               "space": 1073741824
           },
           {
               "name": "Extra Game",
               "price": 100.78,
               "space": 2147483648
           }
       ],
       "total_space": 3221225472, // total space of games
       "remaining_space": 1024 // empty space on the pen-drive after download
   }
   ```

