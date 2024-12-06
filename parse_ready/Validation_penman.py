import penman

def validate_amr_file(file_path):
    
    with open('map_el.txt', 'r', encoding='utf-8') as file:
        # Split annotations by double newline
        annotations = file.read().strip().split("\n\n")

    print(f"Found {len(annotations)} AMR annotations to validate.\n")

    for idx, annotation in enumerate(annotations, start=1):
        print(f"Validating AMR #{idx}...")
        try:
            # Attempt to decode the AMR annotation
            graph = penman.decode(annotation)
            print(f"AMR #{idx} is valid!\n")
        except Exception as e:
            print(f"AMR #{idx} is invalid!")
            print(f"Error: {e}\n")
            
# Call the function with your file
validate_amr_file("map_el.txt")


import penman

def check_for_duplicate_nodes(amr_text):
    try:
        graph = penman.decode(amr_text)
        print("AMR is valid")
    except Exception as e:
        print(f"Invalid AMR: {e}")

with open('map_cat.txt', 'r', encoding='utf-8') as f:
    annotations = f.read().strip().split("\n\n")
    for idx, annotation in enumerate(annotations, start=1):
        check_for_duplicate_nodes(annotation)
