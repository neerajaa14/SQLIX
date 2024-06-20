from level_db import Session, LevelPageContent

def add_level_content_to_database():
    session = Session()
    session.query(LevelPageContent).delete()

    # Add content to the database
    content_entries = [
         
        LevelPageContent(
            question='What is SQL Injection (SQLi)?',
            option1='A technique used by attackers to manipulate SQL queries',
            option2='A type of encryption algorithm',
            option3='A database management system',
            option4='Create a denial-of-service attack',
            answer='A technique used by attackers to manipulate SQL queries',
            requires_input=0
        ),
        LevelPageContent(
            question='How does SQL Injection work?',
            option1='By injecting malicious SQL code into input fields',
            option2='By using VPN',
            option3='By installing firewalls',
            option4='By encrypting database queries',
            answer='By injecting malicious SQL code into input fields',
            requires_input=0
        ),
        LevelPageContent(
            question='Which of the following is a common consequence of SQL Injection attacks?',
            answer='Data Breaches',
            requires_input=1
        ),
        LevelPageContent(
            question='How can users protect themselves against SQL Injection attacks?',
            answer='By being cautious of suspicious websites',
            requires_input=1
        ),
        LevelPageContent(
            question='Full form of SQL?',
            answer='Structured Querey Language',
            requires_input=1
        ),
        LevelPageContent(
            question='Which regulations require organizations to protect against SQL Injection attacks?',
            option1='GPDR',
            option2='PCI DSS',
            option3='HIPAA',
            option4='All of the above',
            answer='All of the above',
            requires_input=0
        ),
        LevelPageContent(
            question='How can SQL Injection impact the confidentiality of data?',
            answer=' By allowing attackers to access sensitive information stored in a database',
            requires_input=1
        ),
        LevelPageContent(
            question='Which of the following SQL statements is used to retrieve data from a database table',
            option1='CREATE',
            option2='SELECT',
            option3='DELETE',
            option4='UPDATE',
            answer='SELECT',
            requires_input=0
        ),
        LevelPageContent(
            question='How do attackers test for SQL Injection?',
            answer='Quotes',
            requires_input=1
        ),
        LevelPageContent(
            question='What indicates SQL Injection vulnerability?',
            answer='Errors',
            requires_input=1
        ),
        LevelPageContent(
            question='In SQL Injection, what type of statement is typically injected into the input fields of a web application to manipulate the database?',
            option1='SELECT',
            option2='CREATE',
            option3='Malicious SQL code',
            option4='ALTER',
            answer='Malicious SQL code',
            requires_input=0
        ),
        LevelPageContent(
            question='How can parameterized queries help prevent SQL Injection attacks',
            answer='using placeholders for user input, which are then filled in with sanitized values ',
            requires_input=1
        ),
        LevelPageContent(
            question='SQL Injection attacks target which layer of a web application?',
            answer='database',
            requires_input=1
        ),
        LevelPageContent(
            question='What does the SQL command "SELECT * FROM users;" do?',
            option1='Updates all records in the users table',
            option2=' Selects all columns from the users table ',
            option3='Deletes all records in the users table',
            option4='Server-side XSS',
            answer='Inserts a new record into the users table ',
            requires_input=0
        ),
        LevelPageContent(
            question='SQL Injection attacks exploit vulnerabilities in which part of a web application?',
            answer='input',
            requires_input=1
        )
    ]

    for entry in content_entries:
        session.add(entry)

    session.commit()

    session.close()