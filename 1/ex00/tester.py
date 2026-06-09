from give_bmi import give_bmi, apply_limit

def main():
    print("--- SUBJECT TEST ---")
    height = [2.71, 1.15]
    weight = [165.3, 38.4]
    
    bmi = give_bmi(height, weight)
    print(bmi, type(bmi))
    print(apply_limit(bmi, 26))
    
    print("\n--- ERROR HANDLING TESTS ---")
    
    # Error Case 1: Different list lengths
    print("Test 1: Different list lengths")
    try:
        give_bmi([2.71], [165.3, 38.4])
        print("Failure: Exception was not raised!")
    except Exception as e:
        print(f"Success: Exception caught - {e}")

    # Error Case 2: Invalid type in height
    print("\nTest 2: Invalid type in height list (string)")
    try:
        give_bmi([2.71, "1.15"], [165.3, 38.4])
        print("Failure: Exception was not raised!")
    except Exception as e:
        print(f"Success: Exception caught - {e}")
        
    # Error Case 3: Invalid type in weight
    print("\nTest 3: Invalid type in weight list (list)")
    try:
        give_bmi([2.71, 1.15], [165.3, [38.4]])
        print("Failure: Exception was not raised!")
    except Exception as e:
        print(f"Success: Exception caught - {e}")

    # Error Case 4: Invalid limit type in apply_limit
    print("\nTest 4: Invalid limit type (string instead of int)")
    try:
        apply_limit(bmi, "26")
        print("Failure: Exception was not raised!")
    except Exception as e:
        print(f"Success: Exception caught - {e}")

    # Error Case 5: Invalid bmi type inside apply_limit array
    print("\nTest 5: Invalid bmi list type")
    try:
        apply_limit([22.5, "29.0"], 26)
        print("Failure: Exception was not raised!")
    except Exception as e:
        print(f"Success: Exception caught - {e}")

if __name__ == "__main__":
    main()