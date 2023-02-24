import unittest

# Function to evaluate car speed
def evaluate_car_speed(speed):
    if speed < 0:
        return "Invalid"
    elif speed < 40:
        return "Low"
    elif speed < 120:
        return "Normal"
    elif speed < 200:
        return "High"
    elif speed < 220:
        return "V.High"
    else:
        return "Invalid"

# Function to evaluate student scores
def evaluate_student_score(score):
    if score < 0:
        return "Invalid"
    elif score < 50:
        return "Failed"
    elif score < 65:
        return "Passed"
    elif score < 75:
        return "Good"
    elif score < 85:
        return "V.Good"
    elif score <= 100:
        return "Excellent"
    else:
        return "Invalid"

# Unit tests for the functions
class TestFunctions(unittest.TestCase):

    # Test suite for evaluate_car_speed function
    def test_evaluate_car_speed_positive_cases(self):
        self.assertEqual(evaluate_car_speed(20), "Low")
        self.assertEqual(evaluate_car_speed(60), "Normal")
        self.assertEqual(evaluate_car_speed(180), "High")
        self.assertEqual(evaluate_car_speed(215), "V.High")

    def test_evaluate_car_speed_negative_cases(self):
        self.assertEqual(evaluate_car_speed(-10), "Invalid")
        self.assertEqual(evaluate_car_speed(300), "Invalid")

    # Test suite for evaluate_student_score function
    def test_evaluate_student_score_positive_cases(self):
        self.assertEqual(evaluate_student_score(30), "Failed")
        self.assertEqual(evaluate_student_score(60), "Passed")
        self.assertEqual(evaluate_student_score(70), "Good")
        self.assertEqual(evaluate_student_score(80), "V.Good")
        self.assertEqual(evaluate_student_score(90), "Excellent")
        

    def test_evaluate_student_score_negative_cases(self):
        self.assertEqual(evaluate_student_score(-10), "Invalid")
        self.assertEqual(evaluate_student_score(120), "Invalid")

if __name__ == '__main__':
    unittest.main()
