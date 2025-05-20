from django.shortcuts import render
from django.http import Http404

# Define the tasks for each day
tasks = {
    "sunday": "Shopping",
    "monday": "Reading and finalising homework.",
    "tuesday": "Preparing for IA",
    "wednesday": "Practical implementation of lab.",
    "thursday": "Hanging out with friends.",
    "friday": "Relaxation.",
    "saturday": "Washing clothes and doing remaining works."
}

def index(request):
    # Get the list of days from the tasks dictionary keys
    days_of_week = tasks.keys()
    return render(request, 'index.html', {
        'days': days_of_week
    })

def day_view(request, day):
    # Normalize the day input to lowercase to match dictionary keys
    day_lower = day.lower()

    # Check if the requested day exists in our tasks dictionary
    if day_lower in tasks:
        task = tasks[day_lower]
        return render(request, 'day.html', {
            'day': day.capitalize(), # Capitalize the day for display
            'task': task
        })
    else:
        # Return a 404 error if the day is not found
        raise Http404("Invalid day")