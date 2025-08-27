import click

def display_menu():
    click.secho("Welcome to the Volunteer Coordination System!", fg='blue')
    click.secho("Please select an option:", fg='blue')
    click.secho("1. Add Event", fg='yellow')
    click.secho("2. List Events", fg='yellow')
    click.secho("3. Add Volunteer", fg='yellow')
    click.secho("4. List Volunteers", fg='yellow')
    click.secho("5. Assign Volunteer", fg='yellow')
    click.secho("6. List Assignments", fg='yellow')
    click.secho("7. Event Report", fg='yellow')
    click.secho("8. Exit", fg='yellow')
    choice = click.prompt("Enter your choice (1-8)", type=int)
    return choice

@click.group()
def cli():
    """Volunteer Coordination System CLI"""
    pass

def main():
    while True:
        choice = display_menu()
        if choice == 8:
            click.secho("Exiting Volunteer Coordination System. Goodbye!", fg='blue')
            break
        else:
            click.secho("Invalid choice. Please select a number between 1 and 8.", fg='red')

if __name__ == '__main__':
    main()