# YumNgein
## Getting Started
- Install dependencies using pip
```commandline
  $ python3 -m pip install -r requirements.txt
```

- Create PostgreSql Database and grant to user
```sql
  CREATE DATABASE mydb;
  CREATE USER myuser WITH PASSWORD 'mypassword';
  GRANT ALL PRIVILEGES ON DATABASE mydb TO myuser;
```
- Edit your database's credentials in *settings.py*
- Get *token* from your Facebook App and put it on *settings.py*
- Deploy your app
- Verify webhook
## Basic Sentences (message to our bot)
- Link your facebook account with your name (myname)
```
  i am myname
```
- Borrow 100$ from peter(your creditor)
```
   borrow peter 100
```
- Your debtor(david) returned $400
```
   david return 400
```
