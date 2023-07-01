import psycopg2


connection = psycopg2.connect(user='postgres',
                              password='postgres',
                              host='localhost',
                              port='8888',
                              database='postgres')
cursor = connection.cursor()

#cursor.execute('create table users_2 (id varchar(8) primary key, first_name varchar(50), last_name varchar(50), age int, email varchar(50)); commit;')
#cursor.execute("INSERT INTO users_2(id, first_name, last_name, age, email) VALUES ('aaaaaaaa', 'John', 'Dow', 18, 'john.dow@gmail.com'), ('bbbbbbbb','Mortimer', 'Black', 18, 'mort.black@gmail.com'), ('cccccccc','Samanda', 'Black', 18, 'samanda.black@gmail.com');COMMIT;")
cursor.fetchone()
cursor.close()
if connection:
    connection.close()

docker run --name teamcity-server  \
    -v C:\teamcity\data:/data/teamcity_server/datadir \
    -v C:\teamcity\logs:/opt/teamcity/logs  \
    -p 8111:8111 \
    jetbrains/teamcity-server