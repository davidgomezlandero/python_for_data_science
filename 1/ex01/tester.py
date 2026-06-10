from array2D import slice_me


if __name__ == "__main__":
    family = [[1.80, 78.4],
              [2.15, 102.7],
              [2.10, 98.5],
              [1.88, 75.2]]

    print("--- Valid Slices ---")
    print("1. Standard slice (0, 2):")
    print(slice_me(family, 0, 2))
    
    print("\n2. Negative end index (1, -2):")
    print(slice_me(family, 1, -2))
    
    print("\n3. Negative start and end indices (-3, -1):")
    print(slice_me(family, -3, -1))
    
    print("\n4. Out of bounds end index (handled by NumPy) (1, 10):")
    print(slice_me(family, 1, 10))

    print("\n--- Error Handling Tests ---")
    
    print("5. Mismatched list sizes:")
    try:
        bad_family_size = [[1.80, 78.4], [2.15]]
        slice_me(bad_family_size, 0, 2)
    except Exception as e:
        print(f"Caught Exception: {e}")

    print("\n6. Invalid family type (dictionary instead of list):")
    try:
        bad_family_type = {"height": 1.80, "weight": 78.4}
        slice_me(bad_family_type, 0, 2)
    except Exception as e:
        print(f"Caught Exception: {e}")

    print("\n7. Invalid start/end types (float/str instead of int):")
    try:
        slice_me(family, 0.5, "2")
    except Exception as e:
        print(f"Caught Exception: {e}")