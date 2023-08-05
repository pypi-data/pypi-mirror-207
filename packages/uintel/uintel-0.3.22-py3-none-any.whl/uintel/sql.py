"""Connect to SQL databases.

Connect (or create) databases on postgreSQL servers, as well as upload DataFrames to databases quickly and efficiently.
"""

__all__ = ["connect", "upload"]

import io, sqlalchemy, sqlalchemy_utils, psycopg2, pandas, warnings, ssl, os
from .install import _get_config, _save_config

def connect(database_name: str, host: str, sslmode="require") -> dict:
    """Connect to a database.

    Connect to a given database (e.g. 'chap'), using the stored credentials for SQL for the host (e.g. encivmu-tml62). If the database does not exist, then a new database is created with this databse_name. 

    Args:
        database_name: The name of the database to connect to, or create if it does not exist.
        host: The name or address of the SQL table host.
    
    Returns:
        A dictionary containing a sqlalchemy Engine ('engine') and a psycopg2 connection ('con').
    """

    config = _get_config()
    try:
        credentials = config["sql"][host]
    except KeyError:
        warnings.warn(f"Unfortunately, {host} is not in your saved SQL databases.")
        credentials = {
            "port": int(input(f"What port is the SQL database on {host}? (e.g. 5002) ")),
            "username": input("What is the username to connect to SQL? (e.g. postgres) "),
            "password": input("What is the password to connect to SQL? ")
        }
        # Save this new connection to the UI configuration file
        config["sql"][host] = credentials
        _save_config(config)


    engine = sqlalchemy.create_engine(f"postgresql+psycopg2://{credentials['username']}:{credentials['password']}@{host}/{database_name}?port={credentials['port']}", connect_args={"sslmode":sslmode})

    if not _database_exists(database_name, engine):
        _create_database(engine.url)

    connection = psycopg2.connect(f"host={host} dbname={database_name} user={credentials['username']} password='{credentials['password']}' port={str(credentials['port'])}", sslmode=sslmode)

    return {"engine": engine, "con": connection}
    

def _database_exists(database_name, engine):
    """Check if a posgtreSQL database exists.

    :param url: A SQLAlchemy engine URL.

    Performs backend-specific testing to quickly determine if a database
    exists on the server. ::

        database_exists('postgresql://postgres@localhost/name')  #=> False
        create_database('postgresql://postgres@localhost/name')
        database_exists('postgresql://postgres@localhost/name')  #=> True

    Supports checking against a constructed URL as well. ::

        engine = create_engine('postgresql://postgres@localhost/name')
        database_exists(engine.url)  #=> False
        create_database(engine.url)
        database_exists(engine.url)  #=> True

    Adapted from sqlalchemy_utils.functions.database.database_exists(url) to include SSL encryption
    """
    return bool(sqlalchemy_utils.functions.database._get_scalar_result(engine, f"SELECT 1 FROM pg_database WHERE datname='{database_name}'"))


def _create_database(url, encoding='utf8', template='template1'):
    """Issue the appropriate CREATE DATABASE statement.

    :param url: A SQLAlchemy engine URL.
    :param encoding: The encoding to create the database as.
    :param template:
        The name of the template from which to create the new database. At the
        moment only supported by PostgreSQL driver.

    To create a database, you can pass a simple URL that would have
    been passed to ``create_engine``. ::

        create_database('postgresql://postgres@localhost/name')

    You may also pass the url from an existing engine. ::

        create_database(engine.url)

    Adapted from sqlalchemy_utils.functions.database.database_exists(url) to include SSL encryption
    """

    url = sqlalchemy.engine.url.make_url(url)
    database = url.database
    url = sqlalchemy_utils.functions.database._set_url_database(url, database="postgres")
    engine = sqlalchemy.create_engine(url, isolation_level='AUTOCOMMIT', connect_args={'sslmode':'prefer'})

    with engine.begin() as conn:
        text = "CREATE DATABASE {} ENCODING 'utf8' TEMPLATE template1".format(
            sqlalchemy_utils.functions.orm.quote(conn, database),
            encoding,
            sqlalchemy_utils.functions.orm.quote(conn, template)
        )
        conn.execute(sqlalchemy.text(text))
        conn.execute("CREATE EXTENSION postgis;")

    engine.dispose()


def upload(df: pandas.DataFrame, table_name: str, db: dict, if_exists: str = "replace") -> None:
    """Upload a DataFrame.

    Upload a Pandas Dataframe to a SQL table called table_name. 

    Args:
        df: The pandas.DataFrame to upload.
        table_name: The name of the table to upload the dataframe to.
        db: A dictionary of the SQL database engine and connection.
        if_exists: The action to undertake if the table_name exists. E.g. "replace" or "append".

    Returns:
        None.
    """

    # Truncates the table and sends the column names to sql
    df.head(0).to_sql(table_name, db['engine'], if_exists=if_exists, index=False) 
    
    # Open connection to sql
    conn = db['engine'].raw_connection()
    cur = conn.cursor()
    
    # Send dataframe to stringio
    output = io.StringIO()
    df.to_csv(output, sep='\t', header=False, index=False)
    
    # Send stringio to sql
    output.seek(0)
    cur.copy_from(output, table_name, null="") # null values become ''
    conn.commit()
