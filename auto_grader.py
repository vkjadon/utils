import os
import importlib.util
import traceback
import csv

# 📂 Submissions directory (students' folders inside)
SUBMISSIONS_DIR = "submissions"

# 📄 Output CSV
OUTPUT_FILE = "grades.csv"

# ✅ Define assignments, function names, and test cases
ASSIGNMENTS = {
    "question1.py": {
        "function": "square",
        "tests": [(2, 4), (-3, 9), (0, 0), (5, 25)]
    },
    "question2.py": {
        "function": "factorial",
        "tests": [(0, 1), (1, 1), (5, 120), (6, 720)]
    }
}

def run_tests(student_file, function_name, test_cases):
    """Run tests on a student's file for a specific function."""
    try:
        # Load student file dynamically
        spec = importlib.util.spec_from_file_location("student_module", student_file)
        student_module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(student_module)

        # Check if required function exists
        if not hasattr(student_module, function_name):
            return 0, f"❌ No function '{function_name}' found"

        func = getattr(student_module, function_name)

        score = 0
        feedback = []
        for i, (inp, expected) in enumerate(test_cases, 1):
            try:
                result = func(inp)
                if result == expected:
                    score += 1
                    feedback.append(f"Test {i}: ✅")
                else:
                    feedback.append(f"Test {i}: ❌ Expected {expected}, got {result}")
            except Exception as e:
                feedback.append(f"Test {i}: ❌ Error {str(e)}")

        return score, " | ".join(feedback)

    except Exception:
        return 0, f"❌ Could not run: {traceback.format_exc()}"

def main():
    results = []

    # Iterate over student folders
    for student in os.listdir(SUBMISSIONS_DIR):
        student_path = os.path.join(SUBMISSIONS_DIR, student)
        if not os.path.isdir(student_path):
            continue  # skip non-folder files

        student_result = {"Student": student}
        total_score = 0

        # Run each assignment
        for qfile, qdata in ASSIGNMENTS.items():
            file_path = os.path.join(student_path, qfile)
            if not os.path.exists(file_path):
                student_result[qfile] = "❌ Missing File"
                continue

            score, feedback = run_tests(file_path, qdata["function"], qdata["tests"])
            student_result[qfile] = f"{score}/{len(qdata['tests'])} | {feedback}"
            total_score += score

        student_result["Total"] = total_score
        results.append(student_result)

    # Write results to CSV
    with open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as f:
        fieldnames = ["Student"] + list(ASSIGNMENTS.keys()) + ["Total"]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(results)

    print(f"✅ Grading complete. Results saved in {OUTPUT_FILE}")

if __name__ == "__main__":
    main()
