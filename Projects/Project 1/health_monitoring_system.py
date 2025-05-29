
"""
Health Monitoring System (HMS)
Author: Rayyan
Description: Measures pulse values for 4 hours, detects abnormalities,
warns doctors, and visualizes data using turtle graphics.
"""

import turtle

MIN_LEVEL = 60
MAX_LEVEL = 100
MAX_HEIGHT = 200  # Cap for turtle drawing

def measure_pulse(p1, p2, p3):
    if p1 <= 0 or p2 <= 0 or p3 <= 0:
        raise ValueError("Pulse values must be positive.")
    return (p1 + p2 + p3) / 3

def abnormal(hourly_averages):
    abnormal_hours = []
    for i, avg in enumerate(hourly_averages):
        if avg < MIN_LEVEL or avg > MAX_LEVEL:
            abnormal_hours.append(i + 1)
    return abnormal_hours if abnormal_hours else None

def warning_doctor(abnormal_hours):
    if abnormal_hours:
        for hour in abnormal_hours:
            print(f"WARNING: Abnormal pulse level detected in hour {hour}.")
    else:
        print("All pulse levels are within normal range.")

def read_pulse():
    hourly_averages = []
    for hour in range(1, 5):
        print(f"\nHour {hour}:")
        p1 = int(input("Enter pulse reading 1: "))
        p2 = int(input("Enter pulse reading 2: "))
        p3 = int(input("Enter pulse reading 3: "))
        avg = measure_pulse(p1, p2, p3)
        print(f"Average pulse for hour {hour}: {avg:.2f}")
        hourly_averages.append(avg)
    return hourly_averages

def draw_chart(pulse_averages):
    try:
        screen = turtle.Screen()
        screen.title("Pulse Averages Chart")
        t = turtle.Turtle()
        t.speed(1)
        t.penup()
        t.goto(-150, -100)
        t.pendown()

        for i, avg in enumerate(pulse_averages):
            height = min(avg, MAX_HEIGHT)  # Limit height
            t.fillcolor("skyblue")
            t.begin_fill()
            t.forward(40)
            t.left(90)
            t.forward(height)
            t.right(90)
            t.forward(40)
            t.right(90)
            t.forward(height)
            t.left(90)
            t.end_fill()
            t.penup()
            t.forward(20)
            t.pendown()

        t.penup()
        t.goto(-140, -120)
        for hour in range(1, 5):
            t.write(f"Hour {hour}", align="left", font=("Arial", 10, "normal"))
            t.forward(100)
        t.hideturtle()
        screen.mainloop()

    except turtle.Terminator:
        print("Chart window was closed early. Skipping chart display.")

def test_measure_pulse():
    assert measure_pulse(80, 90, 100) == 90.0
    try:
        measure_pulse(-1, 80, 90)
        assert False
    except ValueError:
        assert True

def test_abnormal():
    assert abnormal([70, 85, 95, 65]) is None
    assert abnormal([70, 85, 105, 65]) == [3]
    assert abnormal([50, 85, 90, 65]) == [1]

def main():
    print("=== Health Monitoring System ===")
    pulse_averages = read_pulse()
    abnormal_hours = abnormal(pulse_averages)
    warning_doctor(abnormal_hours)
    draw_chart(pulse_averages)

# Run tests
test_measure_pulse()
test_abnormal()

# Uncomment to run the full application
main()
