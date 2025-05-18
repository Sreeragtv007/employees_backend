from datetime import datetime, timedelta, time
import random
from .models import Employee

TRAINING_START = time(8, 0)
TRAINING_END = time(18, 0)

def get_available_slots():
    """Generate training slots between 8am and 6pm, each 1 hour."""
    slots = []
    current = datetime.combine(datetime.today(), TRAINING_START)
    end = datetime.combine(datetime.today(), TRAINING_END)
    while current < end:
        slots.append(current)
        current += timedelta(hours=1)
    return slots

def schedule_trainings():
    """Assign training slots to employees in groups of 10-25."""
    employees = list(Employee.objects.all())
    random.shuffle(employees)

    slots = get_available_slots()
    slot_idx = 0

    for i in range(0, len(employees), 25):
        batch = employees[i:i+25]
        if slot_idx >= len(slots):
            break
        training_time = slots[slot_idx]
        for emp in batch:
            emp.training_time = training_time
            emp.save()
        slot_idx += 1
