import typer
from typing_extensions import Annotated

import mysql.connector


app = typer.Typer()


@app.command()
def dump(
    database: Annotated[str, typer.Argument(..., help="Database name")],
    output_file: Annotated[str, typer.Argument(..., help="Output file name")],
    host: Annotated[str, typer.Option("", "--host", "-h", help="Database host")] = "",
    user: Annotated[str, typer.Option("", "--user", "-u", help="Database user")] = "",
    password: Annotated[str, typer.Option("", "--password", "-p", help="Database password")] = "",
):
    """Create a MySQL database dump."""
    try:
        # Connect to the database
        connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database,
        )

        # Create a cursor object
        cursor = connection.cursor()

        # Execute the mysqldump command

        cursor.execute(
            "mysqldump "
            f"--user={user} " if user else ""
            f"--password={password} " if password else ""
            f"--host={host} " if host else ""
            f"{database} > {output_file}"
        )

        # Close the cursor and connection
        cursor.close()
        connection.close()

        # Print success message
        typer.echo(f"MySQL database dump created successfully: {output_file}")
    except mysql.connector.Error as e:
        typer.echo(f"Error creating MySQL database dump: {e}")


if __name__ == "__main__":
    app()
