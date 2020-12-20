
# Background

This is a completed django tutorial created by following the  instructions on
https://docs.djangoproject.com/en/3.1/intro/tutorial01/

The tutorial expects to use the default db.sqlite3 database, but I made the adjustment
to use a Postgres Database

# Setup

Run the ./setup_dev_env.sh script on Ubuntu 18.04 or 20.04, which will install the
needed dependencies.

Then set the postgres user password

    1. Run the psql command from the postgres user account: sudo -u postgres psql postgres.
    2. Set the password: \password postgres.
    3. Enter a password.
    4. Close psql. \q.
