import click
from crud import (
    create_event,
    get_all_events,
    create_volunteer,
    get_all_volunteers,
    create_assignment,
    get_event_by_id,
    get_volunteer_by_id,
    get_assignments_by_event,
    delete_event as crud_delete_event,
    delete_volunteer as crud_delete_volunteer
)

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
    click.secho("9. Delete Event", fg='yellow')
    click.secho("10. Delete Volunteer", fg='yellow')
    choice = click.prompt("Enter your choice (1-10)", type=int)
    return choice

@click.group()
def cli():
    """Volunteer Coordination System CLI"""
    pass

@cli.command()
def add_event():
    click.secho("Adding a new event...", fg='blue')
    name = click.prompt("Event name")
    date = click.prompt("Date (YYYY-MM-DD)")
    location = click.prompt("Location")
    skills = click.prompt("Required skills (comma-separated)")
    try:
        event = create_event(name, date, location, skills)
        click.secho(f"Event '{event.name}' added successfully with ID {event.id}.", fg='green')
    except ValueError as e:
        click.secho(f"Error: {e}", fg='red')
    except Exception as e:
        click.secho(f"Error adding event: {e}", fg='red')

@cli.command()
def list_events():
    click.secho("Listing all events...", fg='blue')
    events = get_all_events()
    if not events:
        click.secho("No events found.", fg='yellow')
        return
    header = f"{'ID':<5} {'Name':<20} {'Date':<12} {'Location':<15} {'Skills':<20}"
    click.echo(header)
    click.echo("-" * len(header))
    for e in events:
        click.echo(f"{e.id:<5} {e.name:<20} {str(e.date):<12} {e.location:<15} {e.required_skills or '':<20}")

@cli.command()
def add_volunteer():
    click.secho("Adding a new volunteer...", fg='blue')
    name = click.prompt("Volunteer name")
    email = click.prompt("Email")
    phone = click.prompt("Phone")
    skills = click.prompt("Skills (comma-separated)")
    try:
        volunteer = create_volunteer(name, email, phone, skills)
        click.secho(f"Volunteer '{volunteer.name}' added successfully with ID {volunteer.id}.", fg='green')
    except Exception as e:
        click.secho(f"Error adding volunteer: {e}", fg='red')

@cli.command()
def list_volunteers():
    click.secho("Listing all volunteers...", fg='blue')
    volunteers = get_all_volunteers()
    if not volunteers:
        click.secho("No volunteers found.", fg='yellow')
        return
    header = f"{'ID':<5} {'Name':<20} {'Email':<30} {'Phone':<15} {'Skills':<20}"
    click.echo(header)
    click.echo("-" * len(header))
    for v in volunteers:
        click.echo(f"{v.id:<5} {v.name:<20} {v.email:<30} {v.phone or '':<15} {v.skills or '':<20}")

@cli.command()
def assign_volunteer():
    click.secho("Assigning a volunteer to an event...", fg='blue')
    event_id = click.prompt("Event ID", type=int)
    volunteer_id = click.prompt("Volunteer ID", type=int)
    date = click.prompt("Assignment date (YYYY-MM-DD)")
    try:
        event = get_event_by_id(event_id)
        volunteer = get_volunteer_by_id(volunteer_id)
        if not event:
            click.secho(f"Error: Event with ID {event_id} not found.", fg='red')
            return
        if not volunteer:
            click.secho(f"Error: Volunteer with ID {volunteer_id} not found.", fg='red')
            return
        assignment = create_assignment(event_id, volunteer_id, date)
        click.secho(f"Volunteer {volunteer.name} assigned to event {event.name} on {assignment.assignment_date}.", fg='green')
    except ValueError as e:
        click.secho(f"Error: {e}", fg='red')
    except Exception as e:
        click.secho(f"Error assigning volunteer: {e}", fg='red')

@cli.command()
def list_assignments():
    click.secho("Listing assignments for an event...", fg='blue')
    event_id = click.prompt("Event ID", type=int)
    event = get_event_by_id(event_id)
    if not event:
        click.secho(f"Error: Event with ID {event_id} not found.", fg='red')
        return
    assignments = get_assignments_by_event(event_id)
    if not assignments:
        click.secho("No assignments found for this event.", fg='yellow')
        return
    header = f"{'Assignment ID':<15} {'Volunteer':<20} {'Date':<12} {'Status':<10}"
    click.echo(header)
    click.echo("-" * len(header))
    for a in assignments:
        click.echo(f"{a.id:<15} {a.volunteer.name:<20} {str(a.assignment_date):<12} {a.status:<10}")

@cli.command()
def event_report():
    click.secho("Generating event report...", fg='blue')
    event_id = click.prompt("Event ID", type=int)
    event = get_event_by_id(event_id)
    if not event:
        click.secho(f"Error: Event with ID {event_id} not found.", fg='red')
        return
    assignments = get_assignments_by_event(event_id)
    click.secho(f"\nEvent Report: {event.name}", fg='blue')
    click.secho(f"Date: {event.date}", fg='cyan')
    click.secho(f"Location: {event.location}", fg='cyan')
    click.secho(f"Required Skills: {event.required_skills or 'None'}", fg='cyan')
    click.secho(f"Total Volunteers: {len(assignments)}", fg='cyan')
    if not assignments:
        click.secho("No volunteers assigned.", fg='yellow')
        return
    header = f"{'Volunteer Name':<20} {'Email':<30} {'Status':<10}"
    click.echo(header)
    click.echo("-" * len(header))
    for a in assignments:
        click.echo(f"{a.volunteer.name:<20} {a.volunteer.email:<30} {a.status:<10}")

@cli.command(name="delete-event")
def cli_delete_event():
    click.secho("Deleting an event...", fg='blue')
    event_id = click.prompt("Event ID", type=int)
    try:
        crud_delete_event(event_id)
        click.secho(f"Event with ID {event_id} deleted successfully.", fg='green')
    except ValueError as e:
        click.secho(f"Error: {e}", fg='red')
    except Exception as e:
        click.secho(f"Error deleting event: {e}", fg='red')

@cli.command(name="delete-volunteer")
def cli_delete_volunteer():
    click.secho("Deleting a volunteer...", fg='blue')
    volunteer_id = click.prompt("Volunteer ID", type=int)
    try:
        crud_delete_volunteer(volunteer_id)
        click.secho(f"Volunteer with ID {volunteer_id} deleted successfully.", fg='green')
    except ValueError as e:
        click.secho(f"Error: {e}", fg='red')
    except Exception as e:
        click.secho(f"Error deleting volunteer: {e}", fg='red')

def main():
    while True:
        choice = display_menu()
        if choice == 1:
            cli(['add-event'])
        elif choice == 2:
            cli(['list-events'])
        elif choice == 3:
            cli(['add-volunteer'])
        elif choice == 4:
            cli(['list-volunteers'])
        elif choice == 5:
            cli(['assign-volunteer'])
        elif choice == 6:
            cli(['list-assignments'])
        elif choice == 7:
            cli(['event-report'])
        elif choice == 8:
            click.secho("Exiting Volunteer Coordination System. Goodbye!", fg='blue')
            break
        elif choice == 9:
            cli(['delete-event'])
        elif choice == 10:
            cli(['delete-volunteer'])
        else:
            click.secho("Invalid choice. Please select a number between 1 and 10.", fg='red')

if __name__ == '__main__':
    main()
